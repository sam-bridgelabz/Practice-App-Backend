from sqlalchemy.orm import Session
from app.models.ans_model import Answer
from app.schemas.ans_schema import AnswerCreate

def create_answer(db: Session, answer: AnswerCreate):
    db_answer = Answer(
        question_id=answer.question_id,
        what_worked_well=answer.analysis_output.what_worked_well,
        what_can_be_improved=answer.analysis_output.what_can_be_improved,
        correctness=answer.quality_feedback.correctness,
        readability=answer.quality_feedback.readability,
        maintainability=answer.quality_feedback.maintainability,
        design=answer.quality_feedback.design,
        scalability=answer.quality_feedback.scalability,
        correctness_score=answer.quality_scores.correctness,
        readability_score=answer.quality_scores.readability,
        maintainability_score=answer.quality_scores.maintainability,
        design_score=answer.quality_scores.design,
        scalability_score=answer.quality_scores.scalability,
        overall_score=answer.quality_scores.overall
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer
