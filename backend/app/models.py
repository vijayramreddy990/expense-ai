import datetime

from app.database import Base
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__="users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    #Relationships
    expenses: Mapped[list["Expense"]] = relationship("Expense", back_populates="user")
    categories: Mapped[list["Category"]] = relationship("Category", back_populates="user")
    budgets: Mapped[list["Budget"]] = relationship("Budget", back_populates="user")