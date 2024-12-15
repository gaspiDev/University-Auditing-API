from pydantic import BaseModel


class UserForView(BaseModel):
  id: int
  name: str
  lastname: str
  dni: int
  isDean: bool
