from typing import List
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db_async import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.enrollments import Enrollment


class Course(Base):

    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    capacity: Mapped[int] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    
    
    enrollments: Mapped[List["Enrollment"]] = relationship(back_populates="course",cascade="all, delete-orphan")