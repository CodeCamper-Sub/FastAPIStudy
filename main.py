from typing import Set, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.post(
    "/items/",
    response_model=Item, 
    tags=["items"],
    summary="Create an Item",
    response_description="The created Item"
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@app.get("/items/", tags=["items"], description="Read All Items")
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"], deprecated=True)
async def read_users():
    return [{"username": "johndoe"}]