from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.application.schemas.user.user_for_creation import UserForCreation
from app.application.services.user_service import UserService
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user


class UserRouter:
  router = APIRouter(tags=["User"], prefix="/user")

  @router.post("/", status_code=201, response_model=dict)
  def create(user_for_creation: UserForCreation, session: Session = Depends(get_db)):
    service = UserService(session)
    return {"status": 201, "message": f"User ID: {service.create(user_for_creation)} successfully created."}
  
  @router.get("/", status_code=200)
  async def read_current(user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = UserService(session)
    return service.read_by_id(user["id"])
  
  @router.put("/", status_code=200)
  def update(user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    pass

  @router.delete("/", status_code=200)
  def delete(user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    service = UserService(session)
    return {"status": 200, "message": f"User ID: {service.delete(user["id"])} successfully deleted."}
  