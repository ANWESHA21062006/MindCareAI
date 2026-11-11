import React, { useState } from 'react';
import { Navbar } from './components/Navbar';
import { CrisisModal } from './components/CrisisModal';
import { MoodLogEntry } from './types';

export const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<string>('dashboard');
  const [isCrisisModalOpen, setIsCrisisModalOpen] = useState<boolean>(false);
  const [isMoodModalOpen, setIsMoodModalOpen] = useState<boolean>(false);

  return (
    <div className="min-h-screen bg-[#F8FAFC] flex flex-col font-sans text-slate-800">
      {/* Non-intrusive safety notification banner */}
      <div className="bg-gradient-to-r from-amber-50 via-rose-50 to-lavender-50 border-b border-rose-100 text-xs text-slate-700 py-2 px-4">
        <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center space-x-2">
            <span className="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
            <span className="font-medium text-slate-700">MindCare AI is a wellness awareness companion, not a medical or diagnostic device.</span>
          </div>
          <button 
            onClick={() => setIsCrisisModalOpen(true)}
            className="text-rose-600 font-bold hover:underline"
          >
            Immediate Crisis Support (988) &rarr;
          </button>
        </div>
      </div>

      {/* Main Navbar */}
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        onOpenMoodModal={() => setIsMoodModalOpen(true)}
        onOpenCrisisModal={() => setIsCrisisModalOpen(true)}
      />

      {/* Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8">
        <div className="bg-white rounded-3xl p-8 border border-slate-100 shadow-sm text-center space-y-4">
          <h2 className="text-2xl font-bold text-slate-800">MindCare AI React Architecture</h2>
          <p className="text-slate-600 text-sm max-w-xl mx-auto">
            You can run this React frontend alongside the Python FastAPI backend, or use the zero-install standalone application in <code className="bg-slate-100 px-2 py-1 rounded">index.html</code>.
          </p>
          <div className="flex justify-center gap-3 pt-2">
            <a 
              href="../index.html" 
              className="px-5 py-2.5 rounded-2xl bg-lavender-600 hover:bg-lavender-700 text-white font-semibold text-xs shadow-md shadow-lavender-200"
            >
              Open Full Standalone Interactive App
            </a>
          </div>
        </div>
      </main>

      {/* Modals */}
      <CrisisModal isOpen={isCrisisModalOpen} onClose={() => setIsCrisisModalOpen(false)} />
    </div>
  );
};

export default App;
