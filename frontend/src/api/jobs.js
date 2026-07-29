import api from "./axios";

export const getJobs = async () => {
  const response = await api.get("/jobs");
  return response.data;
};

export const discoverJobs = async () => {
  const response = await api.post("/jobs/discover");
  return response.data;
};