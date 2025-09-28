"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";

const TABS = [
  { key: "supabase_logs", label: "Supabase Logs" },
  { key: "gpt_memory", label: "GPT Memory" },
  { key: "infinity_memory", label: "Infinity Agent Memory" },
  { key: "github_status", label: "GitHub Deployments" },
  { key: "google_cloud_status", label: "Google Cloud Nodes" },
  { key: "guardian_logs", label: "Guardian Logs" },
  { key: "vercel_status", label: "Vercel Deployments" },
];

export default function Dashboard() {
  const [data, setData] = useState({});
  const [activeTab, setActiveTab] = useState("supabase_logs");
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      setLoading(true);
      const res = await axios.get(process.env.NEXT_PUBLIC_DASHBOARD_API);
      setData(res.data);
    } catch (err) {
      console.error("Error fetching dashboard data:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 5000); // refresh every 5 sec
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="p-6 bg-gray-900 text-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6 text-blue-400">
        Infinity System Dashboard
      </h1>

      {/* Tabs */}
      <div className="flex space-x-4 border-b border-gray-700 mb-4">
        {TABS.map((tab) => (
          <button
            key={tab.key}
            onClick={() => setActiveTab(tab.key)}
            className={`px-4 py-2 ${
              activeTab === tab.key
                ? "border-b-2 border-blue-500 text-blue-400"
                : "text-gray-400 hover:text-white"
            }`}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Content */}
      <div className="bg-gray-800 p-4 rounded-lg shadow">
        {loading ? (
          <p className="text-gray-400">Loading...</p>
        ) : (
          <pre className="text-sm overflow-x-auto">
            {JSON.stringify(data[activeTab], null, 2)}
          </pre>
        )}
      </div>
    </div>
  );
}
