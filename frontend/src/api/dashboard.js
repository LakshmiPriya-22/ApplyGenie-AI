import api from "./axios";

export const getProfile = async () => {
  const response = await api.get("/auth/me");
  return response.data;
};

export const getDashboard = async () => {
  const response = await api.get("/dashboard");
  return response.data;
};