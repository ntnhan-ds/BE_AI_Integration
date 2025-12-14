from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.config.database import Base


class TextSummary(Base):
    __tablename__ = "text_summaries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    input_text = Column(Text, nullable=False)
    summary_text = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.now())

    user = relationship("User", backref="summaries")
