from app.config.logger import AppLogger
from sqlalchemy.orm import Session
from app.models.review_model import Review
import uuid
import json

logger = AppLogger.get_logger()

def store_code_review_to_db(db: Session, answer_id: str, review_data: dict,
                            reviewer: str = "Code Analyser Gent"):
    """
    Stores code review JSON into the Review table including all quantitative fields.
    """
    try:
        review_summary = json.dumps(review_data.get("Code_Analysis", {}))
        review_points = json.dumps(review_data.get("Code_Quality_Qualitative", {}))

        quantitative = review_data.get("Code_Quality_Quantitative", {})
        new_review = Review(
            id=str(uuid.uuid4()),
            answer_id=answer_id,
            reviewer=reviewer,
            review_summary=review_summary,
            review_points=review_points,
            score_correctness=quantitative.get("Correctness"),
            score_readability=quantitative.get("Readability"),
            score_maintainability=quantitative.get("Maintainability"),
            score_design=quantitative.get("Design"),
            score_scalability=quantitative.get("Scalability"),
            score_overall=quantitative.get("Overall")
        )

        db.add(new_review)
        db.commit()
        db.refresh(new_review)
        return new_review

    except Exception as e:
        db.rollback()
        raise e
