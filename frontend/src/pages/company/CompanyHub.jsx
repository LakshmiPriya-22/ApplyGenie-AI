import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import companyService from "../../services/companyService";

const CompanyHub = () => {
  const [company, setCompany] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!company.trim()) {
      alert("Please enter a company name.");
      return;
    }

    setLoading(true);

    try {
      const response = await companyService.getCompanyDetails(company);
      setResult(response);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch company details.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-6xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Company Hub
        </h1>

        <p className="text-gray-500 mb-6">
          Explore interview experiences, OA questions, hiring process and preparation roadmap.
        </p>

        <div className="flex gap-4">

          <input
            type="text"
            placeholder="Enter Company Name (Google, Amazon...)"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            className="flex-1 border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          />

          <button
            onClick={handleSearch}
            className="bg-cyan-600 hover:bg-cyan-700 text-white px-6 rounded-lg"
          >
            Search
          </button>

        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 mt-8">

          <h2 className="text-xl font-semibold mb-4">
            Company Details
          </h2>

          {loading ? (
            <p>Loading...</p>
          ) : (
            <div className="whitespace-pre-wrap">
              {result || "Search for a company to view details."}
            </div>
          )}

        </div>

      </div>
    </DashboardLayout>
  );
};

export default CompanyHub;