import os
from typing import Annotated
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError


oauth2_bearer = OAuth2PasswordBearer(tokenUrl='api/v1/auth/token')
async def current_user(token: Annotated[str, Depends(oauth2_bearer)]):
  load_dotenv()
  try:
    print(token)
    payload = jwt.get_unverified_claims(token)
    dni= payload.get("sub")
    id= payload.get("id")
    if dni is None or id is None:
      raise HTTPException(status_code=401, detail="Could not validate user.")
    return {"dni": dni, "id": id}
  except JWTError:
    raise HTTPException(status_code=401, detail="Couldn't validate user..")