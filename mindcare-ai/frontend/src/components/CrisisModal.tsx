import React from 'react';
import { Heart, Phone, ShieldAlert, X } from 'lucide-react';

interface CrisisModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const CrisisModal: React.FC<CrisisModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border-2 border-rose-200 relative animate-in fade-in zoom-in-95 duration-200">
        <button
          onClick={onClose}
          className="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 text-slate-500 hover:text-slate-800 flex items-center justify-center text-sm font-bold"
        >
          <X className="w-4 h-4" />
        </button>

        <div className="flex items-center space-x-3 mb-4">
          <div className="w-12 h-12 rounded-2xl bg-rose-100 text-rose-600 flex items-center justify-center text-2xl font-bold">
            <Heart className="w-6 h-6 fill-rose-500 text-rose-500" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-slate-800">You Are Not Alone</h3>
            <p className="text-xs text-rose-600 font-semibold">Immediate, Free & Confidential Support</p>
          </div>
        </div>

        <p className="text-xs text-slate-600 leading-relaxed mb-5">
          If you are experiencing overwhelming emotional pain, thoughts of self-harm, or are in immediate physical danger, compassionate, trained counselors are waiting to speak with you right now.
        </p>

        {/* Helplines Box */}
        <div className="space-y-3 mb-6">
          <a
            href="tel:988"
            className="flex items-center justify-between p-4 rounded-2xl bg-rose-50 border border-rose-200 hover:bg-rose-100/80 transition group"
          >
            <div>
              <span className="text-xs font-bold text-rose-800 block">USA & Canada: 988 Suicide & Crisis Lifeline</span>
              <span className="text-[11px] text-slate-600">Available 24/7. Call or text 988. Free & confidential.</span>
            </div>
            <span className="px-3 py-1.5 rounded-xl bg-rose-600 text-white font-bold text-xs shadow-xs group-hover:scale-105 transition flex items-center space-x-1">
              <Phone className="w-3.5 h-3.5" />
              <span>Call 988</span>
            </span>
          </a>

          <div className="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-xs">
            <span className="font-bold text-slate-800 block">Crisis Text Line (US, UK, Canada)</span>
            <span className="text-slate-600 text-[11px]">Text HOME to 741741 to connect with a Crisis Counselor.</span>
          </div>

          <div className="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-xs">
            <span className="font-bold text-slate-800 block">India: Tele-MANAS</span>
            <span className="text-slate-600 text-[11px]">Dial 14416 or 1800 891 4416 (Govt. 24/7 Mental Health Helpline).</span>
          </div>
        </div>

        {/* Immediate 5-4-3-2-1 Grounding */}
        <div className="p-4 rounded-2xl bg-lavender-50 border border-lavender-200 text-xs">
          <h4 className="font-bold text-lavender-800 mb-1">Emergency 5-4-3-2-1 Grounding:</h4>
          <p className="text-slate-600 text-[11px] leading-relaxed">
            Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 positive truth about yourself right now.
          </p>
        </div>

        <div className="mt-5 text-center">
          <button onClick={onClose} className="text-xs text-slate-500 hover:text-slate-800 underline">
            Return to wellness companion
          </button>
        </div>
      </div>
    </div>
  );
};
