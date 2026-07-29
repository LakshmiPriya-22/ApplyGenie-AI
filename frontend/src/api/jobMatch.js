import api from "./axios";

export const matchResume = async (resumeId, jobId) => {
  const response = await api.post(
    `/matches/jobs/${jobId}/resume/${resumeId}`
  );

  return response.data;
};

export const getResumeMatches = async (resumeId) => {
  const response = await api.get(
    `/matches/resume/${resumeId}`
  );

  return response.data;
};

export const deleteMatch = async (matchId) => {
  const response = await api.delete(
    `/matches/${matchId}`
  );

  return response.data;
};