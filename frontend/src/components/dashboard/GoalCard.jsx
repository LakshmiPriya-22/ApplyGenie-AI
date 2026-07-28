import { Target } from "lucide-react";

export default function GoalCard() {
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

        <h2 className="text-2xl font-semibold">

          Weekly Goals

        </h2>

        <Target
          size={28}
          className="text-blue-500"
        />

      </div>

      {/* Applications */}

      <div className="mt-10">

        <div className="flex justify-between text-sm">

          <span className="text-slate-400">

            Applications

          </span>

          <span>

            12 / 20

          </span>

        </div>

        <div className="mt-3 h-3 rounded-full bg-slate-800 overflow-hidden">

          <div className="h-full w-[60%] rounded-full bg-green-500" />

        </div>

      </div>

      {/* Interviews */}

      <div className="mt-8">

        <div className="flex justify-between text-sm">

          <span className="text-slate-400">

            Interviews

          </span>

          <span>

            3 / 5

          </span>

        </div>

        <div className="mt-3 h-3 rounded-full bg-slate-800 overflow-hidden">

          <div className="h-full w-[65%] rounded-full bg-yellow-500" />

        </div>

      </div>

      {/* Resume */}

      <div className="mt-8">

        <div className="flex justify-between text-sm">

          <span className="text-slate-400">

            Resume Updates

          </span>

          <span>

            1 / 2

          </span>

        </div>

        <div className="mt-3 h-3 rounded-full bg-slate-800 overflow-hidden">

          <div className="h-full w-[50%] rounded-full bg-purple-500" />

        </div>

      </div>

      <button
        className="
        mt-10
        bg-blue-600
        hover:bg-blue-700
        px-5
        py-3
        rounded-xl
        transition
        font-medium
        "
      >
        View Goals
      </button>

    </div>
  );
}