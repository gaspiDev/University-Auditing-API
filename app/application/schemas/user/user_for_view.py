from typing import Optional
from pydantic import BaseModel

from app.domain.entities.university import University


class UserForView(BaseModel):
  id: int
  name: str
  lastname: str
  dni: int
  university: Optional[University] = None
