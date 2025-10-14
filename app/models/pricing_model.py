from sqlalchemy import Column, Integer, String, Float, DateTime
from app.config.database import Base
from datetime import datetime

class GeminiUsage(Base):
    __tablename__ = "gemini_usage"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(100), nullable=True)
    language = Column(String(50), nullable=False)
    tokens_used = Column(Integer, nullable=False)
    cost = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<GeminiUsage(id={self.id}, language={self.language}, tokens={self.tokens_used}, cost={self.cost})>"
