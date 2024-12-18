from fastapi import HTTPException
from sqlmodel import Session, select

from app.domain.entities.budget import Budget


class BudgetRepository:
  def __init__(self, session: Session):
    self.session = session

  def create(self, budget: Budget) -> Budget:
    try:    
      self.session.add(budget)
      self.session.commit()
      self.session.refresh(budget)
      return budget
    except Exception:
      self.session.rollback()
      raise HTTPException(status_code=404, detail="Couldn't save the Budget on db.")
    
  def read(self) -> list[Budget]:
    statement = select(Budget).where(Budget.isActive == True)
    return self.session.exec(statement).all()
  
  def read_by_id(self, budget_id: int) -> Budget:
    statement = select(Budget).where(Budget.isActive == True).where(Budget.id == budget_id)
    return self.session.exec(statement).first()
  
  def update(self) -> Budget:
    pass

  def delete(self, budget: Budget) -> Budget:
    budget.isActive = False
    self.session.add(budget)
    self.session.commit()
    self.session.refresh(budget)
    return budget