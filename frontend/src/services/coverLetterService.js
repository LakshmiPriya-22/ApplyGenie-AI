import api from "./api";

const coverLetterService = {

  generateCoverLetter: async (data) => {
    const response = await api.post(
      "/resume/cover-letter",
      data
    );

    return response.data;
  },

};

export default coverLetterService;