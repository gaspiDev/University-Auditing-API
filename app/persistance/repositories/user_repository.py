from typing import Optional
from fastapi import HTTPException
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.domain.entities.user import User


class UserRepository:
  def __init__(self, session: AsyncSession):
    self.session = session

  async def auth(self, dni: int) -> Optional[User]:
    statement = select(User).where(User.isActive == True).where(User.dni == dni)
    result = await self.session.execute(statement)
    return result.scalar_one_or_none()
  
  async def create(self, user: User) -> User:
    try:
      self.session.add(user)
      await self.session.commit()
      await self.session.refresh(user)
      return user
    except Exception:
      await self.session.rollback()
      raise HTTPException(status_code=400, detail=f"Couldn't save User {user.dni} in db.")

  async def read(self) -> list[User]:
    statement = select(User).where(User.isActive == True)
    result = await self.session.execute(statement)
    return result.scalars().all()
  
  async def read_by_id(self, user_id: int) -> Optional[User]:
    statement = (select(User).where(User.isActive == True).where(User.id == user_id).options(selectinload(User.university)))
    result = await self.session.execute(statement)
    return result.scalar_one_or_none()
  
  async def update(self, user: User):
    try:
      self.session.add(user)
      await self.session.commit()
      await self.session.refresh(user)
      return user
    except Exception:
      await self.session.rollback()
      raise HTTPException(status_code=400, detail=f"Couldn't save User {user.dni} in db.")

  async def delete(self, user: User) -> User:
    try: 
      user.isActive = False
      self.session.add(user)
      await self.session.commit()
      await self.session.refresh(user)
      return user
    except Exception:
      await self.session.rollback()
      raise HTTPException(status_code=400, detail=f"Couldn't delete User in db.")