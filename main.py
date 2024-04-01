from pydantic.json_schema import SkipJsonSchema
# SkipJsonSchema[None]
from typing import List, Set, Union, Dict

from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, SkipJsonSchema[None]] = None
    price: float
    tax: Union[float, SkipJsonSchema[None]] = None
    tags: Set[str] = set()
    images: Union[List[Image], SkipJsonSchema[None]] = None


class Offer(BaseModel):
    name: str
    description: Union[str, SkipJsonSchema[None]] = None
    price: float
    items: List[Item]


@app.post("/offers/")
async def create_offer(offer: Offer = Body(embed=True)):
    return offer


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

