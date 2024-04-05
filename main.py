from pydantic.json_schema import SkipJsonSchema
# SkipJsonSchema[None]
from typing import List, Union

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Union[List[str], SkipJsonSchema[None]] = Header(default=None)):
    return {"X-Token values": x_token}