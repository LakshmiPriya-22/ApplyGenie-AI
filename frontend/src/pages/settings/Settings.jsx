import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";

const Settings = () => {
  const [emailNotifications, setEmailNotifications] = useState(true);

  return (
    <DashboardLayout>
      <div className="max-w-4xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Settings
        </h1>

        <p className="text-gray-500 mb-8">
          Manage your account settings.
        </p>

        <div className="bg-white rounded-xl shadow-lg p-8 space-y-8">

          <div>

            <h2 className="text-xl font-semibold mb-3">
              Email Notifications
            </h2>

            <label className="flex items-center gap-3">

              <input
                type="checkbox"
                checked={emailNotifications}
                onChange={() =>
                  setEmailNotifications(!emailNotifications)
                }
              />

              Receive internship and job alerts

            </label>

          </div>

          <hr />

          <div>

            <h2 className="text-xl font-semibold mb-3">
              Change Password
            </h2>

            <input
              type="password"
              placeholder="New Password"
              className="border rounded-lg p-3 w-full mb-4"
            />

            <button className="bg-cyan-600 hover:bg-cyan-700 text-white px-6 py-3 rounded-lg">
              Update Password
            </button>

          </div>

          <hr />

          <div>

            <h2 className="text-xl font-semibold mb-3 text-red-600">
              Danger Zone
            </h2>

            <button className="bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-lg">
              Delete Account
            </button>

          </div>

        </div>

      </div>
    </DashboardLayout>
  );
};

export default Settings;