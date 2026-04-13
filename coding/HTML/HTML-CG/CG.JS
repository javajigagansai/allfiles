import React from 'react';
import { 
  Plus, Search, Image, LayoutGrid, Code, Briefcase, 
  MessageSquare, ChevronDown, Mic, Send, UserCircle 
} from 'lucide-react';

const ChatGPTClone = () => {
  return (
    <div className="flex h-screen w-full bg-white text-gray-800 font-sans">
      
      {/* Sidebar */}
      <aside className="w-64 border-r border-gray-200 flex flex-col p-4 space-y-6">
        <div className="flex items-center justify-between mb-2">
          <div className="p-1 hover:bg-gray-100 rounded-lg cursor-pointer">
            <LayoutGrid size={20} />
          </div>
        </div>

        <nav className="flex-1 space-y-1">
          <SidebarItem icon={<Plus size={18} />} label="New chat" />
          <SidebarItem icon={<Search size={18} />} label="Search chats" />
          <SidebarItem icon={<Image size={18} />} label="Images" />
          <SidebarItem icon={<LayoutGrid size={18} />} label="Apps" />
          <SidebarItem icon={<Code size={18} />} label="Codex" />
          <SidebarItem icon={<Briefcase size={18} />} label="Projects" />

          <div className="pt-4 pb-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">GPTs</div>
          <SidebarItem icon={<div className="w-5 h-5 bg-orange-100 rounded flex items-center justify-center text-[10px]">∑</div>} label="Math Solver" />
          <SidebarItem icon={<LayoutGrid size={18} />} label="Explore GPTs" />

          <div className="pt-4 pb-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">Group chats</div>
          <SidebarItem icon={<MessageSquare size={18} />} label="New group chat" />
        </nav>

        {/* User Profile Section */}
        <div className="border-t border-gray-100 pt-4">
          <div className="flex items-center justify-between p-2 hover:bg-gray-100 rounded-xl cursor-pointer">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center text-xs font-bold text-white">SK</div>
              <div className="text-sm">
                <p className="font-semibold leading-none">Gagan Sai</p>
                <p className="text-gray-400 text-xs mt-1">Free</p>
              </div>
            </div>
            <button className="text-xs font-medium border border-gray-300 px-3 py-1 rounded-full hover:bg-white">Upgrade</button>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col relative">
        {/* Top Header */}
        <header className="p-4 flex justify-between items-center">
          <div className="flex items-center gap-1 cursor-pointer hover:bg-gray-100 p-2 rounded-lg">
            <span className="font-medium">ChatGPT</span>
            <ChevronDown size={16} />
          </div>
          
          <div className="flex items-center gap-4">
            <button className="bg-indigo-50 text-indigo-600 px-4 py-1.5 rounded-full text-sm font-medium flex items-center gap-2">
              <span className="text-indigo-400">✦</span> Get Plus
            </button>
            <UserCircle size={24} className="text-gray-400" />
          </div>
        </header>

        {/* Center Prompt Area */}
        <div className="flex-1 flex flex-col items-center justify-center px-4">
          <h1 className="text-4xl font-semibold mb-8 text-gray-700">What are you working on?</h1>
          
          <div className="w-full max-w-3xl relative">
            <div className="flex items-center bg-gray-50 border border-gray-200 rounded-3xl p-4 shadow-sm focus-within:border-gray-300 transition-all">
              <Plus size={20} className="text-gray-400 mr-3 cursor-pointer" />
              <input 
                type="text" 
                placeholder="Ask anything" 
                className="flex-1 bg-transparent outline-none text-lg text-gray-600"
              />
              <div className="flex items-center gap-4 text-gray-400">
                <Mic size={20} className="cursor-pointer hover:text-gray-600" />
                <div className="bg-orange-500 p-2 rounded-full text-white cursor-pointer hover:bg-orange-600">
                  <Send size={18} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

const SidebarItem = ({ icon, label }) => (
  <div className="flex items-center gap-3 p-2 hover:bg-gray-100 rounded-xl cursor-pointer text-gray-600 group">
    <div className="text-gray-500 group-hover:text-black">{icon}</div>
    <span className="text-sm font-medium">{label}</span>
  </div>
);

export default ChatGPTClone;