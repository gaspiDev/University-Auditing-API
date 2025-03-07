from pydantic import BaseModel


class BudgetForView(BaseModel):
    id: int
    type: str
    year: int
    total_budget: float
    approved_by: str
