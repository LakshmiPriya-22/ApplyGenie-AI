import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import resumeService from "../../services/resumeService";

const ResumeAnalysis = () => {
  const [analysis, setAnalysis] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchAnalysis();
  }, []);

  const fetchAnalysis = async () => {
    setLoading(true);

    try {
      const response = await resumeService.resumeAnalysis();

      setAnalysis(response);

    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>

      <div className="max-w-6xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Resume Analysis
        </h1>

        <p className="text-gray-500 mb-8">
          AI-generated analysis of your resume.
        </p>

        <div className="bg-white rounded-xl shadow-lg p-8">

          {loading ? (
            <p className="text-center">
              Analyzing Resume...
            </p>
          ) : (
            <div className="prose max-w-none whitespace-pre-wrap">
              {analysis || "No analysis available."}
            </div>
          )}

        </div>

      </div>

    </DashboardLayout>
  );
};

export default ResumeAnalysis;