from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.base import Base

class Recovery(Base):
    __tablename__ = "recovery"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime)
    sleep = Column(Float)
    hrv = Column(Integer)
    resting_heart_rate = Column(Integer)
    stress = Column(Integer)
    energy = Column(Integer)
    soreness = Column(Integer)

    user = relationship("User", back_populates="recovery_records")
