from typing import Optional
from pydantic import BaseModel


class UserForCreation(BaseModel):
  dni: int
  password: str
  name: Optional[str] = None
  lastname: Optional[str] = None