from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field

from app.domain.entities.university import University

class Budget(SQLModel, table=True):
  __tablename__ = "budgets"
  
  id: Optional[int] = Field(default=None, primary_key=True)
  type: str
  year: int
  total_budget: float
  approved_by: Optional[str]
  universities: List[University] = Relationship(back_populates="budget")
  isActive: Optional[bool] = True