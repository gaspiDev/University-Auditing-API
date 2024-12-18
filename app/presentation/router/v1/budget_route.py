


from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.application.schemas.budget.budget_for_creation import BudgetForCreation
from app.application.schemas.budget.budget_for_view import BudgetForView
from app.application.services.budget_service import BudgetServices
from app.persistance.config.database import get_db


class BudgetRouter:
  router = APIRouter(tags=["Budget"], prefix= "/budget")

  @router.post("/", status_code=201, response_model=dict)#party
  def create(budget_req: BudgetForCreation, session: Session = Depends(get_db)):
    serivce = BudgetServices(session)
    return {"status": 201, "message": f"Budget ID: {serivce.create(budget_req)} successfully created."}
  
  @router.get("/", status_code=200, response_model=list[BudgetForView])
  def read(session: Session = Depends(get_db)):
    service = BudgetServices(session= session)
    return service.read()

  @router.get("/{budget_id}", status_code=200, response_model=BudgetForView)
  def read(budget_id: int, session: Session = Depends(get_db)):
    service = BudgetServices(session= session)
    return service.read_by_id(budget_id)

  @router.put("/", status_code=200, response_model=dict)#party
  def update(session: Session = Depends(get_db)):#admin
    pass

  @router.delete("/", status_code=200, response_model=dict)#party
  def delete(budget_id: int, session: Session = Depends(get_db)):
    service = BudgetServices(session= session)
    return {"status": 200, "message": f"Budget ID: {service.delete(budget_id)} successfully deleted"}