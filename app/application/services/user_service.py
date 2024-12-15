from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlmodel import Session
from dotenv import load_dotenv
import os
from app.application.schemas.user.credentials import Credentials
from app.application.schemas.user.user_for_creation import UserForCreation
from app.application.schemas.user.user_for_view import UserForView
from app.domain.entities.user import User
from app.persistance.repositories.user_repository import UserRepository
from passlib.context import CryptContext


class UserService:
  def __init__(self, session: Session):
    self.repository = UserRepository(session)
    self.bcrypt_context = CryptContext(schemes=["bcrypt"])
    load_dotenv()
  
  def auth(self, dni, password):
    user: User = self.repository.auth(dni)
    
    if not user:
      raise HTTPException(status_code=401, detail="Unauthorized, dni or password are incorrect.")
    if not self.bcrypt_context.verify(password, user.password):
      raise HTTPException(status_code=401, detail="Unauthorized, dni or password are incorrect.")
    
    encode = {"sub": user.dni, "id": user.id}
    expires = datetime.now() + timedelta(minutes=20)
    encode.update({"exp": expires})

    token = jwt.encode(encode, os.getenv("SECRET_KEY"), algorithm= os.getenv("HASH_ALGORITHM"))
    
    return {"access_token": token, "token_type": "bearer"}
    
  def create(self, user_for_creation: UserForCreation) -> int:
    hashed_password = self.bcrypt_context.hash(user_for_creation.password)
    user = User(
      dni= user_for_creation.dni,
      password= hashed_password,
      name = user_for_creation.name,
      lastname= user_for_creation.lastname,
      isDean= user_for_creation.isDean,
    )
    return self.repository.create(user).id
  
  def read(self) -> list[UserForView]:
    users: list[User] = self.repository.read()
    users_for_view: list[UserForView] = []
    for u in users:
      user_for_view = UserForView(
        id= u.id,
        name= u.name,
        lastname= u.lastname,
        dni= u.dni,
        isDean= u.isDean
      )
      users_for_view.append(user_for_view)
    return users_for_view
  
  def read_by_id(self, user_id: int) -> User:
    user = self.repository.read_by_id(user_id)
    if not user:
      raise HTTPException(status_code=404, detail=f"User ID: {user_id} doesn't exists.")
    user_for_view = UserForView(
        id= user.id,
        name= user.name,
        lastname= user.lastname,
        dni= user.dni,
        isDean= user.isDean
      )
    return user_for_view
  
  def update(self):
    pass

  def delete(self, user_id: int) -> int:
    user = self.repository.read_by_id(user_id)
    return self.repository.delete(user).id