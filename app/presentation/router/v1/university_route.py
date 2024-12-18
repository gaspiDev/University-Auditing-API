from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.application.schemas.university.university_for_creation import UniversityForCreation
from app.application.schemas.university.university_for_view import UniversityForView
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user
from ....application.services.university_service import UniversityService


class UniversityRoute:
  router = APIRouter(tags=["University"], prefix="/university",)

  @router.post("/", status_code=200, response_model=str)
  def create(user: Annotated[dict ,Depends(current_user)], university_req: UniversityForCreation, session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    created_id = service.create(university_req, user["id"])
    return f"University ID: {created_id} successfully created."

  @router.get("/", response_model= list[UniversityForView])
  def read(session: Session = Depends(get_db)):
    service = UniversityService(session)
    return service.read()

  @router.get("/{university_id}", response_model= UniversityForView)
  def read_by_id(university_id: int, session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    return service.read_by_id(university_id)

  @router.put("/", response_model= str)
  def update(user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = UniversityService(session)
    pass

  @router.delete("/", response_model= str)
  def delete(user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    return f"University ID: {service.delete(user["id"])} successfully"
