import api from "./axios";

// Apply for a Job
export const applyJob = async (resumeId, jobId) => {
    const response = await api.post("/applications", {
        resume_id: resumeId,
        job_id: jobId,
    });

    return response.data;
};

// Get My Applications
export const getMyApplications = async () => {
    const response = await api.get("/applications");
    return response.data;
};

// Get Application by ID
export const getApplication = async (applicationId) => {
    const response = await api.get(
        `/applications/${applicationId}`
    );

    return response.data;
};

// Update Application Status
export const updateApplicationStatus = async (
    applicationId,
    status,
    notes = ""
) => {
    const response = await api.put(
        `/applications/${applicationId}`,
        {
            status,
            notes,
        }
    );

    return response.data;
};

// Withdraw Application
export const withdrawApplication = async (applicationId) => {
    const response = await api.delete(
        `/applications/${applicationId}`
    );

    return response.data;
};

// Search Applications
export const searchApplications = async (params) => {
    const response = await api.get(
        "/applications/search/",
        {
            params,
        }
    );

    return response.data;
};

// Dashboard Statistics
export const getApplicationDashboard = async () => {
    const response = await api.get(
        "/applications/dashboard"
    );

    return response.data;
};