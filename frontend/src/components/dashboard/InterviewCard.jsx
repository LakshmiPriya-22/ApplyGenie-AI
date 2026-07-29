import {
  CalendarDays,
  Clock3,
  Building2,
} from "lucide-react";

const interviews = [
  {
    company: "Google",
    role: "Software Engineer",
    date: "Tomorrow",
    time: "10:00 AM",
  },
  {
    company: "Microsoft",
    role: "Backend Engineer",
    date: "Friday",
    time: "2:30 PM",
  },
  {
    company: "Amazon",
    role: "SDE Intern",
    date: "Monday",
    time: "11:30 AM",
  },
];

export default function InterviewCard() {
  return (
    <div
      className="
      bg-[#111827]
      border
      border-slate-700
      rounded-2xl
      p-8
      hover:border-blue-500
      transition-all
      duration-300
      "
    >
      {/* Header */}

      <div className="flex items-center justify-between">

        <div>

          <h2 className="text-2xl font-semibold">

            Upcoming Interviews

          </h2>

          <p className="text-slate-400 mt-1">

            Your scheduled interview sessions

          </p>

        </div>

        <div className="w-14 h-14 rounded-xl bg-blue-600 flex items-center justify-center">

          <CalendarDays size={26} />

        </div>

      </div>

      {/* List */}

      <div className="mt-8 space-y-5">

        {interviews.map((item) => (

          <div
            key={item.company}
            className="
            flex
            justify-between
            items-center
            bg-[#1E293B]
            border
            border-slate-700
            rounded-xl
            p-5
            hover:border-blue-500
            transition
            "
          >

            {/* Left */}

            <div className="flex gap-4 items-center">

              <div className="w-12 h-12 rounded-full bg-slate-800 flex items-center justify-center">

                <Building2
                  size={20}
                  className="text-blue-400"
                />

              </div>

              <div>

                <h3 className="font-semibold">

                  {item.company}

                </h3>

                <p className="text-slate-400">

                  {item.role}

                </p>

              </div>

            </div>

            {/* Right */}

            <div className="text-right">

              <div className="text-blue-400 font-medium">

                {item.date}

              </div>

              <div className="flex items-center justify-end gap-2 mt-2 text-slate-400 text-sm">

                <Clock3 size={14} />

                {item.time}

              </div>

            </div>

          </div>

        ))}

      </div>

      {/* Button */}

      <button
        className="
        mt-8
        w-full
        bg-blue-600
        hover:bg-blue-700
        py-3
        rounded-xl
        font-medium
        transition
        "
      >
        View Interview Schedule
      </button>

    </div>
  );
}