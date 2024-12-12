from fastapi import FastAPI
from .router.api import ApiRouter


app = FastAPI(title="University Auditing API")

app.include_router(ApiRouter.router)
