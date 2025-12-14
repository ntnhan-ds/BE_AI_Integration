from sqlalchemy.orm import Session
from src.integrations.ollama_client import OllamaClient
from src.repositories.text_summary_repository import create_summary
from src.models.user_model import User

ollama_client = OllamaClient(model_name="gpt-oss:20b")

SUMMARY_PROMPT = """
Hãy tóm tắt ngắn gọn, rõ ràng đoạn văn sau:

{text}
"""

def summarize_text(
    *,
    db: Session,
    user: User,
    input_text: str,
):
    prompt = SUMMARY_PROMPT.format(text=input_text)
    summary = ollama_client.generate(prompt)

    return create_summary(
        db,
        user_id=user.id,
        input_text=input_text,
        summary_text=summary,
    )
