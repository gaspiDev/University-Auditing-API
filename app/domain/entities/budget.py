from typing import Optional
from sqlmodel import SQLModel, Field

class Budget(SQLModel, table=True):
  __tablename__ = "budgets"
  
  id: Optional[int] = Field(default=None, primary_key=True)
  type: str
  year: int
  total_budget: float
  approved_by: Optional[str] = None
  isActive: Optional[bool] = True