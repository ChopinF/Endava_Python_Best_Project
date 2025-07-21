# endpoints/factorial.py
from fastapi import Request, Depends
from typing import Annotated
from fastapi import APIRouter
from pydantic import BaseModel, Field
from .util import verify_api_key
import loguru
from sqlalchemy.orm import Session
from ..db import get_db, Computation, DeletedItem


# Requests
class FactRequest(BaseModel):
    number: Annotated[
        int, Field(description="Retrieve n-th number from factorial series")
    ]


# Response
class FactResponse(BaseModel):
    cached: Annotated[
        bool, Field(description="If it has been retrieved from cache or not")
    ]
    answer: Annotated[int, Field(description="The n-th number of factorial series")]
    api_key: Annotated[str, Field("The given API key")]


# API related
router = APIRouter(
    prefix="/fact",
    tags=["fact"],
    responses={404: {"description": "Not found"}},
)


# helper functions
@router.get("/")
async def get_root_fact():
    return "good fact"


# to empty all the cache


@router.delete("/")
async def delete_cache(
    request: Request,
    api_key=Depends(verify_api_key),
    db: Session = Depends(get_db),  # type: ignore
):
    loguru.logger.info("Emptying cache for fact")

    deleted_items = request.app.state.cache.clear("fact")

    for k, v in deleted_items:
        loguru.logger.info(f"Deleted from cache: {k} -> {v}")
        db.add(
            DeletedItem(
                key=k,
                value=v,
                operation="fact",
                reason="API DELETE",
            )
        )

    db.commit()
    return deleted_items


@router.post(
    "/", tags=["fact"], summary="Populate up to n-th number in factorial series"
)
async def populate(
    payload: FactRequest, request: Request, api_key=Depends(verify_api_key)
):
    n = payload.number
    f = 1
    cache = request.app.state.cache
    cache.set("fact(1)", 1)
    for i in range(2, n + 1):
        f *= i
        cache.set(f"fact({i})", f)


# main function
@router.post(
    "/retrieve",
    response_model=FactResponse,
    tags=["fact"],
    summary="Retrieving the n-th number of factorial",
)
async def fact_operation(
    payload: FactRequest,
    request: Request,
    api_key=Depends(verify_api_key),
    db: Session = Depends(get_db),  # type: ignore
):
    cache = request.app.state.cache
    key = f"fact({payload.number})"

    cached_item = cache.get(key)
    if cached_item is not None:
        result = int(cached_item)
        loguru.logger.info(f"Retrieved from in-memory cache for fact: {result}")

        db.add(
            Computation(
                operation="fact",
                input=str(payload.number),
                result=str(result),
                cached=True,
                api_key=api_key,
            )
        )
        db.commit()

        return FactResponse(answer=result, cached=True, api_key=str(api_key))

    # Compute factorial
    n = payload.number
    loguru.logger.info(f"Computing and caching factorial for: {n}")

    f = 1
    result = 1
    cache.set("fact(1)", f)
    for i in range(2, n + 1):
        f *= i
        cache.set(f"fact({i})", f)
        result = f

    cache.set(key, result)

    db.add(
        Computation(
            operation="fact",
            input=str(payload.number),
            result=str(result),
            cached=False,
            api_key=api_key,
        )
    )
    db.commit()

    return FactResponse(answer=result, api_key=str(api_key), cached=False)
