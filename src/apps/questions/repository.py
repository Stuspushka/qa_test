from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.apps.questions.models import Question
from src.apps.questions.schemas import QuestionCreate

class QuestionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[Question]:
        result = await self.db.execute(
            select(Question).options(selectinload(Question.answers))
        )
        return result.scalars().all()

    async def get_by_id(self, question_id: int) -> Question | None:
        result = await self.db.execute(
            select(Question)
            .where(Question.id == question_id)
            .options(selectinload(Question.answers))
        )
        return result.scalar_one_or_none()

    async def create(self, q: QuestionCreate) -> Question:
        question = Question(text=q.text)
        self.db.add(question)
        await self.db.commit()
        await self.db.refresh(question)
        return question

    async def delete(self, question_id: int) -> bool:
        question = await self.get_by_id(question_id)
        if not question:
            return False
        await self.db.delete(question)
        await self.db.commit()
        return True
