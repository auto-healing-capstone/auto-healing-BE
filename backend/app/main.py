# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import alerts, incidents
from app.core.config import settings
import app.models.schema  # noqa: F401 --- Ensure ORM models are registered before DB init

app = FastAPI(
    title="AIOps AutoHealing API",
    version="1.0.0",
)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_V1_PREFIX = settings.API_V1_STR

app.include_router(alerts.router, prefix=API_V1_PREFIX, tags=["Alerts"])
app.include_router(incidents.router, prefix=API_V1_PREFIX, tags=["Incidents"])


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
