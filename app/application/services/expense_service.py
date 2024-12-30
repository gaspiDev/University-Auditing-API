from typing import Optional
from fastapi import HTTPException
from sqlmodel import Session
from datetime import datetime
from app.application.schemas.expense.expense_for_creation import ExpenseForCreation
from app.application.schemas.expense.expense_for_update import ExpenseForUpdate
from app.application.schemas.expense.expense_for_view import ExpenseForView
from app.application.services.user_service import UserService
from app.domain.entities.expense import Expense
from app.domain.enums.category_enum import CategoryEnum
from app.persistance.repositories.expense_repository import ExpenseRepository
from sqlalchemy.ext.asyncio import AsyncSession


class ExpenseService:
  # TODO: In all services, the repositories and other services should be passed
  # using dependency injection instead of creating new objects explicitly
  def __init__(self, session: AsyncSession):
    self.repository = ExpenseRepository(session)
    self.user_service = UserService(session)

  async def create(self, expense_category, expense_for_creation: ExpenseForCreation, dean_id: int) -> int:
    dean = await self.user_service.read_by_id(dean_id)
    if not dean.university:
      raise HTTPException(status_code=404, detail="Must be linked with a University.")
    expense = Expense(
      date= expense_for_creation.date,
      amount= expense_for_creation.amount,
      category= expense_category,
      university_id= dean.university.id
    )
    
    expense_created = await self.repository.create(expense)
    return expense_created.id

  async def read(self) -> list[ExpenseForView]:
    expenses = await self.repository.read()
    expenses_for_view = []
    for e in expenses:
      expense_for_view = ExpenseForView(
        id= e.id,
        date= e.date,
        amount= e.amount,
        category= e.category,
        university_id= e.university.id
      )
      expenses_for_view.append(expense_for_view)

    return expenses_for_view
  
  async def read_by_id(self, expense_id: int) -> ExpenseForView:
    expense = await self.repository.read_by_id(expense_id)
    if not expense:
      raise HTTPException(status_code=404, detail=f"Expense ID: {expense_id} doesn't exist.")
    expense_for_view = ExpenseForView(
        id= expense.id,
        date= expense.date,
        amount= expense.amount,
        category= expense.category,
        university_id= expense.university.id
    )

    return expense_for_view
  
  async def update(self, expense_for_update: ExpenseForUpdate, category: Optional[CategoryEnum], user_id: int) -> int:
    expense = await self.repository.read_by_id(expense_for_update.id)
    if not expense:
      raise HTTPException(status_code=404, detail=f"Expense ID: {expense_for_update.id} doesn't exist")
    if category:
      expense.category = category
    if expense_for_update.amount >= 0:
      expense.amount = expense_for_update.amount
    
    expense_updated = await self.repository.create(expense)
    return expense_updated.id

  async def delete(self, expense_id: int, dean_id: int) -> int:
    expense = await self.repository.read_by_id(expense_id)
    if expense.university.dean_id != dean_id:
      raise HTTPException(status_code=403,  detail="Forbiden, can't delete expenses of another university.")
    expense_deleted = await self.repository.delete(expense.id)
    return expense_deleted.id
  
  async def total_expenses_by_id_and_year(self, university_id: int, year: int = None) -> float:
    if year is None:
      year = datetime.now().year
    expenses = await self.repository.total_expenses_by_id_and_year(university_id, year)
    return expenses
  
  async def under_budget(self, university_id: int) -> bool:
    total_expense = await self.total_expenses_by_id_and_year(university_id)
    return is_under_budget
