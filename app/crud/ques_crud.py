# app/crud.py
from sqlalchemy.orm import Session
from app.models.ques_model import Question
from typing import List

def get_questions_by_type(
    db: Session, question_type: str, skip: int = 0, limit: int = 10
) -> List[Question]:
    return (
        db.query(
            Question.id,
            Question.stem_md,
            Question.solution_md,
            Question.score_weight,
        )
        .filter(Question.question_type == question_type)
        .offset(skip)
        .limit(limit)
        .all()
    )
