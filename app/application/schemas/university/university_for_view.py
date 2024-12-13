from datetime import date
from pydantic import BaseModel


class UniversityForView(BaseModel):
  id: int
  budget_id: int
  name: str
  province: str
  city: str
  address: str
  established: date
  contact_email: str