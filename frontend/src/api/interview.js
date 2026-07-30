import api from "./axios";

// -------------------------------------
// Generate Interview
// -------------------------------------
export const generateInterview = async (data) => {
    const response = await api.post(
        "/interviews/generate",
        data
    );

    return response.data;
};

// -------------------------------------
// Get My Interviews
// -------------------------------------
export const getMyInterviews = async () => {
    const response = await api.get(
        "/interviews"
    );

    return response.data;
};

// -------------------------------------
// Get Interview By ID
// -------------------------------------
export const getInterview = async (
    interviewId
) => {
    const response = await api.get(
        `/interviews/${interviewId}`
    );

    return response.data;
};

// -------------------------------------
// Submit Answers
// -------------------------------------
export const submitInterview = async (
    interviewId,
    answers
) => {
    const response = await api.post(
        `/interviews/${interviewId}/submit`,
        {
            answers,
        }
    );

    return response.data;
};

// -------------------------------------
// Delete Interview
// -------------------------------------
export const deleteInterview = async (
    interviewId
) => {
    const response = await api.delete(
        `/interviews/${interviewId}`
    );

    return response.data;
};