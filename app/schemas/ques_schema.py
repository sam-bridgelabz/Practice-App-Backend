from pydantic import BaseModel
from typing import Optional
from enum import Enum

class QuestionBase(BaseModel):
    id: str
    programme_id: str
    module_id: str
    topic_id: str
    subtopic_id: str
    question_type: str
    answer_type: str
    difficulty: str
    stem_md: str
    solution_md: Optional[str]
    score_weight: float
    metadata_json: Optional[dict]
    version: int
    is_current: bool

    model_config = {
        "from_attributes": True
    }


class QuestionFiltered(BaseModel):
    id: str
    question_type: str
    stem_md: str
    solution_md: Optional[str]
    score_weight: float

    model_config = {
        "from_attributes": True
    }
