from typing import Union

from fastapi import FastAPI, Query

from pydantic.json_schema import SkipJsonSchema

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Union[str, SkipJsonSchema[None]] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        deprecated=True,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# @app.get("/items/")
# async def read_items(q: Union[str, SkipJsonSchema[None]] = Query(default=None, alias="item-query")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results