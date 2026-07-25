import api from "./api";

const resumeService = {

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

};

export default resumeService;