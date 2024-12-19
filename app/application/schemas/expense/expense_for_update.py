from typing import Optional
from pydantic import BaseModel

from app.domain.enums.category_enum import CategoryEnum


class ExpenseForUpdate(BaseModel):
  id: int
  amount: Optional[float]