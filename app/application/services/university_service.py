from typing import Annotated
from fastapi import Depends, HTTPException
from sqlmodel import Session

from app.application.schemas.university.university_for_creation import UniversityForCreation
from app.application.schemas.university.university_for_view import UniversityForView
from app.application.services.user_service import UserService
from app.domain.entities.university import University
from app.persistance.config.database import get_db
from ...persistance.repositories.university_repository import UniversityRepository


class UniversityService:
  def __init__(self, session: Session):
    self.repository = UniversityRepository(session= session)
    self.user_service = UserService(session= session)
  
  def create(self, university_input: UniversityForCreation, user_id: int) -> int:
    if self.user_service.read_by_id(user_id).university:
      raise HTTPException(status_code=404, detail="Deans can be linked with only one university")
    if university_input.budget_type.lower() == "public":
      budget_id = 1
    elif university_input.budget_type.lower() == "private":
      budget_id = 2
    else:
      raise HTTPException(status_code=404, detail="Invalid budget type. Must be public or private")
    university = University(
      budget_id= budget_id,
      dean_id= user_id,
      name= university_input.name,
      province= university_input.province,
      city= university_input.city,
      address= university_input.address,
      established= university_input.established,
      contact_email= university_input.contact_email,
    )

    return self.repository.create(university).id
  
  def read(self) -> list[UniversityForView]:
    universities = self.repository.read()
    universities_for_view: list[University] = []
    for u in universities:
      university_for_view = UniversityForView(
        id= u.id,
        budget_id= u.budget_id,
        name= u.name,
        province= u.province,
        city= u.city,
        address= u.address,
        established= u.established,
        contact_email= u.contact_email
      )
      universities_for_view.append(university_for_view)
    return universities_for_view
  
  def read_by_id(self, university_id: int) -> UniversityForView:
    university = self.repository.read_by_id(university_id)
    university_for_view = UniversityForView(
      id= university.id,
      budget_id= university.budget_id,
      name= university.name,
      province= university.province,
      city= university.city,
      address= university.address,
      established= university.established,
      contact_email= university.contact_email 
    )
    return university_for_view
  
  def update():
    pass
  
  def delete(self, user_id: int) -> int:
    university = self.user_service.read_by_id(user_id).university
    return self.repository.delete(university).id
