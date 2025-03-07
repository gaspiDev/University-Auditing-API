from sqlalchemy import create_engine
from sqlmodel import SQLModel
from app.domain.entities.user import User
from app.domain.entities.budget import Budget
from app.domain.entities.university import University
from app.domain.entities.expense import Expense


def db_startup():
    SYNC_DATABASE_URL = "sqlite:///./ua_dataset.db"
    sync_engine = create_engine(SYNC_DATABASE_URL)
    SQLModel.metadata.create_all(
        bind=sync_engine,
        tables=[
            User.__table__,
            Budget.__table__,
            University.__table__,
            Expense.__table__,
        ],
    )


# This script was used a first time to create the db file and it should only be
#  run as a module if the db file is lost or corrupted
#   ( all data sets will be lost )
