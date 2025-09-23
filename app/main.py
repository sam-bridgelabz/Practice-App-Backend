from app.config.logger import AppLogger
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import ResponseValidationError
from contextlib import asynccontextmanager
from app.config.database import Base, engine
from app.routers.ques_router import question_router
from app.models import ques_model

logger = AppLogger.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Practice App starting...")
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully.")
    except Exception as e:
        logger.exception(f"Error creating tables: {e}")

    yield

    logger.info("Practice App shutting down...")

app = FastAPI(
    title="Practice App",
    lifespan=lifespan
    )

@app.exception_handler(ResponseValidationError)
async def response_validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=500,
        content={
            "success_status": False,
            "error_details": "Response model validation failed",
            "validation_errors": exc.errors(),   # detailed error info
        },
    )

app.include_router(question_router)

if __name__ == "__main__":
    import logging
    import uvicorn
    # Disable Uvicorn's default handlers
    logging.getLogger("uvicorn").handlers.clear()
    logging.getLogger("uvicorn.access").handlers.clear()
    logging.getLogger("uvicorn.error").handlers.clear()

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_config=None
    )

