from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.persistance.config.database import get_db
from ....application.services.university_service import UniversityService


class UniversityRoute:
  router = APIRouter(tags=["University"], prefix="/university",)

  @router.get("/")
  def read(session: Session = Depends(get_db)):
    service = UniversityService(session= session)
    return service.read()
  
  @router.post("/")
  def create():
    pass