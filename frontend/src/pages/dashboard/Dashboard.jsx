import DashboardLayout from "../../components/layout/DashboardLayout";
import StatsCard from "../../components/dashboard/StatsCard";
import QuickAction from "../../components/dashboard/QuickAction";

const Dashboard = () => {
  return (
    <DashboardLayout>

      {/* Heading */}

      <div className="mb-8">

        <h1 className="text-3xl font-bold">
          Welcome Renuka 👋
        </h1>

        <p className="text-gray-500 mt-2">
          Manage your placements with AI.
        </p>

      </div>

      {/* Stats */}

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

        <StatsCard
          title="Resume Uploaded"
          value="Yes"
          icon="📄"
          color="text-blue-500"
        />

        <StatsCard
          title="ATS Score"
          value="84%"
          icon="🎯"
          color="text-green-500"
        />

        <StatsCard
          title="Applications"
          value="12"
          icon="💼"
          color="text-purple-500"
        />

        <StatsCard
          title="Interview Prep"
          value="Ready"
          icon="🎤"
          color="text-orange-500"
        />

      </div>

      {/* Quick Actions */}

      <div className="mt-10">

        <h2 className="text-2xl font-semibold mb-5">
          Quick Actions
        </h2>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-5">

          <QuickAction
            title="Upload Resume"
            icon="📄"
            onClick={() => {}}
          />

          <QuickAction
            title="Resume Chat"
            icon="🤖"
            onClick={() => {}}
          />

          <QuickAction
            title="Generate PDF"
            icon="📥"
            onClick={() => {}}
          />

          <QuickAction
            title="Optimize Resume"
            icon="✨"
            onClick={() => {}}
          />

        </div>

      </div>

      {/* Recent Activity */}

      <div className="bg-white rounded-xl shadow-md mt-10 p-6">

        <h2 className="text-2xl font-semibold mb-4">
          Recent Activity
        </h2>

        <ul className="space-y-3 text-gray-600">

          <li>✅ Resume uploaded successfully.</li>

          <li>✅ ATS Analysis completed.</li>

          <li>✅ Resume optimized.</li>

          <li>✅ Cover Letter generated.</li>

        </ul>

      </div>

    </DashboardLayout>
  );
};

export default Dashboard;