from fastapi import HTTPException
from sqlmodel import Session

from app.application.schemas.expense.expense_for_creation import ExpenseForCreation
from app.application.schemas.expense.expense_for_view import ExpenseForView
from app.application.services.user_service import UserService
from app.domain.entities.expense import Expense
from app.persistance.repositories.expense_repository import ExpenseRepository
from sqlalchemy.ext.asyncio import AsyncSession


class ExpenseService:
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
  
  def update(self):
    pass
  
  async def delete(self, expense_id: int, dean_id: int) -> int:
    expense = await self.repository.read_by_id(expense_id)
    if expense.university.dean_id != dean_id:
      raise HTTPException(status_code=403,  detail="Forbiden, can't delete expenses of another university.")
    expense_deleted = await self.repository.delete(expense.id)
    return expense_deleted.id
