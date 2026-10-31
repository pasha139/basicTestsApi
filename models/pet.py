from pydantic import BaseModel
from typing import Optional, Literal


class Category(BaseModel):
    id: int = 0
    name: str = ""


class Tag(BaseModel):
    id: int = 0
    name: str = ""


class Pet(BaseModel):
    # required
    name: str
    photoUrls: list[str]

    # optional
    id: Optional[int] = None
    category: Optional[Category] = None
    tags: Optional[list[Tag]] = None
    status: Literal["available", "pending", "sold"] = "available"