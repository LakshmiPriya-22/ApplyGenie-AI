import api from "./api";

const resumeService = {

  // --------------------------
  // Upload Resume
  // --------------------------
  uploadResume: async (formData) => {

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
  },

  // --------------------------
  // Get My Resumes
  // --------------------------
  getResumes: async () => {

    const response = await api.get("/resume");

    return response.data;
  },

  // --------------------------
  // Resume Chat
  // --------------------------
  resumeChat: async (data) => {

    const response = await api.post(
      "/resume-chat/",
      data
    );

    return response.data;
  },

};

export default resumeService;