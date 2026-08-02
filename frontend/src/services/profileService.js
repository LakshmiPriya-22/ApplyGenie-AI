import api from "./api";

const profileService = {

  getProfile: async () => {
    const response = await api.get("/profile/");
    return response.data;
  },

  createProfile: async (data) => {
    const response = await api.post("/profile/", data);
    return response.data;
  },

  updateProfile: async (data) => {
    const response = await api.put("/profile/", data);
    return response.data;
  },

  uploadPhoto: async (formData) => {
    const response = await api.post(
      "/profile/photo",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    return response.data;
  },

  deletePhoto: async () => {
    const response = await api.delete("/profile/photo");
    return response.data;
  },

};

export default profileService;