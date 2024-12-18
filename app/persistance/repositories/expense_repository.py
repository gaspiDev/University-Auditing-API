from fastapi import HTTPException
from sqlmodel import Session, select

from app.domain.entities.expense import Expense


class ExpenseRepository:
  def __init__(self, session: Session):
    self.session = session

  def create(self, expense: Expense) -> Expense:
    try:
      print(expense)
      self.session.add(expense)
      self.session.commit()
      self.session.refresh(expense)
    except Exception:
      raise HTTPException(status_code=404, detail="Couldn't save expense on db")
    
    return expense

  def read(self) -> list[Expense]:
    statement = select(Expense).where(Expense.isActive == True)
    return self.session.exec(statement).all()

  def read_by_id(self, expense_id: int) -> Expense:
    statement = select(Expense).where(Expense.isActive == True).where(Expense.id == expense_id)
    return self.session.exec(statement).first()

  def update(self):
    pass

  def delete(self, expense_id: int) -> Expense:
    expense = self.read_by_id(expense_id)
    expense.isActive = False
    self.session.add(expense)
    self.session.commit()
    self.session.refresh(expense)
    return expense