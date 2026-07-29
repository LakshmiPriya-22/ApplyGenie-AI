import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Register from "./pages/Register";

import Dashboard from "./pages/Dashboard";

import ProfileResume from "./pages/profile/ProfileResume";
import ResumeAnalysis from "./pages/resume/ResumeAnalysis";
//import ATSAnalysis from "./pages/resume/ATSAnalysis";
import ResumeOptimizer from "./pages/resume/ResumeOptimizer";
//import ResumeChat from "./pages/resume/ResumeChat";
//import CoverLetter from "./pages/resume/CoverLetter";

import JobOpportunities from "./pages/jobs/JobOpportunities";
//import CompanyHub from "./pages/jobs/CompanyHub";

import MyApplications from "./pages/applications/MyApplications";

import InterviewPrep from "./pages/interview/InterviewPrep";

//import Notifications from "./pages/notifications/Notifications";

//import Profile from "./pages/profile/Profile";
//import Settings from "./pages/settings/Settings";

function App() {
  return (
    <BrowserRouter>

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
          path="/ats-analysis"
          element={<ATSAnalysis />}
        />

        <Route
          path="/resume-optimizer"
          element={<ResumeOptimizer />}
        />

        <Route
          path="/resume-chat"
          element={<ResumeChat />}
        />

        <Route
          path="/cover-letter"
          element={<CoverLetter />}
        />

        {/* Jobs */}

        <Route
          path="/opportunities"
          element={<JobOpportunities />}
        />

        <Route
          path="/company-hub"
          element={<CompanyHub />}
        />

        {/* Applications */}

        <Route
          path="/applications"
          element={<MyApplications />}
        />

        {/* Interview */}

        <Route
          path="/interview-prep"
          element={<InterviewPrep />}
        />

        {/* Notifications */}

        <Route
          path="/notifications"
          element={<Notifications />}
        />

        {/* User */}

        <Route
          path="/profile"
          element={<Profile />}
        />

        <Route
          path="/settings"
          element={<Settings />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;