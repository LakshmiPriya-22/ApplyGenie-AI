import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import coverLetterService from "../../services/coverLetterService";

const CoverLetter = () => {
  const [company, setCompany] = useState("");
  const [role, setRole] = useState("");
  const [coverLetter, setCoverLetter] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!company || !role) {
      alert("Please enter company and role.");
      return;
    }

    setLoading(true);

    try {
      const response = await coverLetterService.generateCoverLetter({
        company,
        role,
      });

      setCoverLetter(response);
    } catch (error) {
      console.error(error);
      alert("Failed to generate cover letter.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-6xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Cover Letter Generator
        </h1>

        <p className="text-gray-500 mb-6">
          Generate a personalized cover letter for any company.
        </p>

        <div className="grid md:grid-cols-2 gap-4">

          <input
            type="text"
            placeholder="Company Name"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            className="border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          />

          <input
            type="text"
            placeholder="Job Role"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          />

        </div>

        <button
          onClick={handleGenerate}
          className="mt-6 bg-cyan-600 hover:bg-cyan-700 text-white px-8 py-3 rounded-lg"
        >
          {loading ? "Generating..." : "Generate Cover Letter"}
        </button>

        <div className="bg-white rounded-xl shadow-lg p-6 mt-8">

          <h2 className="text-xl font-semibold mb-4">
            Generated Cover Letter
          </h2>

          <div className="whitespace-pre-wrap">
            {coverLetter || "Your generated cover letter will appear here."}
          </div>

        </div>

      </div>
    </DashboardLayout>
  );
};

export default CoverLetter;