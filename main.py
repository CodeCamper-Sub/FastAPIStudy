from pydantic.json_schema import SkipJsonSchema
# SkipJsonSchema[None]
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | SkipJsonSchema[None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | SkipJsonSchema[None] = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | SkipJsonSchema[None] = None


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    # Equivalent
    # UserInDB(
    #     username="john",
    #     password="secret",
    #     email="john.doe@example.com",
    #     full_name=None,
    # )

    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
