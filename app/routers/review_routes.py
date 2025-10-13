from app.config.logger import AppLogger
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.ans_model import Answer
from app.schemas.ans_schema import AnswerInput
from app.utils.code_utils import review_code_with_gemini
from app.crud.review_crud import store_code_review_to_db
import boto3
import os
import io

logger = AppLogger.get_logger()

review_router = APIRouter(prefix="/reviews", tags=["Reviews Genearation"])

S3_BUCKET = os.getenv("AWS_BUCKET")
s3_client = boto3.client("s3")

def upload_to_s3(payload: AnswerInput) -> str:
    """
    Upload the answer text to S3 and return its URL
    """
    logger.info("Uploading to S3...")

    # folder path
    folder_path = f"answers/{payload.coe_name}/{payload.program_name}/{payload.semester}/{payload.user_id}/{payload.module}"

    file_name = f"{payload.question_id}.txt"
    s3_key = f"{folder_path}/{file_name}"

    file_obj = io.BytesIO(payload.answer_text.encode("utf-8"))

    s3_client.upload_fileobj(file_obj, S3_BUCKET, s3_key)

    logger.info(f"File uploaded to S3: https://{S3_BUCKET}.s3.amazonaws.com/{s3_key}")

    # Public URL
    return f"https://{S3_BUCKET}.s3.amazonaws.com/{s3_key}"


# @review_router.post("/answers/")
# async def create_answer(payload: AnswerInput, db: Session = Depends(get_db)):
#     review_results = None
#     try:
#         file_url = upload_to_s3(payload)

#         logger.info("Storing Answer url in DB...")
#         new_answer = Answer(
#             question_id=payload.question_id,
#             user_id=payload.user_id,
#             file_url=file_url
#         )
#         db.add(new_answer)
#         db.commit()
#         db.refresh(new_answer)
#         logger.info(f"Answer stored in DB with id: {new_answer.id}")

#         try:
#             logger.info("Running code review with code analyser agent...")
#             review_results = await review_code_with_gemini(payload.question_text, payload.answer_text, "Java")
#             logger.info(f"Code Analysing finished with Review results: {review_results}")
#         except ValueError as e:
#             logger.warning(f"Code review failed: {e}")
#             review_results = None

#         store_code_review_to_db(db, new_answer.id, review_results)

#         return {
#             "message": "Answer stored and review generated successfully",
#             "payload": {
#                 "answer_id": new_answer.id,
#                 "file_url": new_answer.file_url,
#                 "review_generated": review_results
#                 },
#             "status": 201
#         }

#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=str(e))


@review_router.post("/answers/")
async def create_answer(payload: AnswerInput, db: Session = Depends(get_db)):
    review_results = None
    try:
        file_url = upload_to_s3(payload)

        logger.info("Storing Answer url in DB...")
        new_answer = Answer(
            question_id=payload.question_id,
            user_id=payload.user_id,
            file_url=file_url
        )
        db.add(new_answer)
        db.commit()
        db.refresh(new_answer)
        logger.info(f"Answer stored in DB with id: {new_answer.id}")

        try:
            logger.info("Running code review with code analyser agent...")
            review_results = await review_code_with_gemini(db, payload.user_id, payload.question_text, payload.answer_text, "Java")
            logger.info(f"Code Analysing finished with Review results: {review_results}")
        except ValueError as e:
            logger.warning(f"Code review failed: {e}")
            review_results = None

        store_code_review_to_db(db, new_answer.id, review_results)

        return {
            "message": "Answer stored and review generated successfully",
            "payload": {
                "answer_id": new_answer.id,
                "file_url": new_answer.file_url,
                "review_generated": review_results
                },
            "status": 201
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
