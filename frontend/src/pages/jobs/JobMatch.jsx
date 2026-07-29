import { useLocation, useNavigate } from "react-router-dom";
import DashboardLayout from "../../components/layout/DashboardLayout";

export default function JobMatch() {
  const { state } = useLocation();
  const navigate = useNavigate();

  const match = state?.match;

  if (!match) {
    return (
      <DashboardLayout>
        <div className="flex flex-col items-center justify-center h-[70vh]">
          <h1 className="text-3xl font-bold mb-4">
            No Match Result Found
          </h1>

          <button
            onClick={() => navigate("/opportunities")}
            className="bg-blue-600 px-5 py-3 rounded-xl hover:bg-blue-700"
          >
            Back to Jobs
          </button>
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <h1 className="text-4xl font-bold mb-8">
        AI Job Match
      </h1>

      <div className="bg-[#111827] rounded-2xl p-8 space-y-8">

        {/* Match Score */}
        <div>
          <h2 className="text-2xl font-semibold">
            Match Score
          </h2>

          <h1 className="text-6xl text-green-500 mt-3">
            {match.match_score}%
          </h1>
        </div>

        {/* Summary */}
        <div>
          <h2 className="text-2xl font-semibold mb-3">
            Summary
          </h2>

          <p className="text-slate-300 leading-7">
            {match.summary}
          </p>
        </div>

        {/* Strengths */}
        <div>
          <h2 className="text-2xl font-semibold mb-3">
            Strengths
          </h2>

          <ul className="space-y-2">
            {match.strengths?.map((item, index) => (
              <li key={index}>
                ✅ {item}
              </li>
            ))}
          </ul>
        </div>

        {/* Missing Skills */}
        <div>
          <h2 className="text-2xl font-semibold mb-3">
            Missing Skills
          </h2>

          <ul className="space-y-2">
            {match.missing_skills?.map((item, index) => (
              <li key={index}>
                ❌ {item}
              </li>
            ))}
          </ul>
        </div>

        {/* Recommendations */}
        <div>
          <h2 className="text-2xl font-semibold mb-3">
            Recommendations
          </h2>

          <ul className="space-y-2">
            {match.recommendations?.map((item, index) => (
              <li key={index}>
                💡 {item}
              </li>
            ))}
          </ul>
        </div>

        <div className="pt-4">
          <button
            onClick={() => navigate("/opportunities")}
            className="bg-blue-600 px-5 py-3 rounded-xl hover:bg-blue-700"
          >
            Back to Jobs
          </button>
        </div>

      </div>
    </DashboardLayout>
  );
}