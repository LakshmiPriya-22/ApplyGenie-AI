import api from "./axios";

export const optimizeResume = async (resumeId, jobDescription) => {
  const response = await api.post("/resume-optimizer/", {
    resume_id: resumeId,
    job_description: jobDescription,
  });

  return response.data;
};