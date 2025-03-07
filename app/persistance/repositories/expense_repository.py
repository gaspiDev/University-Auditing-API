from typing import Optional
from fastapi import HTTPException
from sqlalchemy import func
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.expense import Expense
from sqlalchemy.orm import selectinload


class ExpenseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, expense: Expense) -> Expense:
        try:
            self.session.add(expense)
            await self.session.commit()
            await self.session.refresh(expense)
            return expense
        except Exception:
            await self.session.rollback()
            raise HTTPException(status_code=404, detail="Couldn't save expense on db")

    async def read(self) -> list[Expense]:
        statement = (
            select(Expense)
            .where(Expense.isActive == True)
            .options(selectinload(Expense.university))
        )
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def read_by_id(self, expense_id: int) -> Optional[Expense]:
        statement = (
            select(Expense)
            .where(Expense.isActive == True)
            .where(Expense.id == expense_id)
            .options(selectinload(Expense.university))
        )
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    def update(self):
        pass

    async def delete(self, expense_id: int) -> Expense:
        expense = await self.read_by_id(expense_id)
        expense.isActive = False
        self.session.add(expense)
        await self.session.commit()
        await self.session.refresh(expense)
        return expense

    async def total_expenses_by_id_and_year(self, university_id, year: int) -> float:
        statement = (
            select(func.sum(Expense.amount))
            .where(Expense.university_id == university_id)
            .where(func.extract("year", Expense.date) == year)
        )
        result = await self.session.execute(statement)

        return result.scalar_one_or_none() or 0.0
