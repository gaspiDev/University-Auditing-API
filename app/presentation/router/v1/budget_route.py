from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.application.schemas.budget.budget_for_creation import BudgetForCreation
from app.application.schemas.budget.budget_for_view import BudgetForView
from app.application.services.budget_service import BudgetServices
from app.persistance.config.database import get_db


class BudgetRouter:
  router = APIRouter(tags=["Budget"], prefix= "/budget")

  @router.post("/", status_code=201, response_model=dict)
  async def create(budget_for_creation: BudgetForCreation, session: AsyncSession = Depends(get_db)):
    serivce = BudgetServices(session)
    budget_created_id = await serivce.create(budget_for_creation)
    return {"status": 201, "message": f"Budget ID: {budget_created_id} successfully created."}
  
  @router.get("/", status_code=200, response_model=dict)
  async def read(session: AsyncSession = Depends(get_db)):
    service = BudgetServices(session= session)
    budgets = await service.read()
    return {"status": 200, "budgets": budgets}

  @router.get("/{budget_id}", status_code=200, response_model=dict)
  async def read(budget_id: int, session: AsyncSession = Depends(get_db)):
    service = BudgetServices(session= session)
    budget = await service.read_by_id(budget_id)
    return {"status": 200, "budget": budget}
  
  @router.put("/", status_code=200, response_model=dict)
  async def update(session: AsyncSession = Depends(get_db)):
    service = BudgetServices(session= session)
    pass

  @router.delete("/", status_code=200, response_model=dict)
  async def delete(budget_id: int, session: AsyncSession = Depends(get_db)):
    service = BudgetServices(session= session)
    budget_deleted_id = await service.delete(budget_id)
    return {"status": 200, "message": f"Budget ID: {budget_deleted_id} successfully deleted"}