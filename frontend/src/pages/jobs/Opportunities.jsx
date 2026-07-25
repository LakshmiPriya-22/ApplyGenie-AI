import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import jobService from "../../services/jobService";

const Opportunities = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchJobs();
  }, []);

  const fetchJobs = async () => {
    setLoading(true);

    try {
      const response = await jobService.getJobs();
      setJobs(response);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch opportunities.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Job Opportunities
        </h1>

        <p className="text-gray-500 mb-8">
          Explore internships and job opportunities matched to your profile.
        </p>

        {loading ? (
          <p>Loading...</p>
        ) : jobs.length === 0 ? (
          <div className="bg-white rounded-xl shadow-md p-8 text-center">
            No opportunities available.
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">

            {jobs.map((job) => (

              <div
                key={job.id}
                className="bg-white rounded-xl shadow-md p-6 hover:shadow-xl transition"
              >

                <h2 className="text-xl font-bold">
                  {job.role}
                </h2>

                <p className="text-cyan-600 font-medium mt-1">
                  {job.company}
                </p>

                <p className="text-gray-500 mt-3">
                  📍 {job.location}
                </p>

                <p className="text-gray-500">
                  🎓 {job.eligibility}
                </p>

                <p className="text-gray-500">
                  ⏰ Deadline: {job.deadline}
                </p>

                <div className="mt-5">

                  <p className="font-semibold">
                    Match Score
                  </p>

                  <div className="w-full bg-gray-200 rounded-full h-3 mt-2">

                    <div
                      className="bg-green-500 h-3 rounded-full"
                      style={{
                        width: `${job.match_score}%`,
                      }}
                    ></div>

                  </div>

                  <p className="text-sm mt-2">
                    {job.match_score}%
                  </p>

                </div>

                <button
                  className="mt-6 w-full bg-cyan-600 hover:bg-cyan-700 text-white py-2 rounded-lg"
                >
                  View Details
                </button>

              </div>

            ))}

          </div>
        )}

      </div>
    </DashboardLayout>
  );
};

export default Opportunities;