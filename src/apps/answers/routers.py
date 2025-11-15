# src/apps/answers/routers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session
from src.apps.answers.repository import AnswerRepository
from src.apps.answers.schemas import AnswerCreate, AnswerRead
from src.apps.answers.mapper import answer_to_dto, answers_to_dto
from src.apps.questions.repository import QuestionRepository

router = APIRouter()

@router.get("/question/{question_id}", response_model=list[AnswerRead])
async def list_answers(question_id: int, db: AsyncSession = Depends(get_session)):
    repo = AnswerRepository(db)
    answers = await repo.get_all_by_question(question_id)
    return answers_to_dto(answers)

@router.post("/questions/{question_id}/answers/", response_model=AnswerRead, status_code=201)
async def create_answer(
    question_id: int,
    answer: AnswerCreate,
    db: AsyncSession = Depends(get_session)
):
    question_repo = QuestionRepository(db)
    question = await question_repo.get_by_id(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    repo = AnswerRepository(db)
    new_answer = await repo.create(answer, question_id)
    return answer_to_dto(new_answer)

@router.get("/{answer_id}", response_model=AnswerRead)
async def get_answer(answer_id: int, db: AsyncSession = Depends(get_session)):
    repo = AnswerRepository(db)
    answer = await repo.get_by_id(answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer_to_dto(answer)

@router.delete("/{answer_id}", status_code=204)
async def delete_answer(answer_id: int, db: AsyncSession = Depends(get_session)):
    repo = AnswerRepository(db)
    deleted = await repo.delete(answer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Answer not found")
