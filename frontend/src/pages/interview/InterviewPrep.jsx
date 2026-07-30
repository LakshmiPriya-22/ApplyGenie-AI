import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";

import { getMyResume } from "../../api/resume";
import { getJobs } from "../../api/jobs";
import {
  generateInterview,
  submitInterview,
} from "../../api/interview";
export default function InterviewPrep() {
  const [resume, setResume] = useState(null);
  const [jobs, setJobs] = useState([]);
  const [selectedJob, setSelectedJob] = useState("");

  const [interviewType, setInterviewType] =
    useState("Technical + HR");

  const [difficulty, setDifficulty] =
    useState("Medium");

  const [interview, setInterview] = useState(null);

  const [answers, setAnswers] = useState({});

  const [loading, setLoading] = useState(true);

  const [generating, setGenerating] =
    useState(false);

  const [submitting, setSubmitting] =
    useState(false);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const resumeData = await getMyResume();
      setResume(resumeData);

      const jobsData = await getJobs();
      setJobs(jobsData);
    } catch (err) {
      console.error(err);
      alert("Unable to load data.");
    } finally {
      setLoading(false);
    }
  };

  const handleGenerate = async () => {
    if (!selectedJob) {
      alert("Please select a job.");
      return;
    }

    try {
      setGenerating(true);

      const data = await generateInterview({
        resume_id: resume.id,
        job_id: Number(selectedJob),
        interview_type: interviewType,
        difficulty: difficulty,
      });

      setInterview(data);
      setAnswers({});
    } catch (err) {
      console.error(err);

      alert(
        err?.response?.data?.detail ||
        "Interview generation failed."
      );
    } finally {
      setGenerating(false);
    }
  };

  const handleAnswerChange = (index, value) => {
    setAnswers((prev) => ({
      ...prev,
      [index]: value,
    }));
  };

  const handleSubmit = async () => {
    const formattedAnswers = interview.questions.map(
      (q, index) => ({
        question: q.question,
        answer: answers[index] || "",
      })
    );

    try {
      setSubmitting(true);

      const result = await submitInterview(
        interview.id,
        formattedAnswers
      );

      console.log(result);

      setInterview({
        ...result
      });

      alert("Interview evaluated successfully.");
    } catch (err) {
      console.error(err);

      alert(
        err?.response?.data?.detail ||
        "Evaluation failed."
      );
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <DashboardLayout>
        <div className="text-center py-20 text-xl">
          Loading Interview Preparation...
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="max-w-6xl mx-auto">

        <h1 className="text-4xl font-bold mb-8">
          AI Interview Preparation
        </h1>

        {/* Resume */}

        <div className="bg-[#111827] rounded-xl p-6 mb-6 shadow">

          <h2 className="text-2xl font-semibold mb-3">
            Selected Resume
          </h2>

          <p className="text-slate-300">
            {resume?.filename}
          </p>

        </div>

        {/* Job Selection */}

        <div className="bg-[#111827] rounded-xl p-6 shadow mb-8">

          <h2 className="text-2xl font-semibold mb-5">
            Interview Settings
          </h2>

          <div className="mb-5">

            <label className="block mb-2 font-medium">
              Select Job
            </label>

            <select
              value={selectedJob}
              onChange={(e) =>
                setSelectedJob(e.target.value)
              }
              className="w-full bg-slate-800 rounded-lg p-3"
            >

              <option value="">
                Choose Job
              </option>

              {jobs.map((job) => (
                <option
                  key={job.id}
                  value={job.id}
                >
                  {job.title} — {job.company}
                </option>
              ))}

            </select>

          </div>

          <div className="grid md:grid-cols-2 gap-5">

            <div>

              <label className="block mb-2 font-medium">
                Interview Type
              </label>

              <select
                value={interviewType}
                onChange={(e) =>
                  setInterviewType(e.target.value)
                }
                className="w-full bg-slate-800 rounded-lg p-3"
              >
                <option>Technical + HR</option>
                <option>Technical</option>
                <option>HR</option>
              </select>

            </div>

            <div>

              <label className="block mb-2 font-medium">
                Difficulty
              </label>

              <select
                value={difficulty}
                onChange={(e) =>
                  setDifficulty(e.target.value)
                }
                className="w-full bg-slate-800 rounded-lg p-3"
              >
                <option>Easy</option>
                <option>Medium</option>
                <option>Hard</option>
              </select>

            </div>

          </div>

          <button
            onClick={handleGenerate}
            disabled={generating}
            className="mt-8 bg-blue-600 hover:bg-blue-700 px-8 py-3 rounded-lg"
          >
            {generating
              ? "Generating Interview..."
              : "Generate Interview"}
          </button>

        </div>
        {/* Interview Details */}

        {interview && (
          <div className="space-y-8">

            {/* Summary */}

            {interview.summary && (
              <div className="bg-[#111827] rounded-xl p-6 shadow">
                <h2 className="text-2xl font-bold mb-4">
                  Interview Summary
                </h2>

                <p className="text-slate-300 leading-7">
                  {interview.summary}
                </p>
              </div>
            )}

            {/* Tips */}

            {interview.tips &&
              interview.tips.length > 0 && (
                <div className="bg-[#111827] rounded-xl p-6 shadow">
                  <h2 className="text-2xl font-bold mb-4">
                    AI Preparation Tips
                  </h2>

                  <ul className="space-y-2 list-disc pl-6">
                    {interview.tips.map((tip, index) => (
                      <li key={index}>
                        {tip}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

            {/* Roadmap */}

            {interview.roadmap &&
              interview.roadmap.length > 0 && (
                <div className="bg-[#111827] rounded-xl p-6 shadow">
                  <h2 className="text-2xl font-bold mb-4">
                    Learning Roadmap
                  </h2>

                  <ol className="space-y-3 list-decimal pl-6">
                    {interview.roadmap.map((step, index) => (
                      <li key={index}>
                        {step}
                      </li>
                    ))}
                  </ol>
                </div>
              )}

            {/* Questions */}

            <div className="bg-[#111827] rounded-xl p-6 shadow">

              <h2 className="text-3xl font-bold mb-8">
                Interview Questions
              </h2>

              {interview.questions.map((question, index) => (

                <div
                  key={index}
                  className="mb-10 border-b border-slate-700 pb-8"
                >

                  <h3 className="text-xl font-semibold">

                    Q{index + 1}. {question.question}

                  </h3>

                  <p className="text-cyan-400 mt-2">

                    Category :
                    {" "}
                    {question.category}

                  </p>

                  <textarea
                    rows={6}
                    value={answers[index] || ""}
                    placeholder="Type your answer..."
                    onChange={(e) =>
                      handleAnswerChange(
                        index,
                        e.target.value
                      )
                    }
                    className="w-full mt-4 bg-slate-800 rounded-lg p-4 outline-none"
                  />

                </div>

              ))}

              {!interview.feedback && (
                <button
                  onClick={handleSubmit}
                  disabled={submitting}
                  className="bg-green-600 hover:bg-green-700 px-8 py-3 rounded-lg"
                >
                  {submitting
                    ? "Evaluating..."
                    : "Submit Answers"}
                </button>
              )}

            </div>

            {/* Evaluation */}

            {interview.feedback && (

              <div className="bg-[#111827] rounded-xl p-6 shadow">

                <h2 className="text-3xl font-bold mb-6">
                  AI Evaluation
                </h2>

                {/* Score */}

                <div className="mb-8">

                  <h3 className="text-xl font-semibold">
                    Overall Score
                  </h3>

                  <div className="w-full bg-slate-700 rounded-full h-5 mt-4">

                    <div
                      className="bg-green-500 h-5 rounded-full"
                      style={{
                        width: `${interview.score}%`,
                      }}
                    />

                  </div>

                  <p className="text-4xl font-bold text-green-400 mt-4">

                    {interview.score}/100

                  </p>

                </div>

                {/* Feedback */}

                {interview.feedback.overall_feedback && (
                  <div className="mb-8">
                    <h3 className="text-xl font-bold mb-3">
                      Overall Feedback
                    </h3>

                    <p className="text-slate-300 leading-7">
                      {interview.feedback.overall_feedback}
                    </p>
                  </div>
                )}

                {/* Strengths */}

                {interview.feedback.strengths && (
                  <div className="mb-8">
                    <h3 className="text-green-400 text-xl font-bold mb-3">
                      Strengths
                    </h3>

                    <ul className="list-disc pl-6 space-y-2">
                      {interview.feedback.strengths.map(
                        (item, index) => (
                          <li key={index}>
                            {item}
                          </li>
                        )
                      )}
                    </ul>
                  </div>
                )}

                {/* Weaknesses */}

                {interview.feedback.weaknesses && (
                  <div className="mb-8">
                    <h3 className="text-red-400 text-xl font-bold mb-3">
                      Areas to Improve
                    </h3>

                    <ul className="list-disc pl-6 space-y-2">
                      {interview.feedback.weaknesses.map(
                        (item, index) => (
                          <li key={index}>
                            {item}
                          </li>
                        )
                      )}
                    </ul>
                  </div>
                )}

                {/* Suggestions */}

                {interview.feedback.suggestions && (
                  <div>

                    <h3 className="text-cyan-400 text-xl font-bold mb-3">
                      Suggestions
                    </h3>

                    <ul className="list-disc pl-6 space-y-2">
                      {interview.feedback.suggestions.map(
                        (item, index) => (
                          <li key={index}>
                            {item}
                          </li>
                        )
                      )}
                    </ul>

                  </div>
                )}

              </div>

            )}

          </div>
        )}

      </div>

    </DashboardLayout>
  );
}