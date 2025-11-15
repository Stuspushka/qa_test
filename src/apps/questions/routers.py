from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session
from src.apps.questions.repository import QuestionRepository
from src.apps.questions.schemas import QuestionCreate, QuestionSummaryRead, QuestionDetailRead
from src.apps.questions.mapper import questions_to_summary_dto, question_to_detail_dto

router = APIRouter()

@router.get("/", response_model=list[QuestionSummaryRead])
async def list_questions(db: AsyncSession = Depends(get_session)):
    repo = QuestionRepository(db)
    questions = await repo.get_all()
    return questions_to_summary_dto(questions)

@router.post("/", response_model=QuestionDetailRead, status_code=201)
async def create_question(q: QuestionCreate, db: AsyncSession = Depends(get_session)):
    repo = QuestionRepository(db)
    question = await repo.create(q)
    return question_to_detail_dto(question)

@router.get("/{question_id}", response_model=QuestionDetailRead)
async def get_question(question_id: int, db: AsyncSession = Depends(get_session)):
    repo = QuestionRepository(db)
    question = await repo.get_by_id(question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question_to_detail_dto(question)

@router.delete("/{question_id}", status_code=204)
async def delete_question(question_id: int, db: AsyncSession = Depends(get_session)):
    repo = QuestionRepository(db)
    deleted = await repo.delete(question_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Question not found")
