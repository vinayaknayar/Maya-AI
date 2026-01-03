from fastapi import APIRouter, Depends, HTTPException
from .models import User
from sqlmodel import Session, select
from .database import engine, get_db
from pydantic import BaseModel

class RegisterRequest(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

######
# /auth/register endpoint
# /auth/login endpoint
# Simple placeholder hashing (we can upgrade to JWT next)
######

router = APIRouter()


@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = User(
        email=data.email,
        hashed_password=data.password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created"}


@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or user.hashed_password != data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"access_token": "fake-token", "token_type": "bearer"}
