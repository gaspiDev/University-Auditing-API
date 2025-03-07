from typing import Optional
from pydantic import BaseModel


class UniversityForUpdate(BaseModel):
    budget_id: Optional[int]
    name: Optional[str]
    province: Optional[str]
    city: Optional[str]
    address: Optional[str]
    contact_email: Optional[str]
