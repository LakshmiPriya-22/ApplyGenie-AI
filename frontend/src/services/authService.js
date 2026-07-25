import api from "./api";

const authService = {
  register: async (userData) => {
    const response = await api.post("/auth/register", userData);
    return response.data;
  },

  login: async (credentials) => {
    const response = await api.post("/auth/login", credentials);

    localStorage.setItem(
      "access_token",
      response.data.access_token
    );

    return response.data;
  },

  logout: () => {
    localStorage.removeItem("access_token");
  },

  getCurrentUser: async () => {
    const response = await api.get("/auth/me");
    return response.data;
  },
};

export default authService;