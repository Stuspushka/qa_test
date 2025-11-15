from typing import List
from src.apps.questions.models import Question
from src.apps.questions.schemas import QuestionSummaryRead, QuestionDetailRead
from src.apps.answers.schemas import AnswerRead

def question_to_summary_dto(question: Question) -> QuestionSummaryRead:
    data = {
        "id": question.id,
        "text": question.text,
        "created_at": question.created_at.isoformat(),
    }
    return QuestionSummaryRead.model_validate(data)

def questions_to_summary_dto(questions: List[Question]) -> List[QuestionSummaryRead]:
    return [question_to_summary_dto(q) for q in questions]

def question_to_detail_dto(question: Question) -> QuestionDetailRead:
    return QuestionDetailRead.model_validate(
        {
            "id": question.id,
            "text": question.text,
            "created_at": question.created_at.isoformat(),
            "answers": [
                AnswerRead.model_validate(a, from_attributes=True)
                for a in getattr(question, "answers", [])
            ],
        }
    )
