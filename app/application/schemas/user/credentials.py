from pydantic import BaseModel


class Credentials(BaseModel):
  dni: int
  password: str

class Token(BaseModel):
  access_token: str
  token_type: str