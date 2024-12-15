from fastapi import HTTPException
from sqlmodel import Session, select

from app.domain.entities.user import User


class UserRepository:
  def __init__(self, session: Session):
    self.session = session

  def auth(self, dni: int) -> User | None:
    statement = select(User).where(User.isActive == True).where(User.dni == dni)
    result = self.session.exec(statement).first()
    return result
  
  def create(self, user: User) -> User:
    try:
      self.session.add(user)
      self.session.commit()
      self.session.refresh(user)
    except Exception:
      raise HTTPException(status_code=400, detail=f"Couldn't save User {user.dni} in db.")
    return user

  def read(self) -> list[User]:
    statement = select(User).where(User.isActive == True)
    result = self.session.exec(statement)
    return result
  
  def read_by_id(self, user_id: int) -> User:
    statement = select(User).where(User.isActive == True).where(User.id == user_id)
    result = self.session.exec(statement).first()
    return result
  
  def update(self):
    pass

  def delete(self, user: User) -> User:
    user.isActive = False
    self.session.add(user)
    self.session.commit()
    self.session.refresh(user)
    return user