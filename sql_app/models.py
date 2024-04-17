from sqlmodel import Field, Relationship, SQLModel
from typing import List


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)

    items: List["Item"] = Relationship(back_populates="owner")


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str = Field(index=True)

    owner_id: int = Field(foreign_key="user.id")
    owner: User = Relationship(back_populates="items")
