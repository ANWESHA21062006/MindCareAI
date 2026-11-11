"""
MindCare AI - SQLite Database Models and Connection Setup
Ensures local privacy-first persistent storage.
"""

import os
from datetime import datetime, date
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Date, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./mindcare_records.db")

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MoodLog(Base):
    __tablename__ = "mood_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(64), index=True, default="guest_user")
    log_date = Column(Date, default=date.today)
    mood = Column(String(32), nullable=False)
    emoji = Column(String(16), default="😌")
    valence_score = Column(Float, nullable=False) # 1.0 - 10.0
    sleep_hours = Column(Float, default=7.0)
    sleep_quality = Column(String(32), default="Good")
    screen_time_hours = Column(Float, default=4.0)
    steps_count = Column(Integer, default=5000)
    tags = Column(String(256), default="") # Comma-separated
    personal_note = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
