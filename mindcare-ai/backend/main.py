"""
MindCare AI - FastAPI Main Application Server
Full RESTful backend providing AI chat, mood logging, correlation analytics,
and privacy data management.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from datetime import date, timedelta
import random

from database import init_db, get_db, MoodLog
from models import (
    MoodEntryCreate, 
    MoodEntryResponse, 
    ChatRequest, 
    ChatResponse, 
    WellnessInsightReport
)
from correlation_engine import BehavioralCorrelationEngine
from ai_companion import get_companion_reply, CRISIS_RESOURCES

app = FastAPI(
    title="MindCare AI API",
    description="Empathetic, non-diagnostic AI mental wellness companion backend",
    version="1.0.0"
)

# CORS setup for local React / Next.js / HTML frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()
    # Seed initial 14-day sample data if empty
    db = next(get_db())
    count = db.query(MoodLog).count()
    if count == 0:
        seed_sample_logs(db)

def seed_sample_logs(db: Session):
    """Populates realistic baseline wellness logs for immediate analytics."""
    sample_data = [
        {"day_offset": 10, "mood": "Stressed", "emoji": "😫", "score": 4.0, "sleep": 5.5, "screen": 6.8, "steps": 3200, "note": "Deadline stress.", "tags": "Work"},
        {"day_offset": 9, "mood": "Anxious", "emoji": "😰", "score": 4.5, "sleep": 6.0, "screen": 6.2, "steps": 4100, "note": "Nervous about presentation.", "tags": "Work,Social"},
        {"day_offset": 8, "mood": "Calm", "emoji": "😌", "score": 7.0, "sleep": 7.2, "screen": 4.5, "steps": 6800, "note": "Scenic walk in the park.", "tags": "Rest,Exercise"},
        {"day_offset": 7, "mood": "Happy", "emoji": "😊", "score": 8.5, "sleep": 8.0, "screen": 3.8, "steps": 8900, "note": "Relaxed family evening.", "tags": "Outdoors,Family"},
        {"day_offset": 6, "mood": "Calm", "emoji": "😌", "score": 7.5, "sleep": 7.5, "screen": 4.2, "steps": 7200, "note": "Morning yoga, felt grounded.", "tags": "Exercise"},
        {"day_offset": 5, "mood": "Overwhelmed", "emoji": "🤯", "score": 3.8, "sleep": 5.2, "screen": 7.5, "steps": 2900, "note": "Doomscrolling late night.", "tags": "Work"},
        {"day_offset": 4, "mood": "Calm", "emoji": "😌", "score": 7.0, "sleep": 7.0, "screen": 4.0, "steps": 6500, "note": "Box breathing helped a lot.", "tags": "Rest"},
        {"day_offset": 3, "mood": "Happy", "emoji": "😊", "score": 8.2, "sleep": 8.2, "screen": 3.5, "steps": 9400, "note": "Wonderful outdoor hike.", "tags": "Outdoors,Exercise"},
        {"day_offset": 2, "mood": "Calm", "emoji": "😌", "score": 7.6, "sleep": 7.4, "screen": 4.1, "steps": 7800, "note": "Peaceful productive day.", "tags": "Work"},
        {"day_offset": 1, "mood": "Anxious", "emoji": "😰", "score": 5.0, "sleep": 6.1, "screen": 5.8, "steps": 4300, "note": "Crowded commute felt draining.", "tags": "Social"},
        {"day_offset": 0, "mood": "Calm", "emoji": "😌", "score": 7.4, "sleep": 7.5, "screen": 4.0, "steps": 6500, "note": "Feeling centered today.", "tags": "Rest,Exercise"}
    ]
    today = date.today()
    for item in sample_data:
        entry = MoodLog(
            user_id="guest_user",
            log_date=today - timedelta(days=item["day_offset"]),
            mood=item["mood"],
            emoji=item["emoji"],
            valence_score=item["score"],
            sleep_hours=item["sleep"],
            screen_time_hours=item["screen"],
            steps_count=item["steps"],
            tags=item["tags"],
            personal_note=item["note"]
        )
        db.add(entry)
    db.commit()

@app.get("/api/health")
def health_check():
    return {"status": "ok", "app": "MindCare AI", "service": "Mental Wellness Companion"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_companion(req: ChatRequest):
    """Conversational endpoint with empathetic guidance, crisis interception, and tool suggestions."""
    return await get_companion_reply(req)

@app.post("/api/mood/log", response_model=Dict[str, Any])
def log_mood(entry: MoodEntryCreate, db: Session = Depends(get_db)):
    """Logs a user's daily mood, sleep, screen time, and activity."""
    db_entry = MoodLog(
        user_id=entry.user_id,
        log_date=entry.log_date,
        mood=entry.mood,
        emoji=entry.emoji,
        valence_score=entry.valence_score,
        sleep_hours=entry.sleep_hours,
        sleep_quality=entry.sleep_quality,
        screen_time_hours=entry.screen_time_hours,
        steps_count=entry.steps_count,
        tags=",".join(entry.tags),
        personal_note=entry.personal_note
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return {"status": "success", "id": db_entry.id, "message": "Mood logged successfully"}

@app.get("/api/mood/logs", response_model=List[Dict[str, Any]])
def get_mood_logs(user_id: str = "guest_user", limit: int = 30, db: Session = Depends(get_db)):
    """Retrieves chronological mood records for charts and calendar visualization."""
    records = (
        db.query(MoodLog)
        .filter(MoodLog.user_id == user_id)
        .order_by(MoodLog.log_date.asc())
        .limit(limit)
        .all()
    )
    return [
        {
            "id": r.id,
            "date": r.log_date.isoformat(),
            "mood": r.mood,
            "emoji": r.emoji,
            "score": r.valence_score,
            "sleep": r.sleep_hours,
            "screen": r.screen_time_hours,
            "steps": r.steps_count,
            "tags": [t.strip() for t in r.tags.split(",") if t.strip()],
            "note": r.personal_note
        }
        for r in records
    ]

@app.get("/api/insights/correlations", response_model=WellnessInsightReport)
def get_behavioral_insights(user_id: str = "guest_user", db: Session = Depends(get_db)):
    """Computes Pearson correlations between sleep, screen time, steps, and emotional scores."""
    records = (
        db.query(MoodLog)
        .filter(MoodLog.user_id == user_id)
        .order_by(MoodLog.log_date.asc())
        .all()
    )
    logs_data = [
        {
            "valence_score": r.valence_score,
            "sleep_hours": r.sleep_hours,
            "screen_time_hours": r.screen_time_hours,
            "steps_count": r.steps_count
        }
        for r in records
    ]
    return BehavioralCorrelationEngine.analyze_patterns(user_id, logs_data)

@app.get("/api/crisis/resources")
def get_crisis_resources():
    """Returns 24/7 emergency hotlines, text lines, and immediate grounding methods."""
    return {
        "disclaimer": "MindCare is non-diagnostic. In immediate danger or crisis, reach out to professional emergency personnel.",
        "resources": CRISIS_RESOURCES
    }

@app.delete("/api/user/data")
def delete_all_user_data(user_id: str = "guest_user", db: Session = Depends(get_db)):
    """Permanently purges all mood and habit logs for privacy compliance."""
    db.query(MoodLog).filter(MoodLog.user_id == user_id).delete()
    db.commit()
    return {"status": "success", "message": "All user data deleted permanently."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
