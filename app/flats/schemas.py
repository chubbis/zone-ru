from typing import Optional
from pydantic import BaseModel


class FlatBase(BaseModel):
    id: int
    flat_number: int


class FlatItem(FlatBase):
    hot_water: Optional[float]
    cold_water: Optional[float]
    day_el: Optional[float]
    night_el: Optional[float]


class FlatItemUpdate(BaseModel):
    new_cold_water: Optional[float]
    new_day_el: Optional[float]
    new_night_el: Optional[float]
    new_hot_water: Optional[float]
    hot_water: Optional[float]
    cold_water: Optional[float]
    day_el: Optional[float]
    night_el: Optional[float]

    class Config:
        orm_mode = True


