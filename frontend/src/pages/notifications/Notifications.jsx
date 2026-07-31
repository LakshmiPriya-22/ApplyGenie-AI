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

  const handleRead = async (id) => {
    try {
      await notificationService.markAsRead(id);
      fetchNotifications();
    } catch (error) {
      console.error(error);
    }
  };

  const handleReadAll = async () => {
    try {
      await notificationService.markAllAsRead();
      fetchNotifications();
    } catch (error) {
      console.error(error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await notificationService.deleteNotification(id);
      fetchNotifications();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <DashboardLayout>
      <div className="max-w-6xl mx-auto">

        <div className="flex justify-between items-center mb-8">

          <div>
            <h1 className="text-3xl font-bold">
              Notifications
            </h1>

            <p className="text-gray-500 mt-2">
              Stay updated with jobs, interviews and placement activities.
            </p>
          </div>

          <button
            onClick={handleReadAll}
            className="bg-cyan-600 hover:bg-cyan-700 text-white px-5 py-2 rounded-lg"
          >
            Mark All Read
          </button>

        </div>

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
                className={`rounded-xl shadow-md p-6 border-l-4 ${notification.is_read
                    ? "bg-gray-100 border-gray-400"
                    : "bg-white border-cyan-500"
                  }`}
              >

                <div className="flex justify-between">

                  <div className="flex-1">

                    <h2 className="text-xl font-semibold">
                      {notification.title}
                    </h2>

                    <p className="text-gray-600 mt-2">
                      {notification.message}
                    </p>

                    <div className="mt-3 text-sm text-gray-500">
                      {new Date(notification.created_at).toLocaleString()}
                    </div>

                    <div className="mt-2">

                      <span
                        className={`text-sm font-semibold ${notification.is_read
                            ? "text-green-600"
                            : "text-red-600"
                          }`}
                      >
                        {notification.is_read ? "Read" : "Unread"}
                      </span>

                    </div>

                  </div>

                  <div className="flex flex-col gap-2">

                    {!notification.is_read && (

                      <button
                        onClick={() => handleRead(notification.id)}
                        className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-lg"
                      >
                        Read
                      </button>

                    )}

                    <button
                      onClick={() => handleDelete(notification.id)}
                      className="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg"
                    >
                      Delete
                    </button>

                  </div>

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