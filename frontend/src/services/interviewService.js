import api from "./api";

const interviewService = {

  getInterviewPrep: async (data) => {
    const response = await api.post(
      "/resume/interview-questions",
      data
    );

    return response.data;
  },

};

export default interviewService;