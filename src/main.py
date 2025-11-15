from fastapi import FastAPI
from .settings import settings
from .apps.questions.routers import router as questions_router
from .apps.answers.routers import router as answers_router

app = FastAPI(title=settings.APP_TITLE)

app.include_router(questions_router, prefix="/questions", tags=["questions"])
app.include_router(answers_router, prefix="/answers", tags=["answers"])