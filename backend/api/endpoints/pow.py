# endpoints/pow.py
from fastapi import Request, Depends
from typing import Annotated, Union
from fastapi import APIRouter
from pydantic import BaseModel, Field
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..db import get_db, Computation, DeletedItem
import loguru
from .util import verify_api_key

supported_types = ["int", "float", "complex"]


# Requests
class PowRequest(BaseModel):
    a: Annotated[Union[int, float, complex], Field(description="First number")]
    b: Annotated[Union[int, float, complex], Field(description="Second number")]


# Response
class PowResponse(BaseModel):
    cached: Annotated[
        bool, Field(description="If it has been retrieved from cache or not")
    ]
    answer: Annotated[
        Union[int, float, complex], Field(description="The exponentiation result")
    ]
    api_key: Annotated[str, Field("The given API key")]


# API related
router = APIRouter(
    prefix="/pow",
    tags=["power"],
    responses={404: {"description": "Not found"}},
)


# helper functions
@router.get("/")
async def get_supported_types():
    loguru.logger.info("Getting all supported types")
    return supported_types


# to empty all the cache
@router.delete("/")
async def delete_cache(
    request: Request,
    api_key=Depends(verify_api_key),
    db: Session = Depends(get_db),  # type: ignore
):
    loguru.logger.info("Emptying cache for pow")

    deleted_items = request.app.state.cache.clear("pow")

    for k, v in deleted_items:
        loguru.logger.info(f"Deleted from cache: {k} -> {v}")
        db.add(
            DeletedItem(
                key=k,
                value=v,
                operation="pow",
                reason="API DELETE",
            )
        )

    db.commit()
    return deleted_items


# main function
@router.post(
    "/{operand_type}",
    response_model=PowResponse,
    tags=["power"],
    summary="Exponentiation operation",
)
async def pow_operation(
    operand_type: str,
    payload: PowRequest,
    request: Request,
    api_key=Depends(verify_api_key),
    db: Session = Depends(get_db),  # type: ignore
):
    if operand_type not in supported_types:
        loguru.logger.warning("Got an unsupported operand type")
        raise HTTPException(status_code=400, detail="Unsupported operand type")

    key = f"pow({payload.a},{payload.b})"
    cache = request.app.state.cache
    cached_result = cache.get(key)

    if cached_result is not None:
        result = cached_result
        if operand_type == "int":
            result = int(float(result))
        elif operand_type == "float":
            result = float(result)
        elif operand_type == "complex":
            a = complex(payload.a if "j" in str(payload.a) else f"{payload.a}+0j")
            b = complex(payload.b if "j" in str(payload.b) else f"{payload.b}+0j")
            result = a**b  # Re-evaluation not needed if you store complex properly

        loguru.logger.info(f"Retrieved from in-memory cache: {result}")

        db.add(
            Computation(
                operation="pow",
                input=key,
                result=str(result),
                cached=True,
                api_key=api_key,
            )
        )
        db.commit()

        return PowResponse(answer=result, cached=True, api_key=str(api_key))

    try:
        if operand_type == "int":
            result = int(str(payload.a)) ** int(str(payload.b))
        elif operand_type == "float":
            result = float(str(payload.a)) ** float(str(payload.b))
        elif operand_type == "complex":
            result = complex(payload.a) ** complex(payload.b)
        else:
            raise ValueError("Unsupported operand type")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Computation error: {str(e)}")

    # Store in cache
    loguru.logger.info(f"Set to in-memory cache: {key} = {result}")
    cache.set(key, str(result))

    db.add(
        Computation(
            operation="pow",
            input=f"{payload.a},{payload.b}",
            result=str(result),
            cached=False,
            api_key=api_key,
        )
    )
    db.commit()

    return PowResponse(answer=result, api_key=str(api_key), cached=False)
