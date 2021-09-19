from typing import List, Optional

from pydantic import BaseModel


class FlatBase(BaseModel):
    flat_number: str


class ItemCreate(FlatBase):
    pass


class Flat(FlatBase):
    id: int

    class Config:
        orm_mode = True
