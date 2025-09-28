"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/react";
import { ChevronDown, Wallet, Cpu, Bot, Settings, Layers, Radar, Code2 } from "lucide-react";

const dummyData = [
  { name: "BTC", value: 12000 },
  { name: "ETH", value: 8500 },
  { name: "SOL", value: 4300 },
];

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState("chat");

  return (
    <div className="flex h-screen">
      {/* Left Sidebar */}
      <aside className="w-64 glass-bg flex flex-col p-4 space-y-6">
        <motion.div
          initial={{ opacity: 0, x: -40 }}
          animate={{ opacity: 1, x: 0 }}
          className="text-neonblue text-xl font-bold tracking-wide"
        >
          ♾ Infinity UI
        </motion.div>

        <nav className="space-y-3">
          <button
            className={`w-full text-left px-3 py-2 rounded-md border border-silver hover:text-neonblue ${
              activeTab === "chat" ? "bg-glass text-neonblue" : "text-white"
            }`}
            onClick={() => setActiveTab("chat")}
          >
            Chat
          </button>

          <button
            className={`w-full text-left px-3 py-2 rounded-md border border-silver hover:text-neonblue ${
              activeTab === "finance" ? "bg-glass text-neonblue" : "text-white"
            }`}
            onClick={() => setActiveTab("finance")}
          >
            Financial Dashboard
          </button>

          <button
            className={`w-full text-left px-3 py-2 rounded-md border border-silver hover:text-neonblue ${
              activeTab === "agents" ? "bg-glass text-neonblue" : "text-white"
            }`}
            onClick={() => setActiveTab("agents")}
          >
            Agents
          </button>

          <button
            className={`w-full text-left px-3 py-2 rounded-md border border-silver hover:text-neonblue ${
              activeTab === "swarm" ? "bg-glass text-neonblue" : "text-white"
            }`}
            onClick={() => setActiveTab("swarm")}
          >
            Swarm
          </button>

          <button
            className={`w-full text-left px-3 py-2 rounded-md border border-silver hover:text-neonblue ${
              activeTab === "codex" ? "bg-glass text-neonblue" : "text-white"
            }`}
            onClick={() => setActiveTab("codex")}
          >
            Codex Mode
          </button>

          <button
            className={`w-full text-left px-3 py-2 rounded-md border border-silver hover:text-neonblue ${
              activeTab === "scraper" ? "bg-glass text-neonblue" : "text-white"
            }`}
            onClick={() => setActiveTab("scraper")}
          >
            Scraper
          </button>

          <button
            className={`w-full text-left px-3 py-2 rounded-md border border-silver hover:text-neonblue ${
              activeTab === "admin" ? "bg-glass text-neonblue" : "text-white"
            }`}
            onClick={() => setActiveTab("admin")}
          >
            Super Admin
          </button>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 p-6 overflow-y-auto">
        {/* Top Bar */}
        <div className="flex justify-between items-center mb-6">
          {/* Model Dropdown */}
          <Menu as="div" className="relative">
            <MenuButton className="px-3 py-2 border border-silver rounded-md text-white hover:text-neonblue flex items-center">
              Model Selector <ChevronDown className="ml-2 h-4 w-4" />
            </MenuButton>
            <MenuItems className="absolute mt-2 w-48 glass-bg rounded-md shadow-lg">
              <MenuItem>
                <button className="w-full px-4 py-2 text-left hover:text-neonblue">
                  Groq Mixtral
                </button>
              </MenuItem>
              <MenuItem>
                <button className="w-full px-4 py-2 text-left hover:text-neonblue">
                  GPT-4 Limitless
                </button>
              </MenuItem>
              <MenuItem>
                <button className="w-full px-4 py-2 text-left hover:text-neonblue">
                  Custom Model
                </button>
              </MenuItem>
            </MenuItems>
          </Menu>

          {/* Account Dropdown */}
          <Menu as="div" className="relative">
            <MenuButton className="px-3 py-2 border border-silver rounded-md text-white hover:text-neonblue flex items-center">
              Accounts <ChevronDown className="ml-2 h-4 w-4" />
            </MenuButton>
            <MenuItems className="absolute right-0 mt-2 w-48 glass-bg rounded-md shadow-lg">
              <MenuItem>
                <a href="https://supabase.com" className="block px-4 py-2 hover:text-neonblue">
                  Supabase
                </a>
              </MenuItem>
              <MenuItem>
                <a href="https://vercel.com" className="block px-4 py-2 hover:text-neonblue">
                  Vercel
                </a>
              </MenuItem>
              <MenuItem>
                <a href="https://cloud.google.com" className="block px-4 py-2 hover:text-neonblue">
                  Google Cloud
                </a>
              </MenuItem>
              <MenuItem>
                <a href="https://github.com" className="block px-4 py-2 hover:text-neonblue">
                  GitHub
                </a>
              </MenuItem>
            </MenuItems>
          </Menu>
        </div>

        {/* Dynamic Tab Rendering */}
        {activeTab === "chat" && (
          <div className="space-y-4">
            <div className="glass-bg p-4 rounded-lg border border-silver">
              <p className="text-silver">Chat with Infinity Agent...</p>
            </div>
          </div>
        )}

        {activeTab === "finance" && (
          <div className="glass-bg p-6 rounded-lg border border-silver">
            <h2 className="text-xl text-neonblue mb-4">Financial Dashboard</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={dummyData}>
                <XAxis dataKey="name" stroke="#b0b0b0" />
                <YAxis stroke="#b0b0b0" />
                <Tooltip />
                <Bar dataKey="value" fill="#00e5ff" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}

        {activeTab === "admin" && (
          <div className="glass-bg p-6 rounded-lg border border-silver">
            <h2 className="text-xl text-neonblue mb-4">System Overview</h2>
            <p className="text-silver">
              View and edit backend settings, API keys, UI themes, and more.
            </p>
          </div>
        )}
      </main>
    </div>
  );
}
