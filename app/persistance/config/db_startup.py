from sqlmodel import SQLModel
from .database import engine
from ...domain.entities.university import University


SQLModel.metadata.create_all(engine)

# This script was used a first time to create the db file and it should only be
#  run as a module if the db file is lost or corrupted 
#   ( all data sets will be lost ) 