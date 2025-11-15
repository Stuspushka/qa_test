from pydantic import BaseModel, ConfigDict,  Field

class AnswerBase(BaseModel):
    text: str

class AnswerCreate(BaseModel):
    text: str = Field(..., min_length=1)
    user_id: str

class AnswerRead(AnswerBase):
    id: int
    question_id: int
    user_id: str
    created_at: str

    model_config = ConfigDict(from_attributes=True)
