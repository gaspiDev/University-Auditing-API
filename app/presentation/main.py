from fastapi import FastAPI
from .router.api import ApiRouter
from ..persistance.config.db_startup import db_startup


db_startup()
app = FastAPI(title="University Auditing API")
app.include_router(ApiRouter.router)