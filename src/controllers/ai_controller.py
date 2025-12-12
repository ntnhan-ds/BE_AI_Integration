from fastapi import APIRouter
from models.ai_schema import AIRequest
from services.ai_service import AIService

router = APIRouter()

@router.post("/generate")
def create_ai_response(payload: AIRequest):
    return AIService().generate_response(payload)
