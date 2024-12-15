from sqlmodel import SQLModel
from .database import engine
from app.domain.entities.user import User
from ...domain.entities.budget import Budget
from ...domain.entities.university import University

def db_startup():
  SQLModel.metadata.create_all(bind=engine, tables=[User.__table__, Budget.__table__, University.__table__])
  

# This script was used a first time to create the db file and it should only be
#  run as a module if the db file is lost or corrupted 
#   ( all data sets will be lost ) 