from src.apps.answers.schemas import AnswerRead

def answer_to_dto(answer) -> AnswerRead:
    return AnswerRead.model_validate({
        "id": answer.id,
        "text": answer.text,
        "question_id": answer.question_id,
        "user_id": answer.user_id,
        "created_at": answer.created_at.isoformat()
    }, from_attributes=True)

def answers_to_dto(answers) -> list[AnswerRead]:
    return [answer_to_dto(a) for a in answers]
