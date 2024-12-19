from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field
from datetime import date

from app.domain.entities.expense import Expense
from app.domain.entities.user import User

class University(SQLModel, table=True):
  __tablename__ = "universities"

  id: Optional[int] = Field(default=None, primary_key=True)
  budget_id: int = Field(default=None, foreign_key="budgets.id")
  budget: Optional["Budget"] = Relationship(back_populates="universities")
  dean_id: Optional[int] = Field(default=None, foreign_key="users.id", unique=True)
  dean: Optional[User] = Relationship(back_populates="university")
  expenses: List[Expense] = Relationship(back_populates="university")
  name: str = Field(unique=True)
  province: str
  city: str
  established: date
  address: Optional[str] = Field(default=None, unique=True)
  contact_email: Optional[str] = Field(default=None, unique=True)