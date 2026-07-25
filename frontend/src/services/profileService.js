import api from "./api";

const profileService = {
  // Get student profile
  getProfile: async () => {
    const response = await api.get("/profile");
    return response.data;
  },

  // Create profile
  createProfile: async (profileData) => {
    const response = await api.post("/profile", profileData);
    return response.data;
  },

  // Update profile
  updateProfile: async (profileData) => {
    const response = await api.put("/profile", profileData);
    return response.data;
  },

  // Upload resume
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

export default profileService;