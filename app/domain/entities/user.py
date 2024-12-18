from typing import Optional
from sqlmodel import Relationship, SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    dni: int = Field(unique=True)
    password: str = Field(unique=True)
    name: Optional[str] = None
    lastname: Optional[str] = None
    isActive: Optional[bool] = True
    university: Optional["University"] = Relationship(back_populates="dean")
  