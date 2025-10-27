from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.session import engine
from db.base import Base

from routers import auth, admin  # make sure packages import correctly

# create tables (in dev). For prod rely on Alembic migrations.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth+Roles API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"message": "Auth+Roles API up"}
