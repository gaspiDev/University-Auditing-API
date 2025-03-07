from typing import Optional
from pydantic import BaseModel


class ExpenseForUpdate(BaseModel):
    id: int
    amount: Optional[float]
