import { MoodLogEntry, ChatMessage, CorrelationData } from '../types';

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

export const ApiService = {
  async sendChatMessage(message: string, currentMood?: string): Promise<{ reply: string; action?: any; isCrisis?: boolean }> {
    try {
      const res = await fetch(`${API_BASE}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, current_mood: currentMood })
      });
      if (!res.ok) throw new Error('Network error');
      const data = await res.json();
      return {
        reply: data.reply,
        action: data.suggested_action,
        isCrisis: data.is_crisis_detected
      };
    } catch (e) {
      // Local fallback
      return {
        reply: "I am right here with you. Remember to take a gentle, deep breath. How can I best support your comfort today?",
        action: { type: 'breathing', label: 'Try 4-7-8 Breathing', targetRoute: 'selfcare' }
      };
    }
  },

  async fetchMoodLogs(): Promise<MoodLogEntry[]> {
    try {
      const res = await fetch(`${API_BASE}/mood/logs`);
      if (!res.ok) throw new Error('Failed to load logs');
      return await res.json();
    } catch {
      const stored = localStorage.getItem('mindcare_wellness_state_v1');
      if (stored) {
        return JSON.parse(stored).logs || [];
      }
      return [];
    }
  },

  async submitMoodLog(entry: MoodLogEntry): Promise<boolean> {
    try {
      const res = await fetch(`${API_BASE}/mood/log`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          mood: entry.mood,
          emoji: entry.emoji,
          valence_score: entry.score,
          sleep_hours: entry.sleep,
          screen_time_hours: entry.screen,
          steps_count: entry.steps,
          tags: entry.tags,
          personal_note: entry.note
        })
      });
      return res.ok;
    } catch {
      return false;
    }
  },

  async fetchCorrelations(): Promise<any> {
    try {
      const res = await fetch(`${API_BASE}/insights/correlations`);
      if (!res.ok) throw new Error('Failed to load correlations');
      return await res.json();
    } catch {
      return null;
    }
  }
};
