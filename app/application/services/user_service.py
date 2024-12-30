from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os


# TODO: the following imports should all be:
# from app.application.schemas import (
#   Credentials,
#   UserForCreation,
#   UserForUpdate,
#   UserForView,
# )
from app.application.schemas.user.credentials import Credentials
from app.application.schemas.user.user_for_creation import UserForCreation
from app.application.schemas.user.user_for_update import UserForUpdate
from app.application.schemas.user.user_for_view import UserForView


from app.domain.entities.user import User
from app.persistance.repositories.user_repository import UserRepository
from passlib.context import CryptContext

# TODO: Services should not know about the persitence details, this leaks the 
# abstraction from the data layer to the service layer
from sqlalchemy.ext.asyncio import AsyncSession



class UserService:
  def __init__(self, session: AsyncSession):
    self.repository = UserRepository(session)

    # TODO: the encryption of the password should be separated in a separate
    # service (e.g. AuthenticationService) to abstract implementation details
    self.bcrypt_context = CryptContext(schemes=["bcrypt"])

    # TODO: load_dotenv should be done only once in the lifecycle of the app
    load_dotenv()
  
  async def auth(self, dni, password) -> dict:
    user: User = await self.repository.auth(dni)
    

    # TODO: Services should not raise exceptions that are from other layers
    # HTTPException is an error from the route/application layer, errors in the
    # service layer should be either built-in (e.g. ValueError) or custom errors
    # defined in this layer (e.g. InvalidUserInputError)
    if not user:
      raise HTTPException(status_code=401, detail="Unauthorized, dni or password are incorrect.")
    if not self.bcrypt_context.verify(password, user.password):
      raise HTTPException(status_code=401, detail="Unauthorized, dni or password are incorrect.")
    
    encode = {"sub": user.dni, "id": user.id}
    expires = datetime.now() + timedelta(minutes=20)
    encode.update({"exp": expires})

    token = jwt.encode(encode, os.getenv("SECRET_KEY"), algorithm= os.getenv("HASH_ALGORITHM"))
    
    return {"access_token": token, "token_type": "bearer"}
    
  async def create(self, user_for_creation: UserForCreation) -> int:
    hashed_password = self.bcrypt_context.hash(user_for_creation.password)
    user = User(
      dni= user_for_creation.dni,
      password= hashed_password,
      name = user_for_creation.name,
      lastname= user_for_creation.lastname,
    )
    user_created = await self.repository.create(user)
    return user_created.id
  
  async def read_by_id(self, user_id: int) -> UserForView:
    user = await self.repository.read_by_id(user_id)
    if not user:
      raise HTTPException(status_code=404, detail=f"User ID: {user_id} doesn't exists.")

    # TODO: Mapping to a new class should not happen in this layer
    user_for_view = UserForView(
        id= user.id,
        name= user.name,
        lastname= user.lastname,
        dni= user.dni,
        university= user.university
      )
    return user_for_view
  
  # TODO: Missing return value
  async def update(self, user_for_update: UserForUpdate, user_id: int):
    # TODO: This could be simplify by using model_copy with update
    # https://docs.pydantic.dev/latest/concepts/serialization/#model_copy
    user = await self.repository.read_by_id(user_id)
    if user_for_update.name:
      user.name = user_for_update.name
    if user_for_update.lastname:
      user.lastname = user_for_update.lastname
    user_updated = await self.repository.create(user)

  async def delete(self, user_id: int) -> int:
    user = await self.repository.read_by_id(user_id)
    print(user.id)
    user_deleted = await self.repository.delete(user)
    return user_deleted.id