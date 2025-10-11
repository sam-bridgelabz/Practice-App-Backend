from fastapi import APIRouter
from pydantic import BaseModel
from app.templates.prompts import REVIEW_PROMPT



prompt_router = APIRouter(prefix="/prompts", tags=["Default Prompt"])

class PromptResponse(BaseModel):
    default_prompt: str


@prompt_router.get("/default-prompt", response_model=PromptResponse)
def get_default_prompt():
    """
    Return the default system prompt currently configured in the agent
    """
    return {"default_prompt": REVIEW_PROMPT}

