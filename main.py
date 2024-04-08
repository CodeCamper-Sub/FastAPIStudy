from pydantic.json_schema import SkipJsonSchema
# SkipJsonSchema[None]
from typing import Annotated

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: str | SkipJsonSchema[None] = None):
    return q


def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor, use_cache=False)],
    last_query: Annotated[str | SkipJsonSchema[None], Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_or_cookie": query_or_default}