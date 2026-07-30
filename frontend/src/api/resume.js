import api from "./axios";

// Upload Resume
export const uploadResume = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post(
    "/resume/upload",
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

// Get latest uploaded resume
export const getMyResume = async () => {
  const response = await api.get("/resume");

  const resumes = response.data;

  if (!resumes || resumes.length === 0) {
    return null;
  }

  // return the latest resume
  return resumes[0];
};

// Get all resumes
export const getAllResumes = async () => {
  const response = await api.get("/resume");
  return response.data;
};

// Delete resume
export const deleteResume = async (id) => {
  const response = await api.delete(`/resume/${id}`);
  return response.data;
};