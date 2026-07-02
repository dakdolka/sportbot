from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.base import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    duration = Column(Float)
    distance = Column(Float)
    pace = Column(Float)
    avg_heart_rate = Column(Integer)
    max_heart_rate = Column(Integer)
    rpe = Column(Integer)

    user = relationship("User", back_populates="workouts")
