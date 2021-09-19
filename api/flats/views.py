from fastapi import Depends
from sqlalchemy.orm import Session
from database.mysql import get_db
from app.flats import crud, models


async def get_flat():
    pass


def get_flat(flat_id: int, db: Session = Depends(get_db)):
    return db.query(models.FlatItem).filter(models.FlatItem.id == flat_id).first()


def get_flats(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    flats = crud.get_flats(db, skip=skip, limit=limit)
    return flats
