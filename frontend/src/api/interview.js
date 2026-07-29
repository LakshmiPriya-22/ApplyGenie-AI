import api from "./axios";

// -------------------------------------
// Generate Interview
// -------------------------------------
export const generateInterview = async (
    resumeId,
    jobId,
    interviewType = "Technical + HR",
    difficulty = "Medium"
) => {
    try {
        const { data } = await api.post("/interviews/generate", {
            resume_id: resumeId,
            job_id: jobId,
            interview_type: interviewType,
            difficulty,
        });

        return data;
    } catch (error) {
        console.error("Generate Interview Error:", error);
        throw error;
    }
};

// -------------------------------------
// Submit Answers
// -------------------------------------
export const submitInterviewAnswers = async (
    interviewId,
    answers
) => {
    try {
        const { data } = await api.post(
            `/interviews/${interviewId}/submit`,
            {
                answers,
            }
        );

        return data;
    } catch (error) {
        console.error("Submit Interview Error:", error);
        throw error;
    }
};

// -------------------------------------
// Get My Interviews
// -------------------------------------
export const getMyInterviews = async () => {
    try {
        const { data } = await api.get("/interviews");
        return data;
    } catch (error) {
        console.error("Get Interviews Error:", error);
        throw error;
    }
};

// -------------------------------------
// Get Interview By ID
// -------------------------------------
export const getInterview = async (interviewId) => {
    try {
        const { data } = await api.get(
            `/interviews/${interviewId}`
        );

        return data;
    } catch (error) {
        console.error("Get Interview Error:", error);
        throw error;
    }
};

// -------------------------------------
// Delete Interview
// -------------------------------------
export const deleteInterview = async (interviewId) => {
    try {
        const { data } = await api.delete(
            `/interviews/${interviewId}`
        );

        return data;
    } catch (error) {
        console.error("Delete Interview Error:", error);
        throw error;
    }
};