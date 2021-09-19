from sqlalchemy import Column, Integer, Float

from database.mysql import Base


class FlatItem(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True)
    new_hot_water = Column(Float)
    new_cold_water = Column(Float)
    new_day_electricity = Column(Float)
    new_night_electricity = Column(Float)
    flat_number = Column(Integer)
    current_hot_water = Column(Float)
    current_cold_water = Column(Float)
    current_day_electricity = Column(Float)
    current_night_electricity = Column(Float)
