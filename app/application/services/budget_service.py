from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.schemas.budget.budget_for_creation import BudgetForCreation
from app.application.schemas.budget.budget_for_update import BudgetForUpdate
from app.application.schemas.budget.budget_for_view import BudgetForView
from app.domain.entities.budget import Budget
from app.persistance.repositories.budget_repository import BudgetRepository


# TODO: Services could be easily transform to dataclasses
class BudgetServices:
  def __init__(self, session: AsyncSession):
    self.repository = BudgetRepository(session)
  
  async def create(self, budget_for_creation: BudgetForCreation) -> int:
    budgets = await self.read()
    for b in budgets:
      if (b.type == budget_for_creation.type) and (b.year == budget_for_creation.year) and (b.approved_by == budget_for_creation.approved_by):
        raise HTTPException(status_code=400, detail="A party can approve only one budget per year and type")
      
    budget = Budget(
      type= budget_for_creation.type,
      year= budget_for_creation.year,
      total_budget= budget_for_creation.total_budget,
      approved_by= budget_for_creation.approved_by
    )
    budget_created = await self.repository.create(budget)
    return budget_created.id
  
  async def read(self) -> list[BudgetForView]:
    budgets = await self.repository.read()
    budgets_for_view: list[BudgetForView] = []
    for b in budgets:
      budget_for_view = BudgetForView(
        id= b.id,
        type= b.type,
        year= b.year,
        total_budget= b.total_budget,
        approved_by= b.approved_by
      )
      budgets_for_view.append(budget_for_view)
    return budgets_for_view
  
  async def read_by_id(self, budget_id: int) -> BudgetForView:
    budget = await self.repository.read_by_id(budget_id)
    if not budget:
      raise HTTPException(status_code=404, detail=f"Budget ID {budget_id} doesn't exists.")
    budget_for_view = BudgetForView(
        id= budget.id,
        type= budget.type,
        year= budget.year,
        total_budget= budget.total_budget,
        approved_by= budget.approved_by
      )
    return budget_for_view
  
  async def update(self, budget_for_update: BudgetForUpdate) -> int:
    budget = await self.repository.read_by_id(budget_for_update.id)
    if not budget:
      raise HTTPException(status_code=404, detail=f"Budget ID: {budget_for_update.id} doesn't exist")
    
    budget.total_budget = budget_for_update.total_budget
    if budget_for_update.approved_by:
      budget.approved_by = budget_for_update.approved_by

    budget_updated = await self.repository.create(budget)

    return budget_updated.id
  
  async def delete(self, budget_id: int) -> int:
    budget = await self.repository.read_by_id(budget_id)
    if not budget:
      raise HTTPException(status_code=404, detail=f"Budget ID: {budget_id} doesn't exist.")
    budget_deleted = await self.repository.delete(budget)
    return budget_deleted.id
    