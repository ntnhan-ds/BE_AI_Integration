from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.home_controller import router as HomeRouter
from controllers.ai_controller import router as AIRouter


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
    app.include_router(AIRouter, prefix="/ai", tags=["AI"])


    return app


app = create_app()
