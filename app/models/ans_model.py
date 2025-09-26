import uuid
from sqlalchemy import Column, CHAR, Text, Integer, DateTime, ForeignKey, func, String, UniqueConstraint
from sqlalchemy.orm import relationship
from app.config.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    question_id = Column(String(36), ForeignKey("questions.id"), nullable=False)
    user_id = Column(String(36), nullable=True)
    file_url = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    reviews = relationship("Review", back_populates="answer", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint('user_id', 'question_id', name='uq_user_question'),
    )


