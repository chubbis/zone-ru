from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database.mysql import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password_hash = Column(String)
    user_name = Column(String)
