from typing import Annotated, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.schemas.expense.expense_for_creation import ExpenseForCreation
from app.application.schemas.expense.expense_for_update import ExpenseForUpdate
from app.application.services.expense_service import ExpenseService
from app.domain.enums.category_enum import CategoryEnum
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user


class ExpenseRouter:
  router = APIRouter(tags=["Expense"], prefix="/expense")

  @router.post("/", status_code=201, response_model=dict)
  async def create(expense_category: CategoryEnum, expense_for_creation: ExpenseForCreation, user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = ExpenseService(session)
    expense_created_id = await service.create(expense_category, expense_for_creation, user["id"])
    return {"status": 201, "message": f"Expense ID: {expense_created_id} successfully created."}
  
  @router.get("/", status_code=200, response_model=dict)
  async def read(session: AsyncSession = Depends(get_db)):
    service = ExpenseService(session)
    expense = await service.read()
    return {"status": 200, "expenses": expense}
  
  @router.get("/{expense_id}", status_code=200, response_model=dict)
  async def read_by_id(expense_id: int, session: AsyncSession = Depends(get_db)):
    service = ExpenseService(session)
    expense = await service.read_by_id(expense_id)
    return {"status": 200, "expense": expense}
    
  @router.put("/", status_code=200, response_model=dict)
  async def update(category: Optional[CategoryEnum], expense_for_update: ExpenseForUpdate, user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = ExpenseService(session)
    expense_updated_id = await service.update(expense_for_update, category, user["id"])
    
    return {"status": 200 , "message":f"Expense ID: {expense_updated_id} is updated"}

  
  @router.delete("/", status_code=200, response_model=dict)
  async def update(expense_id: int, user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = ExpenseService(session)
    expense_deleted = await service.delete(expense_id, user["id"])
    return {"status": 200, "message": f"Expense ID: {expense_deleted} successfully deleted"}
  