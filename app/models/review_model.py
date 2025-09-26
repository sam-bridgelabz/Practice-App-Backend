import uuid
from sqlalchemy import Column, CHAR, Text, Integer, DateTime, ForeignKey, func, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.config.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    answer_id = Column(
        String(36),
        ForeignKey("answers.id", ondelete="SET NULL"),
        nullable=True
    )
    reviewer = Column(String(100))
    user_id = Column(String(36), nullable=True)
    review_summary = Column(Text)
    review_points = Column(Text)

    # Quantitative scores
    score_correctness = Column(Integer)
    score_readability = Column(Integer)
    score_maintainability = Column(Integer)
    score_design = Column(Integer)
    score_scalability = Column(Integer)
    score_overall = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())

    answer = relationship("Answer", back_populates="reviews")

    __table_args__ = (
        UniqueConstraint('user_id', 'answer_id', name='uq_user_answer'),
    )
