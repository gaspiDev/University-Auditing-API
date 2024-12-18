from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.application.schemas.expense.expense_for_creation import ExpenseForCreation
from app.application.schemas.expense.expense_for_view import ExpenseForView
from app.application.services.expense_service import ExpenseService
from app.domain.enums.category_enum import CategoryEnum
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user


class ExpenseRouter:
  router = APIRouter(tags=["Expense"], prefix="/expense")

  @router.post("/", status_code=201, response_model=dict)
  def create(expense_category: CategoryEnum, expense_for_creation: ExpenseForCreation, user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = ExpenseService(session)
    
    return {"status": 201, "message": f"Expense ID: {service.create(expense_category, expense_for_creation, user["id"])} successfully created."}
  
  @router.get("/", status_code=200, response_model=list[ExpenseForView])
  def read(session: Session = Depends(get_db)):
    service = ExpenseService(session)
    return service.read()
  
  @router.put("/", status_code=200, response_model=dict)
  def update():
    pass
  
  @router.delete("/", status_code=200, response_model=dict)
  def update(expense_id: int, user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = ExpenseService(session)
    return {"status": 200, "message": f"Expense ID: {service.delete(expense_id, user["id"])} successfully deleted"}
    


  
