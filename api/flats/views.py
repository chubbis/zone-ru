from fastapi import Body, Request, Depends
from pydantic import Field

from app.flats.models import FlatItem
from app.flats.schemas import FlatItemUpdate


async def get_flat(flat_id):
    return await FlatItem.get_flat(flat_id)


def get_flats():
    return FlatItem.get_flats()


async def update_flat(
    flat_id: int,
    new_data: FlatItemUpdate = Body(...),
):
    return await FlatItem.update_flat(flat_id, new_data)


async def get_result(flat_id: int):
    return await FlatItem.get_result(flat_id)
