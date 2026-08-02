import { Routes, Route } from "react-router-dom";

// Authentication
import Login from "./pages/Login";
import Register from "./pages/Register";

// Dashboard
import Dashboard from "./pages/Dashboard";

// Resume
import ProfileResume from "./pages/profile/ProfileResume";
import ResumeAnalysis from "./pages/resume/ResumeAnalysis";
import ResumeOptimizer from "./pages/resume/ResumeOptimizer";

// Jobs
import JobOpportunities from "./pages/jobs/JobOpportunities";

// Applications
import MyApplications from "./pages/applications/MyApplications";
import JobMatch from "./pages/jobs/JobMatch";

// Interview
import InterviewPrep from "./pages/interview/InterviewPrep";

import ResumeChat from "./pages/resume/ResumeChat";

import Notifications from "./pages/notifications/Notifications";

import Profile from "./pages/profile/Profile";

import Settings from "./pages/settings/Settings";

function App() {
  return (

    <Routes>

      {/* Authentication */}
      <Route path="/" element={<Login />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      {/* Dashboard */}
      <Route
        path="/dashboard"
        element={<Dashboard />}
      />

      {/* Resume */}
      <Route
        path="/profile-resume"
        element={<ProfileResume />}
      />

      <Route
        path="/resume-analysis"
        element={<ResumeAnalysis />}
      />

      <Route
        path="/resume-optimizer"
        element={<ResumeOptimizer />}
      />

      {/* Jobs */}
      <Route
        path="/opportunities"
        element={<JobOpportunities />}
      />

      {/* Applications */}
      <Route
        path="/applications"
        element={<MyApplications />}
      />

      <Route
        path="/job-match"
        element={<JobMatch />}
      />

      <Route
        path="/resume-chat"
        element={<ResumeChat />}
      />



      {/* Interview */}
      <Route
        path="/interview-prep"
        element={<InterviewPrep />}
      />

      <Route
        path="/notifications"
        element={<Notifications />}
      />

      <Route
        path="/settings"
        element={<Settings />}
      />

      <Route
        path="/profile"
        element={<Profile />}
      />
    </Routes>



  );
}

export default App;