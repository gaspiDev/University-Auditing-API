from typing import Optional
from pydantic import BaseModel


class BudgetForCreation(BaseModel):
  type: str
  year: int
  total_budget: float
  approved_by: Optional[str] = None