import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import { getMyResume } from "../../api/resume";
import { optimizeResume } from "../../api/resumeOptimizer";

export default function ResumeOptimizer() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadResume();
  }, []);

  const loadResume = async () => {
    try {
      const data = await getMyResume();
      setResume(data);
    } catch (err) {
      console.log(err);
    }
  };

  const handleOptimize = async () => {
    if (!resume) {
      alert("Upload a resume first.");
      return;
    }

    if (!jobDescription.trim()) {
      alert("Enter a job description.");
      return;
    }

    try {
      setLoading(true);

      const data = await optimizeResume(
        resume.id,
        jobDescription
      );

      setResult(data);

    } catch (err) {
      console.log(err);
      alert("Optimization failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-8">
        Resume Optimizer
      </h1>

      <div className="bg-[#111827] rounded-2xl p-8">

        <textarea
          rows={10}
          placeholder="Paste Job Description..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          className="w-full p-4 rounded-xl bg-slate-800 border border-slate-700"
        />

        <button
          onClick={handleOptimize}
          className="mt-6 bg-blue-600 px-6 py-3 rounded-xl"
        >
          {loading ? "Optimizing..." : "Optimize Resume"}
        </button>

      </div>

      {result && (
        <div className="bg-[#111827] rounded-2xl p-8 mt-8 space-y-8">

          <div>
            <h2 className="text-2xl font-semibold">ATS Score</h2>
            <h1 className="text-6xl text-green-500">
              {result.ats_score}%
            </h1>
          </div>

          <div>
            <h2 className="text-2xl font-semibold mb-3">
              Professional Summary
            </h2>
            <p>{result.summary}</p>
          </div>

          <div>
            <h2 className="text-2xl font-semibold mb-3">
              Skills
            </h2>

            <div className="flex flex-wrap gap-2">
              {result.skills?.map((skill) => (
                <span
                  key={skill}
                  className="bg-blue-600 px-3 py-1 rounded-full"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>

          <div>
            <h2 className="text-2xl font-semibold mb-3">
              Missing Skills
            </h2>

            <div className="flex flex-wrap gap-2">
              {result.missing_skills?.map((skill) => (
                <span
                  key={skill}
                  className="bg-red-600 px-3 py-1 rounded-full"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>

          <div>
            <h2 className="text-2xl font-semibold mb-3">
              Suggestions
            </h2>

            <ul className="list-disc ml-6 space-y-2">
              {result.suggestions?.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>

          <div>
            <h2 className="text-2xl font-semibold mb-3">
              Projects
            </h2>

            {result.projects?.map((project, index) => (
              <div
                key={index}
                className="bg-slate-800 rounded-xl p-4 mb-4"
              >
                <h3 className="font-bold">
                  {project.title}
                </h3>

                <p className="mt-2">
                  {project.description}
                </p>

                <p className="text-blue-400 mt-2">
                  {project.technologies}
                </p>
              </div>
            ))}
          </div>

        </div>
      )}

    </DashboardLayout>
  );
}