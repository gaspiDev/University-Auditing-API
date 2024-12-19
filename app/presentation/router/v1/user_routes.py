from typing import Annotated
from fastapi import APIRouter, Depends

from app.application.schemas.user.user_for_creation import UserForCreation
from app.application.schemas.user.user_for_update import UserForUpdate
from app.application.schemas.user.user_for_view import UserForView
from app.application.services.user_service import UserService
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user
from sqlalchemy.ext.asyncio import AsyncSession


class UserRouter:
  router = APIRouter(tags=["User"], prefix="/user")

  @router.post("/", status_code=201, response_model=dict)
  async def create(user_for_creation: UserForCreation, session: AsyncSession = Depends(get_db)):
    service = UserService(session)
    user_id = await service.create(user_for_creation)
    return {"status": 201, "message": f"User ID: {user_id} successfully created."}
  
  @router.get("/", status_code=200, response_model=dict)
  async def read_current(user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = UserService(session)
    current_user = await service.read_by_id(user["id"])
    return {"status": 200, "user": current_user}
  
  @router.put("/", status_code=200, response_model=dict)
  async def update(user_for_update: UserForUpdate, user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = UserService(session)
    updated_user_id = await service.update(user_for_update, user["id"])
    return {"status": 200, "message":f"User ID: {updated_user_id} is updated."}
  
  @router.delete("/", status_code=200, response_model=dict)
  async def delete(user: Annotated[dict ,Depends(current_user)], session: AsyncSession = Depends(get_db)):
    service = UserService(session)
    user_id = await service.delete(user["id"])
    return {"status": 200, "message": f"User ID: {user_id} successfully deleted."}
  