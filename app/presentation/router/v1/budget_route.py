


from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.application.schemas.budget.budget_for_creation import BudgetForCreation
from app.application.services.budget_service import BudgetServices
from app.persistance.config.database import get_db


class BudgetRouter:
  router = APIRouter(tags=["Budget"], prefix= "/budget")

  @router.post("/")
  def create(budget_req: BudgetForCreation, session: Session = Depends(get_db)):
    serivce = BudgetServices(session)
    return serivce.create(budget_req)
  
  @router.get("/")
  def read(session: Session = Depends(get_db)):
    service = BudgetServices(session= session)
    return service.read()

  @router.get("/{budget_id}")
  def read(budget_id: int, session: Session = Depends(get_db)):
    service = BudgetServices(session= session)
    return service.read_by_id(budget_id= budget_id)

  @router.put("/")
  def update(session: Session = Depends(get_db)):
    pass

  @router.delete("/")
  def delete(budget_id: int, session: Session = Depends(get_db)):
    service = BudgetServices(session= session)
    return f"Budget ID: {service.delete(budget_id)} successfully deleted"