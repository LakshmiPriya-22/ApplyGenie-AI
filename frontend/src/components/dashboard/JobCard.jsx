import {
  MapPin,
  ArrowRight,
  Building2,
} from "lucide-react";

export default function JobCard({
  company,
  role,
  location,
  match,
  onClick,
}) {
  return (
    <div
      className="
      bg-[#111827]
      border
      border-slate-700
      rounded-2xl
      p-6
      hover:border-blue-500
      hover:-translate-y-1
      transition-all
      duration-300
      cursor-pointer
      "
      onClick={onClick}
    >
      <div className="flex justify-between items-start">

        <div className="flex gap-4">

          <div className="w-14 h-14 rounded-xl bg-slate-800 flex items-center justify-center">

            <Building2
              className="text-blue-500"
              size={22}
            />

          </div>

          <div>

            <h2 className="font-semibold text-lg">
              {company}
            </h2>

            <p className="text-slate-400">
              {role}
            </p>

            <div className="flex items-center gap-2 mt-3 text-slate-500 text-sm">

              <MapPin size={15} />

              {location}

            </div>

          </div>

        </div>

        <div className="bg-green-500/20 text-green-400 px-3 py-1 rounded-full text-sm font-semibold">

          {match}

        </div>

      </div>

      <div className="flex justify-between items-center mt-8">

        <button
          onClick={(e) => {
            e.stopPropagation();
            onClick();
          }}
          className="
          bg-blue-600
          hover:bg-blue-700
          px-5
          py-2.5
          rounded-xl
          transition
          font-medium
          "
        >
          Apply Now
        </button>

        <button
          onClick={(e) => {
            e.stopPropagation();
            onClick();
          }}
          className="flex items-center gap-2 text-blue-400 hover:text-blue-300"
        >
          View

          <ArrowRight size={16} />

        </button>

      </div>

    </div>
  );
}