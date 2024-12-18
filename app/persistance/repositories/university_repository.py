from typing import Annotated
from fastapi import HTTPException
from sqlmodel import Session, select

from app.domain.entities.university import University

class UniversityRepository:
  def __init__(self, session: Session):
    self.session = session
  
  def create(self, university: University) -> University:
    try:
      self.session.add(university)
      self.session.commit()
      self.session.refresh(university)
      return university
    except Exception:
      self.session.rollback()
      raise HTTPException(status_code=404, detail="University already exist: Name, Adress and Contact Email must be unique")
  
  def read(self) -> list[University]:
    statement = select(University).where(University.isActive == True)
    results = self.session.exec(statement).all()
    return results
  
  def read_by_id(self, university_id: int) -> University:
    statement = select(University).where(University.id == university_id)
    result = self.session.exec(statement).first()
    if not result:
      raise HTTPException(status_code=404, detail=f"Id {university_id} doesn't exist.")
    return result
  
  def update():
    pass

  def delete(self, university: University) -> University:
    university.isActive = False
    self.session.add(university)
    self.session.commit()
    self.session.refresh(university)
    return university