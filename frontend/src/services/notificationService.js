import api from "./api";

const notificationService = {

  // Get all notifications
  getNotifications: async () => {
    const response = await api.get("/notifications");
    return response.data;
  },

  // Get unread notification count
  getUnreadCount: async () => {
    const response = await api.get("/notifications/count");
    return response.data;
  },

  // Mark a notification as read
  markAsRead: async (id) => {
    const response = await api.put(`/notifications/${id}/read`);
    return response.data;
  },

  // Mark all notifications as read
  markAllAsRead: async () => {
    const response = await api.put("/notifications/read-all");
    return response.data;
  },

  // Delete a notification
  deleteNotification: async (id) => {
    const response = await api.delete(`/notifications/${id}`);
    return response.data;
  },

};

export default notificationService;