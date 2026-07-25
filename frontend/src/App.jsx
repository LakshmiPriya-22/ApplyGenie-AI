import { Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import Dashboard from "./pages/dashboard/Dashboard";

import ProfileResume from "./pages/profile/ProfileResume";
import Profile from "./pages/profile/Profile";

import ResumeAnalysis from "./pages/resume/ResumeAnalysis";
import ATSAnalysis from "./pages/resume/ATSAnalysis";
import ResumeOptimizer from "./pages/resume/ResumeOptimizer";
import ResumeChat from "./pages/resume/ResumeChat";

import Opportunities from "./pages/jobs/Opportunities";
import CompanyHub from "./pages/company/CompanyHub";
import ApplicationTracker from "./pages/applications/ApplicationTracker";
import Notifications from "./pages/notifications/Notifications";
import InterviewPrep from "./pages/interview/InterviewPrep";
import CoverLetter from "./pages/coverletter/CoverLetter";
import Settings from "./pages/settings/Settings";

import ProtectedRoute from "./routes/ProtectedRoute";

function App() {
  return (
    <Routes>

      <Route path="/" element={<Navigate to="/login" />} />

      <Route path="/login" element={<Login />} />

      <Route path="/register" element={<Register />} />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      <Route path="/profile-resume" element={<ProtectedRoute><ProfileResume /></ProtectedRoute>} />

      <Route path="/resume-analysis" element={<ProtectedRoute><ResumeAnalysis /></ProtectedRoute>} />

      <Route path="/ats-analysis" element={<ProtectedRoute><ATSAnalysis /></ProtectedRoute>} />

      <Route path="/resume-optimizer" element={<ProtectedRoute><ResumeOptimizer /></ProtectedRoute>} />

      <Route path="/resume-chat" element={<ProtectedRoute><ResumeChat /></ProtectedRoute>} />

      <Route path="/opportunities" element={<ProtectedRoute><Opportunities /></ProtectedRoute>} />

      <Route path="/company-hub" element={<ProtectedRoute><CompanyHub /></ProtectedRoute>} />

      <Route path="/applications" element={<ProtectedRoute><ApplicationTracker /></ProtectedRoute>} />

      <Route path="/notifications" element={<ProtectedRoute><Notifications /></ProtectedRoute>} />

      <Route path="/interview-prep" element={<ProtectedRoute><InterviewPrep /></ProtectedRoute>} />

      <Route path="/cover-letter" element={<ProtectedRoute><CoverLetter /></ProtectedRoute>} />

      <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />

      <Route path="/settings" element={<ProtectedRoute><Settings /></ProtectedRoute>} />

    </Routes>
  );
}

export default App;