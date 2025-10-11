import asyncio
import sys

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


from app.config.logger import AppLogger
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.exceptions import ResponseValidationError
from contextlib import asynccontextmanager
from app.config.database import Base, engine
from app.routers.ques_router import question_router
from app.models import ques_model
from app.models import review_model
from app.routers.ans_route import answer_router
from app.routers.review_routes import review_router
from app.utils.s3_utils import create_s3_folders
from app.routers.prompt_route import prompt_router
from app.config.agent_initialization import gemini_model
from app.routers.java_routes import java_router

logger = AppLogger.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Practice App starting...")
        Base.metadata.create_all(bind=engine)

        # if gemini_agent is not None:
        #     analyser_agent_response = await gemini_agent.run("Hi Code Analyser Agent")
        #     logger.info(f"Code Analyser agent initialized --> {analyser_agent_response.output}")

        FOLDER_LIST = ["answers/", "logs/"]
        logger.info("Tables created successfully.")
        create_s3_folders(os.getenv("AWS_BUCKET"), FOLDER_LIST)
        logger.info("Folders created in S3 bucket successfully.")

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
            "validation_errors": exc.errors(),
        },
    )

@app.get("/test", response_class=HTMLResponse)
async def serve_test_page():
    """Serves the WebSocket test HTML file"""
    file_path = os.path.join(os.path.dirname(__file__), "templates", "test.html")
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

app.include_router(question_router)
app.include_router(answer_router)
app.include_router(review_router)
app.include_router(prompt_router)
app.include_router(java_router)

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

