from sqlalchemy import Column, Integer, String
from app.database.database import Base
from pydantic import BaseModel

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# class User(BaseModel):
#     id: int
#     username: str

# class UserCreate(BaseModel):
#     username: str
#     password: str