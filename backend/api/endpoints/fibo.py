# endpoints/fibo.py
from typing import Annotated
from fastapi import Request, Depends
from fastapi import APIRouter
from pydantic import BaseModel, Field
from .util import verify_api_key
import loguru
from sqlalchemy.orm import Session
from ..db import get_db, Computation, DeletedItem
# TODO: adding a deleted items table


# Requests
class FiboRequest(BaseModel):
    number: Annotated[int, Field(description="Retrieve n-th number from fibo series")]


# Response
class FiboResponse(BaseModel):
    cached: Annotated[
        bool, Field(description="If it has been retrieved from cache or not")
    ]
    answer: Annotated[int, Field(description="The n-th number of fibo series")]
    api_key: Annotated[str, Field("The given API key")]


# API related
router = APIRouter(
    prefix="/fibo",
    tags=["fibo"],
    responses={404: {"description": "Not found"}},
)


# helper functions
@router.get("/")
async def get_root_fibo():
    return "good fibo"


@router.delete("/")
async def delete_cache(
    request: Request,
    api_key=Depends(verify_api_key),
    db: Session = Depends(get_db),  # type: ignore
):
    loguru.logger.info("Emptying cache for fibo")

    deleted_items = request.app.state.cache.clear("fibo")

    for k, v in deleted_items:
        loguru.logger.info(f"Deleted from cache: {k} -> {v}")
        db.add(
            DeletedItem(
                key=k,
                value=v,
                operation="fibo",
                reason="API DELETE",
            )
        )

    db.commit()
    return deleted_items


@router.post("/", tags=["fibo"], summary="Populate up to n-th number in fibo series")
async def populate(
    payload: FiboRequest, request: Request, api_key=Depends(verify_api_key)
):
    n = payload.number
    f1 = 1
    f2 = 1
    cache = request.app.state.cache
    cache.set("fibo(1)", 1)
    for i in range(2, n):
        c = f1 + f2
        f1 = f2
        f2 = c
        cache.set(f"fibo({i})", c)


# main function
@router.post(
    "/retrieve",
    response_model=FiboResponse,
    tags=["fibo"],
    summary="Retrieving the n-th number of fibo",
)
async def fibo_operation(
    payload: FiboRequest,
    request: Request,
    api_key=Depends(verify_api_key),
    db: Session = Depends(get_db),  # type: ignore
):
    cache = request.app.state.cache
    key = f"fibo({payload.number})"

    cached_item = cache.get(key)
    if cached_item is not None:
        result = int(cached_item)  # safe cast bcs stored as str
        loguru.logger.info(f"Retrieved from in-memory cache for fibo: {result}")

        db.add(
            Computation(
                operation="fibo",
                input=key,
                result=str(result),
                cached=True,
                api_key=api_key,
            )
        )
        db.commit()

        return FiboResponse(answer=result, cached=True, api_key=str(api_key))

    n = payload.number
    loguru.logger.info(f"Computing and caching Fibonacci up to index: {n}")

    f1, f2 = 1, 1
    result = 1
    for i in range(2, n + 1):
        result = f1 + f2
        f1, f2 = f2, result
        cache.set(f"fibo({i})", result)  # populate intermediate values

    cache.set(key, result)

    db.add(
        Computation(
            operation="fibo",
            input=key,
            result=str(result),
            cached=False,
            api_key=api_key,
        )
    )
    db.commit()

    return FiboResponse(answer=result, api_key=str(api_key), cached=False)
