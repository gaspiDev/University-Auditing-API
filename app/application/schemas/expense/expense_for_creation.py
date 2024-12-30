from datetime import date
from typing import Optional

from pydantic import BaseModel

# TODO: This import is not used
from sqlmodel import Field

# TODO: Use __init__ to expose values and simplify imports to be 
# from app.domain import Category Enum
from app.domain.enums.category_enum import CategoryEnum 


class ExpenseForCreation(BaseModel):
  date: date  # TODO: Whenever possible use datetime instead of date
  amount: float