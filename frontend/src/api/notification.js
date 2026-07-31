import api from "./axios";

// Get all notifications
export const getNotifications = async () => {
    const response = await api.get("/notifications");
    return response.data;
};

// Get unread count
export const getUnreadCount = async () => {
    const response = await api.get("/notifications/count");
    return response.data;
};

// Mark one as read
export const markAsRead = async (id) => {
    const response = await api.put(`/notifications/${id}/read`);
    return response.data;
};

// Mark all as read
export const markAllAsRead = async () => {
    const response = await api.put("/notifications/read-all");
    return response.data;
};

// Delete notification
export const deleteNotification = async (id) => {
    const response = await api.delete(`/notifications/${id}`);
    return response.data;
};