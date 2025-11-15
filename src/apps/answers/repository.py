from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from src.apps.answers.models import Answer
from src.apps.answers.schemas import AnswerCreate

class AnswerRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_by_question(self, question_id: int) -> list[Answer]:
        result = await self.db.execute(
            select(Answer)
            .where(Answer.question_id == question_id)
            .options(selectinload(Answer.question))
        )
        return result.scalars().all()

    async def get_by_id(self, answer_id: int) -> Answer | None:
        result = await self.db.execute(
            select(Answer).where(Answer.id == answer_id)
        )
        return result.scalar_one_or_none()

    async def create(self, answer: AnswerCreate, question_id: int) -> Answer:
        new_answer = Answer(
            text=answer.text,
            user_id=answer.user_id,
            question_id=question_id
        )
        self.db.add(new_answer)
        await self.db.commit()
        await self.db.refresh(new_answer)
        return new_answer

    async def delete(self, answer_id: int) -> bool:
        answer = await self.get_by_id(answer_id)
        if not answer:
            return False
        await self.db.delete(answer)
        await self.db.commit()
        return True
