from typing import Annotated
from fastapi import Depends
from sqlmodel import Session

from app.persistance.config.database import get_db
from ...persistance.repositories.university_repository import UniversityRepository


class UniversityService:
  def __init__(self, session: Session):
    self.repository = UniversityRepository(session= session)
  
  def read(self):
    return self.repository.read()