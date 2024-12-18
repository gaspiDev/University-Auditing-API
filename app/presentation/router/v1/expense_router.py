from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.application.schemas.expense.expense_for_creation import ExpenseForCreation
from app.application.services.expense_service import ExpenseService
from app.domain.enums.category_enum import CategoryEnum
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user


class ExpenseRouter:
  router = APIRouter(tags=["Expense"], prefix="/expense")

  @router.post("/")
  def create(expense_category: CategoryEnum, expense_for_creation: ExpenseForCreation, user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = ExpenseService(session)
    
    return f"Expense ID: {service.create(expense_category, expense_for_creation, user["id"])} successfully created."
  
  @router.get("/")
  def read(session: Session = Depends(get_db)):
    service = ExpenseService(session)
    return service.read()
  
  @router.put("/")
  def update():
    pass
  
  @router.delete("/")
  def update(expense_id: int, user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = ExpenseService(session)
    return f"Expense ID: {service.delete(expense_id, user["id"])} successfully deleted"
    


  
