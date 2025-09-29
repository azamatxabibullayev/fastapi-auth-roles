from fastapi import FastAPI
from db.session import Base, engine
from routers import auth, admin

app = FastAPI(title="FastAPI Auth Roles")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(admin.router)
