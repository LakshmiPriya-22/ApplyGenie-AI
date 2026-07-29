import { NavLink } from "react-router-dom";

const menuItems = [
  {
    name: "Dashboard",
    path: "/dashboard",
    icon: "🏠",
  },
  {
    name: "Profile & Resume",
    path: "/profile-resume",
    icon: "📄",
  },
  {
    name: "Resume Analysis",
    path: "/resume-analysis",
    icon: "📊",
  },
  {
    name: "ATS Analysis",
    path: "/ats-analysis",
    icon: "🎯",
  },
  {
    name: "Resume Optimizer",
    path: "/resume-optimizer",
    icon: "✨",
  },
  {
    name: "Resume Chat",
    path: "/resume-chat",
    icon: "🤖",
  },
  {
    name: "Job Opportunities",
    path: "/opportunities",
    icon: "💼",
  },
  {
    name: "Company Hub",
    path: "/company-hub",
    icon: "🏢",
  },
  {
    name: "Applications",
    path: "/applications",
    icon: "📋",
  },
  {
    name: "Interview Prep",
    path: "/interview-prep",
    icon: "🎤",
  },
  {
    name: "Cover Letter",
    path: "/cover-letter",
    icon: "📝",
  },
  {
    name: "Notifications",
    path: "/notifications",
    icon: "🔔",
  },
  {
    name: "Profile",
    path: "/profile",
    icon: "👤",
  },
  {
    name: "Settings",
    path: "/settings",
    icon: "⚙️",
  },
];

const Sidebar = () => {
  return (
    <aside className="w-72 h-screen bg-slate-900 text-white flex flex-col">

      {/* Logo */}
      <div className="p-6 border-b border-slate-700">
        <h1 className="text-2xl font-bold text-cyan-400">
          ApplyGenie AI
        </h1>

        <p className="text-sm text-slate-400 mt-1">
          AI Placement Assistant
        </p>
      </div>

      {/* Navigation */}
      <nav className="flex-1 overflow-y-auto py-4">

        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center gap-3 px-6 py-3 transition-all duration-200 ${isActive
                ? "bg-cyan-600 text-white border-r-4 border-cyan-300"
                : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            <span className="text-xl">
              {item.icon}
            </span>

            <span className="font-medium">
              {item.name}
            </span>
          </NavLink>
        ))}

      </nav>

      {/* Footer */}
      <div className="border-t border-slate-700 p-5">

        <p className="text-sm text-slate-400">
          Version 1.0
        </p>

        <p className="text-xs text-slate-500 mt-1">
          © 2026 ApplyGenie AI
        </p>

      </div>

    </aside>
  );
};

export default Sidebar;