from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.ans_schema import AnswerCreate
from app.crud.ans_crud import create_answer
from app.config.logger import AppLogger

logger = AppLogger.get_logger()
answer_router = APIRouter(prefix="/answers", tags=["Answers"])

@answer_router.post("/insert-answer", status_code=201)
def add_answer(answer: AnswerCreate, db: Session = Depends(get_db)):
    try:
        new_answer = create_answer(db, answer)
        logger.info(f"Answer inserted for question_id={answer.question_id}")
        return {
            "message": "Answer inserted successfully",
            "payload": {
                "answer_id": new_answer.id,
                "question_id": new_answer.question_id
            },
            "status": 201
        }
    except Exception as e:
        logger.exception(f"Error inserting answer: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
