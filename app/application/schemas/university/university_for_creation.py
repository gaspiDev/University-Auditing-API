from datetime import date
from typing import Optional
from pydantic import BaseModel


class UniversityForCreation(BaseModel):
    budget_type: str
    name: str
    province: str
    city: str
    established: date
    address: Optional[str]
    contact_email: Optional[str]
