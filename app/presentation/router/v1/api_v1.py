from fastapi import APIRouter

from app.presentation.router.v1.auth_router import AuthRouter
from app.presentation.router.v1.budget_route import BudgetRouter
from app.presentation.router.v1.expense_router import ExpenseRouter
from app.presentation.router.v1.user_routes import UserRouter
from .university_route import UniversityRoute


class ApiRouter:
    router = APIRouter(tags=["All Endpoints"], prefix="/api/v1")

    @router.get("/healthcheck")
    async def health_check():
        return "University Auditing API currently: ACTIVE"

    @router.get("/version")
    async def version():
        return "v1.0"

    router.include_router(AuthRouter.router)
    router.include_router(UserRouter.router)
    router.include_router(UniversityRoute.router)
    router.include_router(ExpenseRouter.router)
    router.include_router(BudgetRouter.router)
