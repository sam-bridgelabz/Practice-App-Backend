# app/routers/questions.py
from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse
from decimal import Decimal
from sqlalchemy.orm import Session
from typing import List
from app.schemas.ques_schema import QuestionFiltered
from app.crud import ques_crud
from app.config.database import get_db

question_router = APIRouter(prefix="/questions", tags=["Questions"])


@question_router.get("/get_questions", response_model=List[QuestionFiltered])
def read_questions(
    question_type: str = Query(..., description="Filter by question type"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    try:
        questions = ques_crud.get_questions_by_type(
            db, question_type=question_type, skip=skip, limit=limit
        )

        payload = [
            {
                "id": q.id,
                "stem_md": q.stem_md,
                "solution_md": q.solution_md,
                "score_weight": float(q.score_weight) if isinstance(q.score_weight, Decimal) else q.score_weight
            }
            for q in questions
        ]

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Questions fetched successfully",
                "payload": payload,
                "status": status.HTTP_200_OK
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": f"Error fetching questions: {str(e)}",
                "payload": [],
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR
            }
        )
