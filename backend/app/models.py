import datetime

from app.database import Base
from sqlalchemy import Integer, String, DateTime, func, UniqueConstraint
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
    
class Category(Base):
    __tablename__="categories"
    
    __table_args__ = (UniqueConstraint('user_id', 'name', name='uq_user_category_name'),)
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    
    #Relationships
    user: Mapped["User"] = relationship("User", back_populates="categories")
    expenses: Mapped[list["Expense"]] = relationship("Expense", back_populates="category")
    budgets: Mapped[list["Budget"]] = relationship("Budget", back_populates="category")
    