from fastapi import HTTPException
from sqlmodel import Session

from app.application.schemas.budget.budget_for_creation import BudgetForCreation
from app.application.schemas.budget.budget_for_view import BudgetForView
from app.domain.entities.budget import Budget
from app.persistance.repositories.budget_repository import BudgetRepository


class BudgetServices:
  def __init__(self, session: Session):
    self.repository = BudgetRepository(session)
  
  def create(self, budget_for_creation: BudgetForCreation):
    budgets = self.read()
    for b in budgets:
      if (b.type == budget_for_creation.type) and (b.year == budget_for_creation.year) and (b.approved_by == budget_for_creation.approved_by):
        raise HTTPException(status_code=400, detail="A party can approve only one budget per year and type")
      
    budget = Budget(
      type= budget_for_creation.type,
      year= budget_for_creation.year,
      total_budget= budget_for_creation.total_budget,
      approved_by= budget_for_creation.approved_by
    )
    return self.repository.create(budget= budget)
  
  def read(self) -> list[BudgetForView]:
    budgets = self.repository.read()
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
  
  def read_by_id(self, budget_id: int):
    budget = self.repository.read_by_id(budget_id)
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
  
  def update(self):
    pass

  def delete(self, budget_id: int):
    budget = self.repository.read_by_id(budget_id)
    return self.repository.delete(budget).id
    