from src.config.database import engine, Base
from src.models.user_model import User
from src.models.text_summary_model import TextSummary

Base.metadata.create_all(bind=engine)
