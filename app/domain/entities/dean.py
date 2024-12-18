from typing import Optional
from sqlmodel import Field, SQLModel


class Dean(SQLModel, table=True):
  __tablename__ = "deans"

  id: Optional[int] = Field(default=None, primary_key=True)
  