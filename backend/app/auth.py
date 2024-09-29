from .database import get_user_by_email
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends, HTTPException, status
import os
from datetime import timedelta, datetime
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + (expires_delta or ACCESS_TOKEN_EXPIRE_MINUTES)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
