from datetime import datetime, date
from decimal import Decimal

from app.database import Base
from sqlalchemy import Integer, String, DateTime, func, UniqueConstraint, ForeignKey, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

    
class Budget(Base):
    __tablename__="budgets"
    
    __table_args__ = (UniqueConstraint('user_id', 'category_id', 'month','year', name='uq_budget_user_category_period'),)
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=True, index=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(12,2), nullable=False)
    month: Mapped[int] = mapped_column(Integer, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    
    #Relationships
    user: Mapped["User"] = relationship("User", back_populates="budgets")
    category: Mapped["Category | None"] = relationship("Category", back_populates="budgets")