from pydantic import BaseModel, Field
from typing import Optional

class AnalysisOutput(BaseModel):
    what_worked_well: Optional[str] = None
    what_can_be_improved: Optional[str] = None

class QualityFeedback(BaseModel):
    correctness: Optional[str] = None
    readability: Optional[str] = None
    maintainability: Optional[str] = None
    design: Optional[str] = None
    scalability: Optional[str] = None

class QualityScores(BaseModel):
    correctness: Optional[int] = None
    readability: Optional[int] = None
    maintainability: Optional[int] = None
    design: Optional[int] = None
    scalability: Optional[int] = None
    overall: Optional[int] = None

class AnswerCreate(BaseModel):
    question_id: str = Field(..., description="UUID of the related question")
    analysis_output: AnalysisOutput
    quality_feedback: QualityFeedback
    quality_scores: QualityScores

class AnswerInput(BaseModel):
    question_text: str
    answer_text: str
    question_id: str
    coe_name: str
    program_name: str
    semester: str
    user_id: str
    module: str
    question_id: str
