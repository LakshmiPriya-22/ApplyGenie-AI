import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";

import {
    getMyApplications,
    withdrawApplication,
} from "../../api/application";

export default function MyApplications() {
    const [applications, setApplications] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadApplications();
    }, []);

    const loadApplications = async () => {
        try {
            const data = await getMyApplications();
            console.log(data);
            setApplications(data);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleWithdraw = async (id) => {
        if (!window.confirm("Withdraw this application?")) return;

        try {
            await withdrawApplication(id);
            alert("Application withdrawn successfully.");
            loadApplications();
        } catch (err) {
            console.error(err);
            alert("Unable to withdraw application.");
        }
    };

    return (
        <DashboardLayout>
            <div className="flex justify-between items-center mb-8">
                <h1 className="text-4xl font-bold">
                    My Applications
                </h1>
            </div>

            {loading ? (
                <h2>Loading...</h2>
            ) : applications.length === 0 ? (
                <h2>No Applications Found</h2>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {applications.map((application) => (
                        <div
                            key={application.id}
                            className="bg-[#111827] rounded-2xl p-6"
                        >
                            <h2 className="text-2xl font-bold">
                                {application.job?.title || `Job #${application.job_id}`}
                            </h2>

                            <p className="text-slate-400 mt-2">
                                {application.job?.company}
                            </p>

                            <p className="mt-2">
                                📍 {application.job?.location}
                            </p>

                            <p className="mt-2">
                                💼 {application.job?.employment_type}
                            </p>

                            <p className="mt-4">
                                Resume ID : {application.resume_id}
                            </p>

                            <p className="mt-2">
                                Status :
                                <span
                                    className={`ml-2 font-semibold ${application.status === "Applied"
                                            ? "text-green-400"
                                            : application.status === "Rejected"
                                                ? "text-red-400"
                                                : application.status === "Interview"
                                                    ? "text-yellow-400"
                                                    : application.status === "Offer"
                                                        ? "text-cyan-400"
                                                        : "text-white"
                                        }`}
                                >
                                    {application.status}
                                </span>
                            </p>

                            <p className="mt-2 text-sm text-slate-400">
                                Applied :
                                {" "}
                                {new Date(
                                    application.applied_at
                                ).toLocaleDateString()}
                            </p>

                            {application.notes && (
                                <p className="mt-3 text-slate-300">
                                    Notes : {application.notes}
                                </p>
                            )}

                            <button
                                onClick={() =>
                                    handleWithdraw(application.id)
                                }
                                className="mt-5 bg-red-600 hover:bg-red-700 px-5 py-2 rounded-xl"
                            >
                                Withdraw
                            </button>
                        </div>
                    ))}
                </div>
            )}
        </DashboardLayout>
    );
}