from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from app.core.auth import get_current_user

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd.hash(password)

def verify_password(plain, hashed):
    return pwd.verify(plain, hashed)

def require_role(role: str):
    def checker(user = Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(status_code=403, detail="No autorizado")
        return user
    return checker
