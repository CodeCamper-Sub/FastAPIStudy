from pydantic.json_schema import SkipJsonSchema
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, SkipJsonSchema[None]] = None
    price: float
    tax: Union[float, SkipJsonSchema[None]] = None


class User(BaseModel):
    username: str
    full_name: Union[str, SkipJsonSchema[None]] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results