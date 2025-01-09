from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.application.schemas.user.credentials import Token
from app.application.services.user_service import UserService
from app.persistance.config.database import get_db


class AuthRouter:
  router = APIRouter(tags=["auth"], prefix="/auth")

  @router.post("/token", status_code=200, response_model= Token)
  async def auth(credentials: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_db)):
    service = UserService(session)
    user_auth = await service.auth(credentials.username, credentials.password)
    return user_auth