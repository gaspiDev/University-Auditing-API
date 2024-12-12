from sqlmodel import SQLModel, Field

class University(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    location: str