import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import applicationService from "../../services/applicationService";

const ApplicationTracker = () => {
  const [applications, setApplications] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchApplications();
  }, []);

  const fetchApplications = async () => {
    setLoading(true);

    try {
      const response = await applicationService.getApplications();
      setApplications(response);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch applications.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-7xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Application Tracker
        </h1>

        <p className="text-gray-500 mb-8">
          Track all your internship and job applications.
        </p>

        <div className="bg-white rounded-xl shadow-lg overflow-hidden">

          <table className="w-full">

            <thead className="bg-cyan-600 text-white">

              <tr>
                <th className="p-4 text-left">Company</th>
                <th className="p-4 text-left">Role</th>
                <th className="p-4 text-left">Applied On</th>
                <th className="p-4 text-left">Status</th>
                <th className="p-4 text-left">Match</th>
              </tr>

            </thead>

            <tbody>

              {loading ? (

                <tr>
                  <td colSpan="5" className="p-6 text-center">
                    Loading...
                  </td>
                </tr>

              ) : applications.length === 0 ? (

                <tr>
                  <td colSpan="5" className="p-6 text-center">
                    No Applications Found
                  </td>
                </tr>

              ) : (

                applications.map((app) => (

                  <tr
                    key={app.id}
                    className="border-b hover:bg-gray-50"
                  >

                    <td className="p-4">
                      {app.company}
                    </td>

                    <td className="p-4">
                      {app.role}
                    </td>

                    <td className="p-4">
                      {app.applied_date}
                    </td>

                    <td className="p-4">

                      <span
                        className={`px-3 py-1 rounded-full text-sm text-white ${
                          app.status === "Applied"
                            ? "bg-blue-500"
                            : app.status === "Interview"
                            ? "bg-orange-500"
                            : app.status === "Selected"
                            ? "bg-green-500"
                            : "bg-red-500"
                        }`}
                      >
                        {app.status}
                      </span>

                    </td>

                    <td className="p-4">
                      {app.match_score}%
                    </td>

                  </tr>

                ))

              )}

            </tbody>

          </table>

        </div>

      </div>
    </DashboardLayout>
  );
};

export default ApplicationTracker;