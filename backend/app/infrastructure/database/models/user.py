from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from app.infrastructure.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)
    gender = Column(String(10))
    experience = Column(String(50))
    created_at = Column(DateTime)

    goals = relationship("Goal", back_populates="user")
    training_plans = relationship("TrainingPlan", back_populates="user")
    workouts = relationship("Workout", back_populates="user")
    recovery_records = relationship("Recovery", back_populates="user")
    ai_summaries = relationship("AISummary", back_populates="user")
