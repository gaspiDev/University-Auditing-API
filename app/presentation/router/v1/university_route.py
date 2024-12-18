from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.schemas.university.university_for_creation import UniversityForCreation
from app.application.schemas.university.university_for_view import UniversityForView
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user
from ....application.services.university_service import UniversityService


class UniversityRoute:
  router = APIRouter(tags=["University"], prefix="/university",)

  @router.post("/", status_code=201, response_model=dict)
  async def create(user: Annotated[dict ,Depends(current_user)], university_for_creation: UniversityForCreation, session: AsyncSession = Depends(get_db)):
    service = UniversityService(session= session)
    university_id = await service.create(university_for_creation, user["id"])
    return {"status": 201, "message":f"University ID: {university_id} successfully created."}

  @router.get("/", status_code=200, response_model= dict)
  async def read(session: AsyncSession = Depends(get_db)):
    service = UniversityService(session)
    universities = await service.read()
    return {"status": 200, "universities": universities}

  @router.get("/{university_id}", status_code=200, response_model= dict)
  async def read_by_id(university_id: int, session: AsyncSession = Depends(get_db)):
    service = UniversityService(session= session)
    university = await service.read_by_id(university_id)
    return {"status": 200, "university": university}
  
  @router.put("/", status_code=200, response_model=dict)
  async def update(user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = UniversityService(session)
    pass

  @router.delete("/", status_code=200, response_model=dict)
  async def delete(user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = UniversityService(session= session)
    university_deleted_id = await service.delete(user["id"])
    return {"status": 200, "message": f"University ID: {university_deleted_id} successfully deleted."}
