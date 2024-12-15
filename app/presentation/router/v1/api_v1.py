from fastapi import APIRouter

from app.presentation.router.v1.budget_route import BudgetRouter
from .university_route import UniversityRoute


class ApiRouter:
  router = APIRouter(tags=["All Endpoints"], prefix="/api/v1")

  @router.get("/healthcheck")
  def health_check():
    return "University Auditing API currently: ACTIVE"

  @router.get("/version")
  def version():
    return "v1.0"

  router.include_router(UniversityRoute.router)
  router.include_router(BudgetRouter.router)