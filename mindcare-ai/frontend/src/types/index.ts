export type MoodType = 'Happy' | 'Calm' | 'Anxious' | 'Stressed' | 'Sad' | 'Overwhelmed';

export interface MoodLogEntry {
  id?: number;
  date: string;
  mood: MoodType;
  emoji: string;
  score: number; // 1.0 - 10.0
  sleep: number; // hours
  screen: number; // hours
  steps: number;
  tags: string[];
  note?: string;
}

export interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  text: string;
  timestamp: string;
  action?: {
    type: 'breathing' | 'journal' | 'soundscape' | 'hotline';
    label: string;
    targetRoute: string;
  };
}

export interface CorrelationData {
  factorName: string;
  r: number;
  strength: string;
  direction: string;
  insight: string;
  recommendation: string;
}

export interface HabitItem {
  id: number;
  title: string;
  done: boolean;
  icon: string;
}
