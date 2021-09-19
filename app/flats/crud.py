from sqlalchemy.orm import Session

from . import models
from database.mysql import engine

models.Base.metadata.create_all(bind=engine)


def get_flat(db: Session, flat_id: int):
    return db.query(models.FlatItem).filter(models.FlatItem.id == flat_id).first()


def get_flats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FlatItem).offset(skip).limit(limit).all()


# def create_flat(db: Session, user: schemas.UserCreate):
#     db_flat = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
