from typing import Optional
from pydantic import BaseModel


class UserForUpdate(BaseModel):
  name: Optional[str]
  lastname: Optional[str]