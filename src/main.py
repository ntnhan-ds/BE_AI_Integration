from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controllers.home_controller import router as HomeRouter
from src.controllers.user_controller import router as UserRouter
from src.controllers.text_summary_controller import router as TextSummaryRouter

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Integration",
        version="1.0.0",
    )

    # CORS setup
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(HomeRouter, prefix="/home", tags=["Home"])
    app.include_router(UserRouter, prefix="/user", tags=["User"])
    app.include_router(TextSummaryRouter, prefix="/text_summary", tags=["AI"])

    return app


app = create_app()
