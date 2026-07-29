import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import DashboardLayout from "../../components/layout/DashboardLayout";

import { getJobs, discoverJobs } from "../../api/jobs";
import { getMyResume } from "../../api/resume";
import { matchResume } from "../../api/jobMatch";
import { applyJob } from "../../api/application";

export default function JobOpportunities() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  useEffect(() => {
    loadJobs();
  }, []);

  const loadJobs = async () => {
    try {
      const data = await getJobs();
      setJobs(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleDiscover = async () => {
    try {
      await discoverJobs();
      alert("Jobs discovered successfully!");
      loadJobs();
    } catch (err) {
      console.error(err);
      alert("Job discovery failed.");
    }
  };

  const handleMatchResume = async (jobId) => {
    try {
      const resume = await getMyResume();

      const result = await matchResume(
        resume.id,
        jobId
      );

      navigate("/job-match", {
        state: {
          match: result,
        },
      });

    } catch (err) {
      console.error(err);
      alert("Failed to match resume.");
    }
  };

  const handleApply = async (jobId) => {
    try {
      const resume = await getMyResume();

      await applyJob(
        resume.id,
        jobId
      );

      alert("Application submitted successfully!");

    } catch (err) {
      console.error(err);

      if (err.response?.data?.detail) {
        alert(err.response.data.detail);
      } else {
        alert("Unable to apply for this job.");
      }
    }
  };

  return (
    <DashboardLayout>

      <div className="flex justify-between items-center mb-8">

        <h1 className="text-4xl font-bold">
          Job Opportunities
        </h1>

        <button
          onClick={handleDiscover}
          className="bg-blue-600 hover:bg-blue-700 px-5 py-3 rounded-xl"
        >
          Discover Jobs
        </button>

      </div>

      {loading ? (
        <h2>Loading Jobs...</h2>
      ) : jobs.length === 0 ? (
        <h2>No Jobs Found</h2>
      ) : (

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {jobs.map((job) => (

            <div
              key={job.id}
              className="bg-[#111827] rounded-2xl p-6"
            >

              <h2 className="text-2xl font-bold">
                {job.title}
              </h2>

              <p className="text-slate-400 mt-2">
                {job.company}
              </p>

              <p className="mt-2">
                📍 {job.location}
              </p>

              <p>
                💼 {job.employment_type}
              </p>

              <p>
                ⭐ {job.experience_level}
              </p>

              <div className="flex gap-3 mt-6">

                <button
                  onClick={() => handleMatchResume(job.id)}
                  className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded-xl"
                >
                  Match Resume
                </button>

                <button
                  onClick={() => handleApply(job.id)}
                  className="bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded-xl"
                >
                  Apply Job
                </button>

              </div>

            </div>

          ))}

        </div>

      )}

    </DashboardLayout>
  );
}