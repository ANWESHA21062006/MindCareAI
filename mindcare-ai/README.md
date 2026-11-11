# MindCare AI - AI Mental Wellness Companion

> **"Understanding your emotions through gentle daily awareness, behavioral patterns, and supportive self-care."**

MindCare AI is a modern, responsive, non-diagnostic mental wellness application built to help individuals track their emotional well-being, uncover correlations between their habits (sleep duration, screen time, physical activity) and their mood, and engage with compassionate AI companionship and evidence-based grounding practices.

---

## 🌟 Core Features

### 1. AI Chat Companion
- **Empathetic Emotional Support:** Validates feelings without judgment or clinical coldness.
- **Actionable Grounding Suggestions:** Recommends breathing techniques, journaling questions, and relaxation audio.
- **Safety & Crisis Interception:** Automatically screens for distress and self-harm keywords, providing immediate compassionate de-escalation, emergency hotlines (988 in USA/Canada, 14416 in India, 111/116 in UK), and grounding exercises.
- **Optional Gemini API Integration:** Seamlessly switches between built-in on-device empathetic responses and live Google Gemini API models.

### 2. Daily Mood & Habit Tracker
- **Categorized Emotional States:** Track feelings like *Happy*, *Calm*, *Anxious*, *Stressed*, *Sad*, and *Overwhelmed*.
- **Emotional Intensity Slider:** Fine-grained 1-10 energy and valence scale.
- **Contextual Tags & Journaling:** Tag entries with *Work*, *Rest*, *Family*, *Exercise*, *Social*, and write reflective notes.
- **Calendar & Timeline View:** Monthly heatmaps and chronological reflection cards.

### 3. Behavioral Pattern Analysis
- **Holistic Lifestyle Tracking:** Sleep duration, daily screen time, and physical steps.
- **Statistical Correlation Engine:** Calculates Pearson correlation coefficients ($r$) between:
  - Sleep duration vs. Mood valence (e.g., $r = +0.78$ indicating significant emotional stabilization)
  - Screen time vs. Perceived stress ($r = +0.64$ identifying fatigue thresholds)
  - Daily step count vs. Calmness ($r = +0.52$ showing mood elevation with movement)

### 4. Non-Diagnostic AI Wellness Insights
- Generates transparent, plain-language pattern explanations (e.g., *"You reported feeling stressed on days when sleep duration was under 6.0 hours"*).
- Strictly non-diagnostic: explicitly emphasizes wellness habits rather than claiming behavioral patterns constitute a medical diagnosis.

### 5. Personalized Self-Care & Grounding Studio
- **Guided Animated Breathing:**
  - **4-7-8 Relaxing Breath:** Natural tranquilizer for pre-sleep anxiety.
  - **Box Breathing (4-4-4-4):** Used to reset high nervous system arousal.
  - **Deep Calm (5-5 Coherence):** Balances heart rate variability (HRV).
  - Dynamic visual breathing sphere with phase timers and cycle counters.
- **Ambient Soundscapes (Web Audio API Synthesizer):** Zero external audio file dependencies. Synthesizes Gentle Rain (pink noise), Ocean Waves (modulated filter), Forest Wind, and 432Hz Zen Drones in real-time.
- **Guided Journaling Studio:** Daily cognitive reframing and gratitude prompts with private on-device storage.
- **Sleep Hygiene Checklist:** Practical evidence-based wind-down habits.

### 6. Comprehensive Privacy & Safety Architecture
- **Client-Side Data Ownership:** Check-ins and journal entries are stored locally.
- **Export Data:** Download complete mood and habit histories in structured JSON format.
- **Delete All Records:** 1-click permanent erasure for total privacy control.
- **Crisis Support Directory:** Dedicated 24/7 emergency contacts and 5-4-3-2-1 grounding protocol accessible from every screen.

---

## 🎨 UI/UX Design System
- **Palette:** Soft lavender (`#8B5CF6`, `#EDE9FE`), pastel sky blue (`#38BDF8`, `#E0F2FE`), mint green (`#10B981`, `#DCFCE7`), and warm rose accents.
- **Typography & Layout:** Clean Inter typography, glassmorphism cards, rounded pill buttons, and responsive mobile-first architecture.

---

## 📂 Project Structure

```text
mindcare-ai/
├── index.html                   # Zero-install, standalone full-stack interactive SPA (Open in any browser!)
├── README.md                    # Project documentation & execution guide
├── backend/                     # Python FastAPI Backend
│   ├── main.py                  # API endpoints (Chat, Mood logging, Insights, Crisis)
│   ├── models.py                # Pydantic schemas
│   ├── correlation_engine.py    # Statistical correlation engine (Pearson r, patterns)
│   ├── ai_companion.py          # Empathetic AI companion & crisis interception
│   ├── database.py              # SQLite & SQLAlchemy persistent database
│   └── requirements.txt         # FastAPI dependencies
└── frontend/                    # Modern React / TypeScript architecture
    ├── package.json
    ├── tailwind.config.js
    ├── index.html
    └── src/
        ├── App.tsx
        ├── main.tsx
        ├── index.css
        ├── types/index.ts
        ├── services/api.ts
        └── components/
            ├── Navbar.tsx
            └── CrisisModal.tsx
```

---

## 🚀 How to Run

### Option 1: Instant Standalone Web App (Zero Setup)
Simply double-click or open `index.html` in your favorite web browser (Chrome, Edge, Firefox, Safari).
- Everything (AI companion engine, charts, Web Audio soundscape synthesizer, breathing animations, and local persistence) runs immediately with **zero installs and zero configuration**!

### Option 2: Running the Python FastAPI Backend
```bash
# Navigate to the backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload --port 8000
```
- Open your browser to `http://localhost:8000/docs` to test interactive Swagger API documentation.

### Option 3: Running the React Frontend
```bash
# Navigate to the frontend directory
cd frontend

# Install npm packages
npm install

# Start Vite dev server
npm run dev
```

---

## ⚖️ Non-Diagnostic Disclaimer
*MindCare AI is an educational and lifestyle tool designed to support personal emotional awareness and daily habits. It is not a medical device, psychiatric diagnostic system, or substitute for professional medical care. If you are experiencing symptoms of acute psychological distress or thoughts of self-harm, please contact emergency medical personnel or the 988 Suicide & Crisis Lifeline immediately.*
