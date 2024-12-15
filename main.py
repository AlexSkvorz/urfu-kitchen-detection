from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.api.kitchen_router import kitchen_router


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    title="URFU Kitchen Detection (group 9)",
    root_path="/api",
    version="1.0.0"
)

app.include_router(kitchen_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)
