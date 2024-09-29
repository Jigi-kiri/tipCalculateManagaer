from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    proPic = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    last_login = Column(DateTime, default=datetime.utcnow)


class Tip(Base):
    __tablename__ = 'tips'
    id = Column(Integer, primary_key=True, index=True)
    place = Column(String, nullable=False)
    totalAmount = Column(Float, nullable=False)
    tipAmount = Column(Float, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")
