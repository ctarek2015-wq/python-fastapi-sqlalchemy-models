import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.teas import router as TeasRouter
from controllers.comments import router as CommentsRouter
from controllers.user import router as UsersRouter

app = FastAPI()
app.include_router(TeasRouter, prefix="/api")
app.include_router(CommentsRouter, prefix="/api")
app.include_router(UsersRouter, prefix="/api")

origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "").split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"ok": True}


@app.get("/")
def home():
    return {"message": "Hello World!"}
