from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    detail: str

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}", responses={404: {"model": ErrorResponse}})
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}