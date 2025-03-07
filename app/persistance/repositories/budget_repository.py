from typing import Optional
from fastapi import HTTPException
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.budget import Budget


class BudgetRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, budget: Budget) -> Budget:
        try:
            self.session.add(budget)
            await self.session.commit()
            await self.session.refresh(budget)
            return budget
        except Exception:
            await self.session.rollback()
            raise HTTPException(
                status_code=404, detail="Couldn't save the Budget on db."
            )

    async def read(self) -> list[Budget]:
        statement = select(Budget).where(Budget.isActive == True)
        result = await self.session.execute(statement)
        return result.scalars().all()

    async def read_by_id(self, budget_id: int) -> Optional[Budget]:
        statement = (
            select(Budget).where(Budget.isActive == True).where(Budget.id == budget_id)
        )
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    def update(self) -> Budget:
        pass

    async def delete(self, budget: Budget) -> Budget:
        budget.isActive = False
        self.session.add(budget)
        await self.session.commit()
        await self.session.refresh(budget)
        return budget
