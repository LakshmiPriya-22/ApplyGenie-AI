import api from "./axios";

export const askResume = async (question) => {
    
    const response = await api.post("/resume-chat/", {
        question,
    });

    return response.data;
};
