import React from 'react';
import { Heart, Sparkles, Plus, AlertCircle } from 'lucide-react';

interface NavbarProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
  onOpenMoodModal: () => void;
  onOpenCrisisModal: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  setActiveTab,
  onOpenMoodModal,
  onOpenCrisisModal
}) => {
  const tabs = [
    { id: 'dashboard', label: 'Dashboard' },
    { id: 'chat', label: 'AI Companion' },
    { id: 'mood', label: 'Mood Tracker' },
    { id: 'insights', label: 'Behavioral Insights' },
    { id: 'selfcare', label: 'Self-Care' },
    { id: 'settings', label: 'Privacy & Settings' }
  ];

  return (
    <header className="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-slate-100 shadow-xs">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand */}
        <div 
          onClick={() => setActiveTab('dashboard')} 
          className="flex items-center space-x-3 cursor-pointer select-none"
        >
          <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-lavender-500 via-pastelBlue-400 to-mint-400 flex items-center justify-center text-white shadow-md shadow-lavender-200">
            <Heart className="w-5 h-5 fill-current" />
          </div>
          <div>
            <span className="text-xl font-bold bg-gradient-to-r from-lavender-600 to-pastelBlue-500 bg-clip-text text-transparent">
              MindCare AI
            </span>
            <span className="hidden sm:inline-block ml-2 px-2 py-0.5 text-[10px] uppercase tracking-wider font-semibold bg-lavender-100 text-lavender-700 rounded-full">
              Companion
            </span>
          </div>
        </div>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center space-x-1">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-3.5 py-2 rounded-xl text-xs font-semibold transition ${
                activeTab === tab.id
                  ? 'text-lavender-700 bg-lavender-50 shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </nav>

        {/* CTA buttons */}
        <div className="flex items-center space-x-2">
          <button
            onClick={onOpenMoodModal}
            className="hidden sm:inline-flex items-center space-x-1 px-3.5 py-2 rounded-xl bg-gradient-to-r from-lavender-600 to-mint-500 text-white text-xs font-semibold shadow-xs hover:opacity-95 transition"
          >
            <Plus className="w-3.5 h-3.5" />
            <span>Check-In</span>
          </button>
          <button
            onClick={onOpenCrisisModal}
            className="px-2.5 py-1.5 rounded-xl bg-rose-50 text-rose-600 hover:bg-rose-100 text-xs font-semibold border border-rose-200 transition flex items-center space-x-1"
          >
            <AlertCircle className="w-3.5 h-3.5" />
            <span>Crisis SOS</span>
          </button>
        </div>
      </div>
    </header>
  );
};
