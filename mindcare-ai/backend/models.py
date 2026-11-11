"""
MindCare AI - Pydantic Data Models
Defines schema for Mood logs, Behavioral Metrics, Chat queries, and Wellness Insights.
"""

from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from datetime import date, datetime

class MoodType(str):
    HAPPY = "Happy"
    CALM = "Calm"
    ANXIOUS = "Anxious"
    STRESSED = "Stressed"
    SAD = "Sad"
    OVERWHELMED = "Overwhelmed"

class MoodEntryCreate(BaseModel):
    user_id: str = "guest_user"
    log_date: date = Field(default_factory=date.today)
    mood: str = Field(..., description="E.g., Happy, Calm, Anxious, Stressed, Sad, Overwhelmed")
    emoji: str = Field(default="😌")
    valence_score: float = Field(..., ge=1.0, le=10.0, description="1 (very low) to 10 (very positive)")
    sleep_hours: float = Field(..., ge=0.0, le=24.0)
    sleep_quality: Optional[str] = Field(default="Good")
    screen_time_hours: float = Field(..., ge=0.0, le=24.0)
    steps_count: int = Field(default=0, ge=0)
    tags: List[str] = Field(default_factory=list)
    personal_note: Optional[str] = None

class MoodEntryResponse(MoodEntryCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ChatMessage(BaseModel):
    sender: str = Field(..., description="'user' or 'assistant'")
    text: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)

class ChatRequest(BaseModel):
    user_id: str = "guest_user"
    message: str
    conversation_history: List[ChatMessage] = Field(default_factory=list)
    current_mood: Optional[str] = None
    api_key: Optional[str] = None

class ChatActionSuggestion(BaseModel):
    type: str = Field(..., description="'breathing', 'journal', 'soundscape', or 'hotline'")
    label: str
    target_route: str

class ChatResponse(BaseModel):
    reply: str
    is_crisis_detected: bool = False
    crisis_resources: Optional[List[Dict[str, str]]] = None
    suggested_action: Optional[ChatActionSuggestion] = None

class CorrelationMetric(BaseModel):
    factor_name: str
    correlation_coefficient: float
    strength: str
    direction: str
    narrative_insight: str
    recommended_habit: str

class WellnessInsightReport(BaseModel):
    user_id: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)
    disclaimer: str = (
        "Non-Diagnostic Notice: MindCare insights describe statistical associations "
        "between your daily self-reported habits and mood scores. They do not constitute "
        "a medical diagnosis, psychiatric evaluation, or treatment plan."
    )
    total_logs_analyzed: int
    correlations: List[CorrelationMetric]
    key_findings: List[str]
    positive_reinforcements: List[str]
