from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.application.schemas.university.university_for_creation import UniversityForCreation
from app.application.schemas.university.university_for_update import UniversityForUpdate
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
  async def update(university_for_update: UniversityForUpdate, user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = UniversityService(session)
    updated_university_id = await service.update(university_for_update, user["id"])
    return {"status": 200, "message": f"University ID: {updated_university_id} is updated."}

  @router.delete("/", status_code=200, response_model=dict)
  async def delete(user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = UniversityService(session= session)
    university_deleted_id = await service.delete(user["id"])
    return {"status": 200, "message": f"University ID: {university_deleted_id} successfully deleted."}
  
  @router.get("/{university_id}/total-expense/{year}", status_code=200, response_model=dict)
  async def total_expense_by_year(university_id: int, year: int, session: AsyncSession = Depends(get_db)):
    service = UniversityService(session= session)
    total_expenses = await service.total_expenses_by_year(university_id, year)
    return {"status": 200, "content": total_expenses}
  
  @router.get("/{university_id}/under-budget", status_code=200, response_model=dict)
  async def underbudget(university_id: int, session: AsyncSession = Depends(get_db)):
    service = UniversityService(session= session)
    is_under_budget = await service.under_budget(university_id)
    return {"status": 200, "under_budget": is_under_budget }

