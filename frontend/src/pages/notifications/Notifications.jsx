import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import notificationService from "../../services/notificationService";

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchNotifications();
  }, []);

  const fetchNotifications = async () => {
    setLoading(true);

    try {
      const response = await notificationService.getNotifications();
      setNotifications(response);
    } catch (error) {
      console.error(error);
      alert("Failed to load notifications.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-6xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Notifications
        </h1>

        <p className="text-gray-500 mb-8">
          Stay updated with jobs, deadlines and placement activities.
        </p>

        {loading ? (
          <div className="bg-white rounded-xl shadow-md p-6">
            Loading...
          </div>
        ) : notifications.length === 0 ? (
          <div className="bg-white rounded-xl shadow-md p-6 text-center">
            No Notifications Available
          </div>
        ) : (
          <div className="space-y-5">

            {notifications.map((notification) => (

              <div
                key={notification.id}
                className="bg-white rounded-xl shadow-md p-6 border-l-4 border-cyan-500"
              >

                <div className="flex justify-between">

                  <div>

                    <h2 className="text-xl font-semibold">
                      {notification.title}
                    </h2>

                    <p className="text-gray-600 mt-2">
                      {notification.message}
                    </p>

                  </div>

                  <span className="text-sm text-gray-500">
                    {notification.date}
                  </span>

                </div>

              </div>

            ))}

          </div>
        )}

      </div>
    </DashboardLayout>
  );
};

export default Notifications;