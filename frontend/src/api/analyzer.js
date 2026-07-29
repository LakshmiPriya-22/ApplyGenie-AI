import api from "./axios";

export const getLatestAnalysis = async () => {
  const response = await api.get("/analyzer/latest");
  return response.data;
};