import api from "./axios";

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

export const getMyResume = async () => {
  const response = await api.get("/resume/me");
  return response.data;
};

export const deleteResume = async (id) => {
  const response = await api.delete(`/resume/${id}`);
  return response.data;
};