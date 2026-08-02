import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import settingsService from "../../services/settingsService";

const Settings = () => {

  const [settings, setSettings] = useState({
    email_notifications: true,
    job_notifications: true,
    interview_notifications: true,
    theme: "dark"
  });

  const [password, setPassword] = useState({
    current_password: "",
    new_password: ""
  });

  useEffect(() => {
    loadSettings();
  }, []);

  const loadSettings = async () => {

    try {

      const data = await settingsService.getSettings();

      setSettings(data);

    } catch (error) {

      console.error(error);

    }

  };

  const handleUpdate = async () => {

    try {

      await settingsService.updateSettings(settings);

      alert("Settings Updated Successfully");

    } catch (error) {

      console.error(error);

      alert("Failed to update settings.");

    }

  };

  const handlePassword = async () => {

    try {

      await settingsService.changePassword(password);

      alert("Password Changed");

      setPassword({
        current_password: "",
        new_password: ""
      });

    } catch (error) {

      console.error(error);

      alert("Failed to change password.");

    }

  };

  const handleDelete = async () => {

    const confirmDelete = window.confirm(
      "Delete your account permanently?"
    );

    if (!confirmDelete) return;

    try {

      await settingsService.deleteAccount();

      alert("Account Deleted");

      localStorage.removeItem("token");

      window.location.href = "/login";

    } catch (error) {

      console.error(error);

    }

  };

  return (

    <DashboardLayout>

      <div className="max-w-5xl mx-auto">

        <h1 className="text-3xl font-bold mb-8">
          Settings
        </h1>

        <div className="bg-[#111827] rounded-xl p-8 space-y-8">

          {/* Notifications */}

          <div>

            <h2 className="text-xl font-semibold mb-4">
              Notifications
            </h2>

            <label className="flex items-center gap-3 mb-3">

              <input
                type="checkbox"
                checked={settings.email_notifications}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    email_notifications: e.target.checked
                  })
                }
              />

              Email Notifications

            </label>

            <label className="flex items-center gap-3 mb-3">

              <input
                type="checkbox"
                checked={settings.job_notifications}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    job_notifications: e.target.checked
                  })
                }
              />

              Job Notifications

            </label>

            <label className="flex items-center gap-3">

              <input
                type="checkbox"
                checked={settings.interview_notifications}
                onChange={(e) =>
                  setSettings({
                    ...settings,
                    interview_notifications: e.target.checked
                  })
                }
              />

              Interview Notifications

            </label>

          </div>

          {/* Theme */}

          <div>

            <h2 className="text-xl font-semibold mb-3">

              Theme

            </h2>

            <select
              value={settings.theme}
              onChange={(e) =>
                setSettings({
                  ...settings,
                  theme: e.target.value
                })
              }
              className="bg-gray-800 rounded-lg p-3"
            >

              <option value="dark">Dark</option>

              <option value="light">Light</option>

            </select>

          </div>

          {/* Password */}

          <div>

            <h2 className="text-xl font-semibold mb-3">

              Change Password

            </h2>

            <input
              type="password"
              placeholder="Current Password"
              className="w-full bg-gray-800 rounded-lg p-3 mb-3"
              value={password.current_password}
              onChange={(e) =>
                setPassword({
                  ...password,
                  current_password: e.target.value
                })
              }
            />

            <input
              type="password"
              placeholder="New Password"
              className="w-full bg-gray-800 rounded-lg p-3"
              value={password.new_password}
              onChange={(e) =>
                setPassword({
                  ...password,
                  new_password: e.target.value
                })
              }
            />

            <button
              onClick={handlePassword}
              className="mt-4 bg-cyan-600 px-6 py-2 rounded-lg"
            >
              Change Password
            </button>

          </div>

          {/* Save */}

          <button
            onClick={handleUpdate}
            className="bg-green-600 px-8 py-3 rounded-lg"
          >
            Save Settings
          </button>

          {/* Delete */}

          <div className="border-t border-gray-700 pt-8">

            <h2 className="text-red-500 text-xl font-semibold mb-4">

              Danger Zone

            </h2>

            <button
              onClick={handleDelete}
              className="bg-red-600 px-8 py-3 rounded-lg"
            >
              Delete Account
            </button>

          </div>

        </div>

      </div>

    </DashboardLayout>

  );

};

export default Settings;