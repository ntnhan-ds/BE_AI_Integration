from sqlalchemy.orm import Session
from src.models.text_summary_model import TextSummary

def create_summary(
    db: Session,
    user_id: int,
    input_text: str,
    summary_text: str
):
    summary = TextSummary(
        user_id=user_id,
        input_text=input_text,
        summary_text=summary_text
    )
    db.add(summary)
    db.commit()
    db.refresh(summary)
    return summary
