import api from "./api";

const companyService = {
  getCompanyDetails: async (companyName) => {
    const response = await api.post("/company/search", {
      company: companyName,
    });

    return response.data;
  },
};

export default companyService;