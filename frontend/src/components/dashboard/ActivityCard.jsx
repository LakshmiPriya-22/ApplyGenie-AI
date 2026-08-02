import {
  Upload,
  CheckCircle2,
  Bot,
  Mail,
  Clock3,
} from "lucide-react";

const activities = [
  {
    icon: Upload,
    title: "Resume Uploaded",
    desc: "Resume uploaded successfully",
    time: "2 mins ago",
  },
  {
    icon: CheckCircle2,
    title: "ATS Analysis Completed",
    desc: "Resume score updated",
    time: "10 mins ago",
  },
  {
    icon: Bot,
    title: "Interview Generated",
    desc: "10 AI interview questions created",
    time: "30 mins ago",
  },
  {
    icon: Mail,
    title: "Application Email Sent",
    desc: "Email delivered successfully",
    time: "1 hour ago",
  },
];

export default function ActivityCard({
  onViewNotifications,
}) {
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
      <div className="flex justify-between items-center mb-8">

        <div>

          <h2 className="text-2xl font-semibold">
            Recent Activity
          </h2>

          <p className="text-slate-400 mt-1">
            Latest actions in your account
          </p>

        </div>

      </div>

      <div className="space-y-6">

        {activities.map((item, index) => {

          const Icon = item.icon;

          return (

            <div
              key={index}
              className="flex gap-4"
            >

              <div className="w-11 h-11 rounded-full bg-slate-800 flex items-center justify-center">

                <Icon
                  size={18}
                  className="text-blue-500"
                />

              </div>

              <div className="flex-1">

                <h3 className="font-medium">
                  {item.title}
                </h3>

                <p className="text-slate-400 text-sm mt-1">
                  {item.desc}
                </p>

                <div className="flex items-center gap-2 mt-2 text-xs text-slate-500">

                  <Clock3 size={13} />

                  {item.time}

                </div>

              </div>

            </div>

          );

        })}

      </div>

      <button
        onClick={onViewNotifications}
        className="
        mt-8
        w-full
        border
        border-slate-700
        rounded-xl
        py-3
        hover:bg-slate-800
        transition
        cursor-pointer
        "
      >
        View All Activity
      </button>

    </div>
  );
}