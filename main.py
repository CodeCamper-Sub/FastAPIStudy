from pydantic.json_schema import SkipJsonSchema
# SkipJsonSchema[None]
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | SkipJsonSchema[None], Cookie()] = None):
    return {"ads_id": ads_id}