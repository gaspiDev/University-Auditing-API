from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.application.schemas.user.user_for_creation import UserForCreation
from app.application.services.user_service import UserService
from app.persistance.config.database import get_db
from helpers.auth_functions import current_user


class UserRouter:
  router = APIRouter(tags=["User"], prefix="/user")

  @router.post("/")
  def create(user_for_creation: UserForCreation, session: Session = Depends(get_db)):
    service = UserService(session)
    return {"status": 201, "message": f"User ID: {service.create(user_for_creation)} successfully created."}
  
  @router.get("/all")
  def read(session: Session = Depends(get_db)):
    service = UserService(session)
    return service.read()
  
  @router.get("/{user_id}")
  def read_by_id(user_id:int, session: Session = Depends(get_db)):
    service = UserService(session)
    return service.read_by_id(user_id)
  
  @router.put("/")
  def update(session: Session = Depends(get_db)):
    pass

  @router.delete("/{user_id}")
  def delete(user_id: int, session: Session = Depends(get_db)):
    service = UserService(session)
    return {"status": 200, "message": f"User ID: {service.delete(user_id)} successfully deleted."}
  
  @router.get("/")
  async def read_current(user: Annotated[dict ,Depends(current_user)], session: Session = Depends(get_db)):
    if user is None:
      raise HTTPException(status_code=401, detail="Authentication Failed")
    return {"User": user}