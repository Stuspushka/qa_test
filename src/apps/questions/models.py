from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base
from src.apps.common.models import TimestampMixin
from src.apps.answers.models import Answer

class Question(Base, TimestampMixin):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)


    answers: Mapped[list["Answer"]] = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
