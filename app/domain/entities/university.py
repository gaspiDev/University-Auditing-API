from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

class University(SQLModel, table=True):
  __tablename__ = "universities"

  id: Optional[int] = Field(default=None, primary_key=True)
  budget_id: Optional[int] = Field(default=None, foreign_key="budgets.id")
  dean_id: Optional[int] = Field(default=None, foreign_key="users.id", unique=True)
  name: str = Field(unique=True)
  province: str
  city: str
  established: date
  address: Optional[str] = Field(default=None, unique=True)
  contact_email: Optional[str] = Field(default=None, unique=True)
  isActive: Optional[bool] = True