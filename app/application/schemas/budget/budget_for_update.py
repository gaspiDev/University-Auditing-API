from typing import Optional
from pydantic import BaseModel


class BudgetForUpdate(BaseModel):
    id: int
    total_budget: float
    approved_by: Optional[str]
