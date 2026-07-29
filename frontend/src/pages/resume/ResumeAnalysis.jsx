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

console.log(data);

setAnalysis(data.analysis);

        } catch (err) {

            console.log(err);

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

                <div>

                    <h2 className="text-2xl font-semibold">

                        ATS Score

                    </h2>

                    <h1 className="text-6xl text-green-500 mt-4">

                        {analysis.resume_score}%

                    </h1>

                </div>

                <div>

                    <h2 className="text-2xl font-semibold mb-4">

                        Skills

                    </h2>

                    <ul className="space-y-2">

                        {analysis.technical_skills?.map((skill) => (
  <li key={skill}>✅ {skill}</li>
))}

                    </ul>

                </div>

                <div>

                    <h2 className="text-2xl font-semibold mb-4">

                        Missing Skills

                    </h2>

                    <ul className="space-y-2">

                        {analysis.missing_skills?.map(skill => (

                            <li key={skill}>

                                ❌ {skill}

                            </li>

                        ))}

                    </ul>

                </div>

                <div>

                    <h2 className="text-2xl font-semibold mb-4">

                        Suggestions

                    </h2>

                    <ul className="space-y-2">

                        {analysis.career_suggestions?.map(item => (

                            <li key={item}>

                                • {item}

                            </li>

                        ))}

                    </ul>

                </div>

            </div>

        </DashboardLayout>

    );

}