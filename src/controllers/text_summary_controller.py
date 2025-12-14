from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.db_depend import get_db
from src.security.dependency import get_current_user
from src.models.user_model import User
from src.models.text_summary_schema import (
    TextSummaryCreate,
    TextSummaryResponse,
)
from src.services.text_summary_service import summarize_text

router = APIRouter()

@router.post("/summary", response_model=TextSummaryResponse)
def create_summary_api(
    data: TextSummaryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return summarize_text(
        db=db,
        user=current_user,
        input_text=data.input_text,
    )
