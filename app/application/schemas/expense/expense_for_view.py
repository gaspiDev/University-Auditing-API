from typing import Optional
from pydantic import BaseModel
from datetime import date

from app.domain.entities.university import University
from app.domain.enums.category_enum import CategoryEnum

class ExpenseForView(BaseModel):
  id: int
  date: date
  amount: float
  category: Optional[CategoryEnum] = None
  
  # TODO: Expense is using university id but User is using the nested object,
  # there should be a consistent approach
  university_id: int