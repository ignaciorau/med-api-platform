from fastapi import FastAPI
from app.db.database import engine

app = FastAPI(title="Medical API")

@app.get("/")
def root():
    return {"status": "ok"}

@app.on_event("startup")
def startup():
    engine.connect()