"""
MindCare AI - Empathetic AI Companion & Safety Interceptor
Provides non-diagnostic, compassionate emotional companionship.
Enforces crisis detection guardrails and self-care recommendations.
"""

import os
import re
from typing import Dict, Any, List, Optional
from models import ChatRequest, ChatResponse, ChatActionSuggestion

CRISIS_KEYWORDS = [
    r"\bkill myself\b",
    r"\bsuicide\b",
    r"\bwant to die\b",
    r"\bend my life\b",
    r"\bhurt myself\b",
    r"\bself[- ]?harm\b",
    r"\bcutting\b",
    r"\bno reason to live\b",
    r"\bbetter off dead\b",
    r"\bcan'?t go on\b",
    r"\bend it all\b"
]

CRISIS_RESOURCES = [
    {
        "region": "United States & Canada",
        "service": "988 Suicide & Crisis Lifeline",
        "contact": "Call or Text 988 (Available 24/7, Free, Confidential)"
    },
    {
        "region": "Crisis Text Line (US/UK/Canada)",
        "service": "Crisis Text Line",
        "contact": "Text HOME to 741741"
    },
    {
        "region": "United Kingdom",
        "service": "Samaritans & NHS 111",
        "contact": "Call 116 123 (Samaritans) or 111 (NHS Mental Health)"
    },
    {
        "region": "India",
        "service": "Tele-MANAS",
        "contact": "Dial 14416 or 1800 891 4416"
    },
    {
        "region": "International",
        "service": "Befrienders Worldwide",
        "contact": "Visit https://www.befrienders.org for global crisis hotlines"
    }
]

SYSTEM_PROMPT = """You are MindCare AI, an empathetic, non-diagnostic mental wellness companion.
Your mission is to offer warmth, active listening, gentle perspective reframing, and self-care practices.

Core Guidelines:
1. NON-DIAGNOSTIC: Never diagnose mental health conditions (e.g. do not say "You have major depressive disorder" or "This is ADHD"). Focus on validating present feelings, daily habits, and stress relief.
2. EMPATHETIC & SUPPORTIVE: Validate the user's emotion before offering solutions. Use warm, calming language.
3. ACTIONABLE SELF-CARE: Proactively suggest grounding techniques:
   - 4-7-8 breathing or box breathing for anxiety / physical tension
   - Guided journaling questions for overthinking or racing thoughts
   - Sleep wind-down routines or ambient sounds for sleep struggles
   - Gentle physical movement for sluggishness or brain fog
4. SAFETY: If the user indicates self-harm or immediate crisis, provide emergency hotlines immediately with compassionate care.
Keep responses concise, conversational, and easy to read.
"""

def detect_crisis(message: str) -> bool:
    """Checks if message contains crisis or self-harm markers."""
    msg_lower = message.lower()
    for pattern in CRISIS_KEYWORDS:
        if re.search(pattern, msg_lower):
            return True
    return False

def generate_local_companion_reply(user_msg: str, mood: Optional[str] = None) -> ChatResponse:
    """Fallback empathetic response generator that runs completely offline with zero latency."""
    lower = user_msg.lower()

    if any(k in lower for k in ["breath", "anxious", "panic", "heart racing", "chest"]):
        return ChatResponse(
            reply=(
                "I hear the tension you're experiencing. When anxiety surges, our nervous system switches "
                "into high alert and shallow breathing signals danger to the brain. Let's take a pause together. "
                "A gentle 4-7-8 breath or box breathing exercise can physically signal your vagus nerve to slow down."
            ),
            suggested_action=ChatActionSuggestion(
                type="breathing",
                label="Start Guided 4-7-8 Breathing",
                target_route="selfcare"
            )
        )

    if any(k in lower for k in ["overwhelm", "burnout", "work", "too much", "deadline", "exhaust"]):
        return ChatResponse(
            reply=(
                "It sounds like you have been carrying a heavy weight on your shoulders. When everything feels "
                "urgent at once, our cognitive capacity gets flooded. You don't have to solve everything today. "
                "What is one tiny task you can give yourself permission to step away from or simplify right now?"
            ),
            suggested_action=ChatActionSuggestion(
                type="journal",
                label="Open Journaling Prompt",
                target_route="selfcare"
            )
        )

    if any(k in lower for k in ["sleep", "tired", "insomnia", "wake up", "bed", "night"]):
        return ChatResponse(
            reply=(
                "Sleep struggles can make every small daily frustration feel so much louder. Even if sleep feels "
                "elusive tonight, try to rest your eyes and body quietly—quiet resting still provides valuable physical "
                "restoration. Would you like to put on some calming ambient rain or wave sounds in the background?"
            ),
            suggested_action=ChatActionSuggestion(
                type="soundscape",
                label="Play Rain Soundscape",
                target_route="selfcare"
            )
        )

    if any(k in lower for k in ["sad", "lonely", "down", "cry", "hopeless"]):
        return ChatResponse(
            reply=(
                "Thank you for sharing that with me. It takes real courage to admit when you're feeling down. "
                "Please remember that sadness is a natural emotion that deserves gentle space, not self-judgment. "
                "Treat yourself as kindly today as you would treat a close friend going through the same thing."
            ),
            suggested_action=ChatActionSuggestion(
                type="journal",
                label="Write a Gentle Reflection",
                target_route="selfcare"
            )
        )

    # General supportive answer
    return ChatResponse(
        reply=(
            f"Thank you for checking in{' feeling ' + mood if mood else ''}. I'm here to listen and help you unpack "
            "whatever is on your mind. We can explore what might be contributing to your mood today, try a short "
            "calming exercise, or just talk it through. What would feel most supportive right now?"
        ),
        suggested_action=ChatActionSuggestion(
            type="breathing",
            label="Try a 2-Minute Breathing Pause",
            target_route="selfcare"
        )
    )

async def get_companion_reply(req: ChatRequest) -> ChatResponse:
    """Orchestrates safety screening, Gemini LLM invocation, and fallback."""
    # 1. Emergency Safety Filter
    if detect_crisis(req.message):
        return ChatResponse(
            reply=(
                "I hear how much pain you are carrying right now, and I want you to know that your life and safety "
                "deeply matter. Because I am an AI, I cannot provide the emergency human support you deserve right now. "
                "Please connect with a compassionate crisis counselor immediately. You don't have to carry this alone."
            ),
            is_crisis_detected=True,
            crisis_resources=CRISIS_RESOURCES,
            suggested_action=ChatActionSuggestion(
                type="hotline",
                label="Call 988 (USA/Canada) or 14416 (India)",
                target_route="crisis"
            )
        )

    # 2. Try Gemini API if key is provided or configured in environment
    api_key = req.api_key or os.environ.get("GEMINI_API_KEY")
    if api_key:
        try:
            from google import genai
            client = genai.Client(api_key=api_key)
            prompt_content = f"{SYSTEM_PROMPT}\n\nUser mood context: {req.current_mood or 'Unspecified'}\nUser message: {req.message}"
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_content,
            )
            if response and response.text:
                return ChatResponse(
                    reply=response.text.strip(),
                    is_crisis_detected=False,
                    suggested_action=ChatActionSuggestion(
                        type="breathing",
                        label="Explore Calming Exercises",
                        target_route="selfcare"
                    )
                )
        except Exception as e:
            # Fall through to resilient local empathy engine on any API error or quota limit
            pass

    # 3. Fallback to Local Empathetic Engine
    return generate_local_companion_reply(req.message, req.current_mood)
