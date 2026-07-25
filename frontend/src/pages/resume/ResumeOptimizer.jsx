import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import resumeService from "../../services/resumeService";

const ResumeOptimizer = () => {
  const [jobDescription, setJobDescription] = useState("");
  const [optimizedResume, setOptimizedResume] = useState("");
  const [loading, setLoading] = useState(false);

  const handleOptimize = async () => {
    if (!jobDescription.trim()) {
      alert("Please enter a Job Description.");
      return;
    }

    setLoading(true);

    try {
      const response = await resumeService.resumeOptimizer({
        job_description: jobDescription,
      });

      setOptimizedResume(response);

    } catch (error) {
      console.error(error);
      alert("Failed to optimize resume.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-6xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Resume Optimizer
        </h1>

        <p className="text-gray-500 mb-6">
          Generate an ATS-optimized resume based on the Job Description.
        </p>

        <textarea
          rows="8"
          placeholder="Paste Job Description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          className="w-full border rounded-lg p-4 focus:outline-none focus:ring-2 focus:ring-cyan-500"
        />

        <button
          onClick={handleOptimize}
          className="mt-5 bg-cyan-600 hover:bg-cyan-700 text-white px-8 py-3 rounded-lg"
        >
          {loading ? "Optimizing..." : "Optimize Resume"}
        </button>

        <div className="bg-white rounded-xl shadow-lg p-6 mt-8">

          <h2 className="text-xl font-semibold mb-4">
            Optimized Resume
          </h2>

          <div className="whitespace-pre-wrap">
            {optimizedResume || "No optimized resume generated."}
          </div>

        </div>

      </div>
    </DashboardLayout>
  );
};

export default ResumeOptimizer;