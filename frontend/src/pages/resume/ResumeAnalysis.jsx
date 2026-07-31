import { useEffect, useState } from "react";

import DashboardLayout from "../../components/layout/DashboardLayout";
import { getLatestAnalysis } from "../../api/analyzer";

export default function ResumeAnalysis() {
    const [analysis, setAnalysis] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadAnalysis();
    }, []);

    const loadAnalysis = async () => {
        try {
            const data = await getLatestAnalysis();

            console.log("========== ANALYSIS ==========");
            console.log("TYPE:", typeof data);
            console.log("DATA:", data);
            console.log("RESUME SCORE:", data?.resume_score);

            console.log("SETTING ANALYSIS:", data);
            setAnalysis(data);
        } catch (err) {
            console.error("Resume Analysis Error:", err);
        } finally {
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <DashboardLayout>
                <h1 className="text-3xl font-bold">
                    Loading Analysis...
                </h1>
            </DashboardLayout>
        );
    }

    if (!analysis) {
        return (
            <DashboardLayout>
                <h1 className="text-3xl font-bold">
                    No Analysis Found
                </h1>
            </DashboardLayout>
        );
    }

    return (
        <DashboardLayout>
            <h1 className="text-4xl font-bold mb-10">
                AI Resume Analysis
            </h1>

            <div className="bg-[#111827] rounded-2xl p-8 space-y-8">

                {/* ATS Score */}
                <div>
                    <h2 className="text-2xl font-semibold">
                        ATS Score
                    </h2>

                    <h1 className="text-6xl text-green-500 mt-4">
                        {analysis.resume_score ?? "Not Found"}%
                    </h1>
                </div>

                {/* Technical Skills */}
                <div>
                    <h2 className="text-2xl font-semibold mb-4">
                        Technical Skills
                    </h2>

                    {analysis.technical_skills?.length ? (
                        <ul className="space-y-2">
                            {analysis.technical_skills.map((skill) => (
                                <li key={skill}>✅ {skill}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No technical skills found.</p>
                    )}
                </div>

                {/* Soft Skills */}
                <div>
                    <h2 className="text-2xl font-semibold mb-4">
                        Soft Skills
                    </h2>

                    {analysis.soft_skills?.length ? (
                        <ul className="space-y-2">
                            {analysis.soft_skills.map((skill) => (
                                <li key={skill}>✅ {skill}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No soft skills found.</p>
                    )}
                </div>

                {/* Strengths */}
                <div>
                    <h2 className="text-2xl font-semibold mb-4">
                        Strengths
                    </h2>

                    {analysis.strengths?.length ? (
                        <ul className="space-y-2">
                            {analysis.strengths.map((item) => (
                                <li key={item}>⭐ {item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No strengths found.</p>
                    )}
                </div>

                {/* Missing Skills */}
                <div>
                    <h2 className="text-2xl font-semibold mb-4">
                        Missing Skills
                    </h2>

                    {analysis.missing_skills?.length ? (
                        <ul className="space-y-2">
                            {analysis.missing_skills.map((skill) => (
                                <li key={skill}>❌ {skill}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No missing skills.</p>
                    )}
                </div>

                {/* Career Suggestions */}
                <div>
                    <h2 className="text-2xl font-semibold mb-4">
                        Career Suggestions
                    </h2>

                    {analysis.career_suggestions?.length ? (
                        <ul className="space-y-2">
                            {analysis.career_suggestions.map((item) => (
                                <li key={item}>💡 {item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p>No suggestions found.</p>
                    )}
                </div>

            </div>
        </DashboardLayout>
    );
}