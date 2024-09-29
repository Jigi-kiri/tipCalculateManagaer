from fastapi import FastAPI
from app.routes import user, tip
from fastapi.middleware.cors import CORSMiddleware

from .database import create_db_and_tables


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(tip.router, prefix="/tip", tags=["Tip"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
