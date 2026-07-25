import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import interviewService from "../../services/interviewService";

const InterviewPrep = () => {
  const [company, setCompany] = useState("");
  const [questions, setQuestions] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!company.trim()) {
      alert("Please enter a company name.");
      return;
    }

    setLoading(true);

    try {
      const response = await interviewService.getInterviewPrep({
        company: company,
      });

      setQuestions(response);

    } catch (error) {
      console.error(error);
      alert("Failed to fetch interview preparation.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-6xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Interview Preparation
        </h1>

        <p className="text-gray-500 mb-6">
          Get interview questions and preparation roadmap.
        </p>

        <div className="flex gap-4">

          <input
            type="text"
            placeholder="Enter Company Name"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            className="flex-1 border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          />

          <button
            onClick={handleGenerate}
            className="bg-cyan-600 hover:bg-cyan-700 text-white px-6 rounded-lg"
          >
            Generate
          </button>

        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 mt-8">

          <h2 className="text-xl font-semibold mb-4">
            AI Interview Preparation
          </h2>

          {loading ? (
            <p>Generating...</p>
          ) : (
            <div className="whitespace-pre-wrap">
              {questions || "No interview preparation generated."}
            </div>
          )}

        </div>

      </div>
    </DashboardLayout>
  );
};

export default InterviewPrep;