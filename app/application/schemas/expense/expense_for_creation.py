from datetime import date
from pydantic import BaseModel


class ExpenseForCreation(BaseModel):
    date: date
    amount: float
