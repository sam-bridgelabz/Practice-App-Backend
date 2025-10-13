# app/crud.py
from sqlalchemy.orm import Session
from app.models.ques_model import Question
from typing import List

def get_questions_by_ans_type(
    db: Session, answer_type: str, skip: int = 0, limit: int = 10
) -> List[Question]:
    return (
        db.query(
            Question.id,
            Question.question_type,
            Question.answer_type,
            Question.stem_md,
            Question.solution_md,
            Question.score_weight,
        )
        .filter(Question.answer_type == answer_type)
        .offset(skip)
        .limit(limit)
        .all()
    )
