from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import Any, Dict
from app.templates.prompts import REVIEW_PROMPT, REVIEW_PROMPT_THEORY

prompt_router = APIRouter(prefix="/prompts", tags=["Default Prompt"])

class PromptResponse(BaseModel):
    message: str
    payload: Dict[str, Any]
    status: int


@prompt_router.get("/default-prompt", response_model=PromptResponse)
def get_default_prompt(answer_type: str = Query(..., description="Type of question (e.g. 'code' or 'theory')")):
    """
    Return the default system prompt currently configured in the agent
    """
    if answer_type.upper() == "CODE":
        return {
            "message": "Successfully fetched default code check prompt",
            "payload": {"default_code_check_prompt":REVIEW_PROMPT},
            "status": 200
            }
    else:
        return {
            "message": "Successfully fetched default code check prompt",
            "payload": {"default_theory_check_prompt":REVIEW_PROMPT_THEORY},
            "status": 200
            }

