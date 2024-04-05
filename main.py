from pydantic.json_schema import SkipJsonSchema
# SkipJsonSchema[None]
from typing import Annotated

from fastapi import FastAPI, Form, Query

app = FastAPI()


@app.post("/login/")
async def login(*, username: str = Form(max_length=10, validation_alias="aliasUsername"), password: Annotated[str, Form()]):
    return {"username": username}