from pydantic import BaseModel
from datetime import datetime

class TextSummaryCreate(BaseModel):
    input_text: str

class TextSummaryResponse(BaseModel):
    id: int
    input_text: str
    summary_text: str
    created_at: datetime

    class Config:
        from_attributes = True
