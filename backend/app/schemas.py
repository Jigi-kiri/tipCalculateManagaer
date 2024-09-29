from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    name: str
    proPic: Optional[str] = None
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    name: str
    token: str


class Token(BaseModel):
    token: str


class TipCreate(BaseModel):
    place: str
    totalAmount: float
    tipPercentage: float


class TipResponse(BaseModel):
    tip: float


class TotalTip(BaseModel):
    place: str
    totalAmount: float
    tipAmount: float


class TotalTipResponse(BaseModel):
    totalTip: List[TotalTip]
