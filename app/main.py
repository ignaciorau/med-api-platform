from fastapi import FastAPI
from app.db.database import Base, engine
from app.models import user
from app.routes import auth
from fastapi.security import OAuth2PasswordBearer
from app.core.auth import oauth2_scheme
from fastapi import Depends
from app.core.auth import get_current_user


app = FastAPI(title="Medical API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/_auth_test")
def auth_test(token: str = Depends(oauth2_scheme)):
    return {"token": token}

@app.get("/me")
def me(user=Depends(get_current_user)):
    return user
