import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import resumeService from "../../services/resumeService";

const ATSAnalysis = () => {
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!jobDescription.trim()) {
      alert("Please enter a Job Description.");
      return;
    }

    setLoading(true);

    try {
      const response = await resumeService.atsAnalysis({
        job_description: jobDescription,
      });

      setResult(response);

    } catch (error) {
      console.error(error);
      alert("Failed to analyze ATS.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>

      <div className="max-w-6xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          ATS Analysis
        </h1>

        <p className="text-gray-500 mb-6">
          Compare your resume with a Job Description.
        </p>

        <textarea
          rows="8"
          placeholder="Paste Job Description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          className="w-full border rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        />

        <button
          onClick={handleAnalyze}
          className="mt-5 bg-cyan-600 hover:bg-cyan-700 text-white px-8 py-3 rounded-lg"
        >
          {loading ? "Analyzing..." : "Analyze ATS"}
        </button>

        <div className="bg-white rounded-xl shadow-lg p-6 mt-8">

          <h2 className="text-xl font-semibold mb-4">
            ATS Report
          </h2>

          <div className="whitespace-pre-wrap">
            {result || "No ATS report available."}
          </div>

        </div>

      </div>

    </DashboardLayout>
  );
};

export default ATSAnalysis;