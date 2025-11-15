from pydantic import BaseModel, ConfigDict
from typing import List
from src.apps.answers.schemas import AnswerRead

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    pass

class QuestionSummaryRead(QuestionBase):
    id: int
    created_at: str

    model_config = ConfigDict(from_attributes=True)

class QuestionDetailRead(QuestionBase):
    id: int
    created_at: str
    answers: List[AnswerRead] = []

    model_config = ConfigDict(from_attributes=True)
