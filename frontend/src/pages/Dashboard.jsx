import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import DashboardLayout from "../components/layout/DashboardLayout";

import ATSCard from "../components/dashboard/ATSCard";
import GoalCard from "../components/dashboard/GoalCard";
import InterviewCard from "../components/dashboard/InterviewCard";
import JobCard from "../components/dashboard/JobCard";
import ActivityCard from "../components/dashboard/ActivityCard";

import { getProfile } from "../api/dashboard";

function Dashboard() {

  const navigate = useNavigate();

  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadProfile();
  }, []);

  const loadProfile = async () => {

    try {

      const data = await getProfile();

      setUser(data);

    } catch (err) {

      console.error(err);

    } finally {

      setLoading(false);

    }

  };

  return (

    <DashboardLayout>

      {/* HERO */}

      <div className="mb-10">

        <h1 className="text-4xl font-bold">

          {loading
            ? "Loading..."
            : `Good Evening, ${user?.email} 👋`
          }

        </h1>

        <p className="text-slate-400 mt-2">

          Track your applications, interviews and AI recommendations.

        </p>

      </div>

      {/* TOP CARDS */}

      <div className="grid lg:grid-cols-2 gap-6">

        <ATSCard
          onImproveResume={() => navigate("/resume-optimizer")}
          onViewAnalysis={() => navigate("/resume-analysis")}
        />

        <GoalCard
          onViewGoals={() => navigate("/applications")}
        />

      </div>

      {/* Interview */}

      <div className="mt-6">

        <InterviewCard
          onViewSchedule={() => navigate("/interview-prep")}
        />

      </div>

      {/* Bottom Section */}

      <div className="grid lg:grid-cols-2 gap-6 mt-6">

        {/* Jobs */}

        <div>

          <h2 className="text-2xl font-semibold mb-5">

            Recommended Jobs

          </h2>

          <div className="space-y-5">

            <JobCard
              company="Google"
              role="Software Engineer"
              location="Hyderabad"
              match="94% Match"
              onClick={() => navigate("/jobs")}
            />

            <JobCard
              company="Microsoft"
              role="Backend Engineer"
              location="Bengaluru"
              match="91% Match"
              onClick={() => navigate("/jobs")}
            />

            <JobCard
              company="Amazon"
              role="SDE Intern"
              location="Chennai"
              match="89% Match"
              onClick={() => navigate("/jobs")}
            />

          </div>

        </div>

        {/* Activity */}

        <ActivityCard
          onViewNotifications={() => navigate("/notifications")}
        />

      </div>

    </DashboardLayout>

  );

}

export default Dashboard;