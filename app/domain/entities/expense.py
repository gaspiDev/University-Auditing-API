from datetime import date
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from app.domain.enums.category_enum import CategoryEnum


class Expense(SQLModel, table=True):
    __tablename__ = "expenses"

    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    amount: float
    category: Optional[CategoryEnum] = None
    university_id: int = Field(default=None, foreign_key="universities.id")
    university: Optional["University"] = Relationship(back_populates="expenses")
    isActive: Optional[bool] = True
