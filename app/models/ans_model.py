import uuid
from sqlalchemy import Column, CHAR, Text, Integer, DateTime, ForeignKey, func
from app.config.database import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    question_id = Column(CHAR(36), ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)

    # Example columns for your JSON fields:
    what_worked_well = Column(Text, nullable=True)
    what_can_be_improved = Column(Text, nullable=True)

    correctness = Column(Text, nullable=True)
    readability = Column(Text, nullable=True)
    maintainability = Column(Text, nullable=True)
    design = Column(Text, nullable=True)
    scalability = Column(Text, nullable=True)

    correctness_score = Column(Integer, nullable=True)
    readability_score = Column(Integer, nullable=True)
    maintainability_score = Column(Integer, nullable=True)
    design_score = Column(Integer, nullable=True)
    scalability_score = Column(Integer, nullable=True)
    overall_score = Column(Integer, nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
