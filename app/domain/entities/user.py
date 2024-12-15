from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
  __tablename__ = "users"

  id: Optional[int] = Field(default=None, primary_key=True)
  dni: int = Field(unique= True)
  password: str = Field(unique= True)
  name: Optional[str] = None
  lastname: Optional[str] = None
  isDean: Optional[bool] = False
  isActive: Optional[bool] = True
  