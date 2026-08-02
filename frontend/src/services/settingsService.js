import api from "./api";

const settingsService = {

    // -----------------------------
    // Get Settings
    // -----------------------------
    getSettings: async () => {

        const response = await api.get("/settings/");

        return response.data;
    },

    // -----------------------------
    // Update Settings
    // -----------------------------
    updateSettings: async (data) => {

        const response = await api.put(
            "/settings/",
            data
        );

        return response.data;
    },

    // -----------------------------
    // Change Password
    // -----------------------------
    changePassword: async (data) => {

        const response = await api.put(
            "/settings/change-password",
            data
        );

        return response.data;
    },

    // -----------------------------
    // Delete Account
    // -----------------------------
    deleteAccount: async () => {

        const response = await api.delete(
            "/settings/account"
        );

        return response.data;
    }

};

export default settingsService;