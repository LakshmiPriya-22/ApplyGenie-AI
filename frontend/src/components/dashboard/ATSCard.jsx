import { FileCheck } from "lucide-react";

export default function ATSCard({
  onImproveResume,
  onViewAnalysis,
}) {
  return (
    <div
      className="
      bg-[#111827]
      border
      border-slate-700
      rounded-2xl
      p-8
      h-full
      hover:border-blue-500
      transition-all
      duration-300
      "
    >
      <div className="flex justify-between items-center">

        <div>

          <p className="text-slate-400 text-sm">
            ATS Resume Score
          </p>

          <h1 className="text-6xl font-bold mt-3">
            92%
          </h1>

        </div>

        {/* Resume Analysis Button */}
        <button
          onClick={onViewAnalysis}
          className="
          w-16
          h-16
          rounded-2xl
          bg-blue-600
          flex
          items-center
          justify-center
          hover:bg-blue-700
          transition
          cursor-pointer
          "
          title="View Resume Analysis"
        >
          <FileCheck size={28} />
        </button>

      </div>

      <div className="mt-10">

        <div className="flex justify-between text-sm text-slate-400 mb-3">

          <span>Resume Strength</span>

          <span>92%</span>

        </div>

        <div className="h-3 rounded-full bg-slate-800 overflow-hidden">

          <div className="h-full w-[92%] rounded-full bg-blue-500" />

        </div>

      </div>

      <p className="mt-6 text-slate-400 leading-7">

        Your resume performs better than

        <span className="text-blue-500 font-semibold">
          {" "}84%
        </span>

        {" "}of candidates based on ATS analysis.

      </p>

      <button
        onClick={onImproveResume}
        className="
        mt-8
        bg-blue-600
        hover:bg-blue-700
        px-5
        py-3
        rounded-xl
        font-medium
        transition
        cursor-pointer
        "
      >
        Improve Resume
      </button>

    </div>
  );
}