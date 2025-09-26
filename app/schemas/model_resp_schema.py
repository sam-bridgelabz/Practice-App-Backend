from pydantic import BaseModel

class AnalysisOutput(BaseModel):
    what_worked_well: str
    what_can_be_improved: str


class QualityFeedback(BaseModel):
    correctness: str
    readability: str
    maintainability: str
    design: str
    scalability: str


class QualityScores(BaseModel):
    correctness: int
    readability: int
    maintainability: int
    design: int
    scalability: int
    overall: int


class CodeReviewOutput(BaseModel):
    analysis_output: AnalysisOutput
    quality_feedback: QualityFeedback
    quality_scores: QualityScores

class CodeReviewResponse(BaseModel):
    success_status: bool
    error_details: str | None
    results: CodeReviewOutput
