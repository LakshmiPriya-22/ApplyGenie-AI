import { Link, useLocation } from "react-router-dom";
import {
  LayoutDashboard,
  User,
  FileText,
  Search,
  Briefcase,
  Building2,
  ClipboardList,
  Bell,
  MessageSquare,
  FileCheck,
  Settings,
  LogOut,
  Sparkles,
} from "lucide-react";

export default function Sidebar() {
  const location = useLocation();

  const menuItems = [
    {
      name: "Dashboard",
      icon: <LayoutDashboard size={20} />,
      path: "/dashboard",
    },
    {
      name: "Profile & Resume",
      icon: <User size={20} />,
      path: "/profile-resume",
    },
    {
      name: "Resume Analysis",
      icon: <FileText size={20} />,
      path: "/resume-analysis",
    },
    {
      name: "Resume Optimizer",
      icon: <Sparkles size={20} />,
      path: "/resume-optimizer",
    },
    {
      name: "Job Opportunities",
      icon: <Search size={20} />,
      path: "/opportunities",
    },
    {
      name: "Company Hub",
      icon: <Building2 size={20} />,
      path: "/company-hub",
    },
    {
      name: "Applications",
      icon: <ClipboardList size={20} />,
      path: "/applications",
    },
    {
      name: "Interview Prep",
      icon: <MessageSquare size={20} />,
      path: "/interview-prep",
    },
    {
      name: "Cover Letter",
      icon: <FileCheck size={20} />,
      path: "/cover-letter",
    },
    {
      name: "Notifications",
      icon: <Bell size={20} />,
      path: "/notifications",
    },
    {
      name: "Settings",
      icon: <Settings size={20} />,
      path: "/settings",
    },
    
  ];

  return (
    <aside className="w-72 bg-[#111827] text-white flex flex-col">

      {/* Logo */}
      <div className="p-6 border-b border-slate-700">
        <h1 className="text-2xl font-bold">
          ApplyGenie AI
        </h1>
        <p className="text-sm text-slate-400 mt-1">
          AI Career Assistant
        </p>
      </div>

      {/* Navigation */}
      <nav className="flex-1 px-4 py-6">

        {menuItems.map((item) => (
          <Link
            key={item.path}
            to={item.path}
            className={`flex items-center gap-3 px-4 py-3 rounded-xl mb-2 transition ${
              location.pathname === item.path
                ? "bg-blue-600 text-white"
                : "text-slate-300 hover:bg-slate-800 hover:text-white"
            }`}
          >
            {item.icon}
            <span>{item.name}</span>
          </Link>
        ))}

      </nav>

      {/* Logout */}
      <div className="p-4 border-t border-slate-700">

        <button
          onClick={() => {
            localStorage.removeItem("access_token");
            window.location.href = "/login";
          }}
          className="w-full flex items-center gap-3 px-4 py-3 rounded-xl bg-red-600 hover:bg-red-700 transition"
        >
          <LogOut size={20} />
          Logout
        </button>

      </div>

    </aside>
  );
}