from typing import Annotated
from sqlmodel import Session, select

from app.domain.entities.university import University

class UniversityRepository:
  def __init__(self, session: Session):
    self.session = session
  def read(self):
    statement = select(University)
    results = self.session.exec(statement).all()
    return results
  #instead of returning a str i want to have accses to my db