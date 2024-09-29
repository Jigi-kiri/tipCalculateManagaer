from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserResponse
from app.database import SessionLocal
from app.models import User
from app.auth import create_access_token, hash_password, verify_password

router = APIRouter()


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email,
                   hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = create_access_token({"sub": db_user.email})
    return {"name": db_user.name, "token": token}


@router.post("/login")
def login_user(user: UserCreate, db: Session = Depends(SessionLocal)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": db_user.email})
    return {"name": db_user.name, "token": token}
