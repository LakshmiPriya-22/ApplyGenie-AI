import api from "./axios";

export const getResumeAnalysis = async (resumeId) => {
  const response = await api.get(`/analysis/${resumeId}`);
  return response.data;
};