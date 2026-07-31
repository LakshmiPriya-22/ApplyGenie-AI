import { useEffect, useState } from "react";
import { Bell, Search, UserCircle } from "lucide-react";
import { useNavigate } from "react-router-dom";
import notificationService from "../../services/notificationService";

const Navbar = () => {
  const navigate = useNavigate();

  const [unreadCount, setUnreadCount] = useState(0);

  useEffect(() => {
    loadUnreadCount();

    // Refresh every 10 seconds
    const interval = setInterval(loadUnreadCount, 10000);

    return () => clearInterval(interval);
  }, []);

  const loadUnreadCount = async () => {
    try {
      const data = await notificationService.getUnreadCount();

      // Supports either { unread: 3 } or { count: 3 }
      setUnreadCount(data.unread ?? data.count ?? 0);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <header className="h-16 bg-white border-b border-gray-200 flex items-center justify-between px-6 shadow-sm">

      {/* Search */}
      <div className="flex items-center bg-gray-100 rounded-lg px-3 py-2 w-96">

        <Search
          size={18}
          className="text-gray-500"
        />

        <input
          type="text"
          placeholder="Search..."
          className="bg-transparent outline-none ml-2 w-full text-sm"
        />

      </div>

      {/* Right Section */}
      <div className="flex items-center gap-6">

        {/* Notification Bell */}
        <button
          onClick={() => navigate("/notifications")}
          className="relative"
        >

          <Bell
            size={22}
            className="text-gray-600 hover:text-cyan-600 cursor-pointer"
          />

          {unreadCount > 0 && (
            <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full h-5 min-w-[20px] px-1 flex items-center justify-center">
              {unreadCount}
            </span>
          )}

        </button>

        {/* User */}
        <div className="flex items-center gap-3">

          <UserCircle
            size={38}
            className="text-cyan-600"
          />

          <div>

            <h3 className="font-semibold">
              Renuka
            </h3>

            <p className="text-xs text-gray-500">
              Student
            </p>

          </div>

        </div>

      </div>

    </header>
  );
};

export default Navbar;