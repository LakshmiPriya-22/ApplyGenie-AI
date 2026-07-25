import api from "./api";

const notificationService = {

  getNotifications: async () => {
    const response = await api.get("/notifications");
    return response.data;
  },

};

export default notificationService;