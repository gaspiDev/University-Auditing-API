from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.application.schemas.university.university_for_creation import UniversityForCreation
from app.application.schemas.university.university_for_view import UniversityForView
from app.persistance.config.database import get_db
from ....application.services.university_service import UniversityService


class UniversityRoute:
  router = APIRouter(tags=["University"], prefix="/university",)

  @router.post("/", response_model=str)
  def create(university_req: UniversityForCreation, session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    created_id = service.create(university_input= university_req)
    return f"University ID: {created_id} successfully created."

  @router.get("/", response_model= list[UniversityForView])
  def read(session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    return service.read()

  @router.get("/{university_id}", response_model= UniversityForView)
  def read_by_id(university_id: int, session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    return service.read_by_id(university_id= university_id)

  @router.put("/", response_model= str)
  def update(session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    pass

  @router.delete("/{university_id}", response_model= str)
  def delete(university_id: int, session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    return f"University ID: {service.delete(university_id)} successfully"
