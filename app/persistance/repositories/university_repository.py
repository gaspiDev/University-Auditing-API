from typing import Annotated
from fastapi import HTTPException
from sqlmodel import  select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.university import University

class UniversityRepository:
  def __init__(self, session: AsyncSession):
    self.session = session
  
  async def create(self, university: University) -> University:
    try:
      self.session.add(university)
      await self.session.commit()
      await self.session.refresh(university)
      return university
    except Exception:
      await self.session.rollback()
      raise HTTPException(status_code=404, detail="University already exist: Name, Adress and Contact Email must be unique")
  
  async def read(self) -> list[University]:
    statement = select(University)
    results = await self.session.execute(statement)
    return results.scalars().all()
  
  async def read_by_id(self, university_id: int) -> University:
    statement = select(University).where(University.id == university_id)
    result = await self.session.execute(statement)
    return result.scalar_one_or_none()
  
  def update():
    pass

  async def delete(self, university: University) -> University:
    await self.session.delete(university)
    await self.session.commit()
    return university