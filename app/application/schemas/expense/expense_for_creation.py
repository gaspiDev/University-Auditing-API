from datetime import date
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field

from app.domain.enums.category_enum import CategoryEnum


class ExpenseForCreation(BaseModel):
  date: date
  amount: float