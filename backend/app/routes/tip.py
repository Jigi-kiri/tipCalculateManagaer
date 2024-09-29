from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import TipCreate, TipResponse, TipListResponse
from app.models import Tip
from app.database import SessionLocal

router = APIRouter()


@router.post("/calculate", response_model=TipResponse)
def calculate_tip(tip_data: TipCreate, db: Session = Depends(SessionLocal)):
    tip_amount = (tip_data.tipPercentage / 100) * tip_data.totalAmount
    new_tip = Tip(
        place=tip_data.place,
        total_amount=tip_data.totalAmount,
        tip_percentage=tip_data.tipPercentage,
        tip_amount=tip_amount
    )
    db.add(new_tip)
    db.commit()
    return {"tip": tip_amount}


@router.get("/", response_model=List[TipListResponse])
def get_tips(startDate: str, endDate: str, db: Session = Depends(SessionLocal)):
    # Implement logic to filter tips by date range
    tips = db.query(Tip).filter_by().all()
    return tips
