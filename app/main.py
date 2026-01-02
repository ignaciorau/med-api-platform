from fastapi import FastAPI
from app.db.database import engine
from app.db.database import Base, engine
from app.models import user
from app.routes import auth

app = FastAPI(title="Medical API")

@app.get("/")
def root():
    return {"status": "ok"}

@app.on_event("startup")
def startup():
    engine.connect()

app.include_router(auth.router)

Base.metadata.create_all(bind=engine)