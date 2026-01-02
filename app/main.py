from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user
from app.routes import auth

app = FastAPI(title="Medical API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"status": "ok"}
