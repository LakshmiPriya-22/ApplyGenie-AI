import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import resumeService from "../../services/resumeService";

const ResumeChat = () => {
    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleSend = async () => {

        if (!question.trim()) return;

        const userQuestion = question;

        setMessages((prev) => [
            ...prev,
            {
                role: "user",
                content: userQuestion,
            },
        ]);

        setQuestion("");
        setLoading(true);

        try {

            const response = await resumeService.resumeChat({
                question: userQuestion,
            });

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: response.answer,
                },
            ]);

        } catch (error) {

            console.error(error);

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: "Sorry, I couldn't answer your question.",
                },
            ]);

        } finally {

            setLoading(false);

        }
    };

    return (
        <DashboardLayout>

            <div className="max-w-5xl mx-auto">

                <h1 className="text-3xl font-bold mb-2">
                    🤖 Resume Chat
                </h1>

                <p className="text-gray-500 mb-6">
                    Ask anything about your uploaded resume.
                </p>

                <div className="bg-white rounded-xl shadow-lg h-[550px] overflow-y-auto p-6 space-y-4">

                    {messages.length === 0 && (
                        <p className="text-gray-500">
                            Example questions:
                            <br />
                            • Tell me about myself.
                            <br />
                            • What are my strengths?
                            <br />
                            • Which programming languages do I know?
                            <br />
                            • What projects have I completed?
                        </p>
                    )}

                    {messages.map((msg, index) => (
                        <div
                            key={index}
                            className={`flex ${
                                msg.role === "user"
                                    ? "justify-end"
                                    : "justify-start"
                            }`}
                        >
                            <div
                                className={`max-w-[80%] rounded-xl px-5 py-3 ${
                                    msg.role === "user"
                                        ? "bg-cyan-600 text-white"
                                        : "bg-gray-200 text-gray-900"
                                }`}
                            >
                                <p className="font-semibold mb-1">
                                    {msg.role === "user"
                                        ? "You"
                                        : "ApplyGenie AI"}
                                </p>

                                <p className="whitespace-pre-wrap">
                                    {msg.content}
                                </p>
                            </div>
                        </div>
                    ))}

                    {loading && (
                        <div className="text-gray-500">
                            🤖 AI is thinking...
                        </div>
                    )}

                </div>

                <div className="flex gap-3 mt-6">

                    <input
                        type="text"
                        placeholder="Ask anything about your resume..."
                        value={question}
                        onChange={(e) => setQuestion(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === "Enter") {
                                handleSend();
                            }
                        }}
                        className="flex-1 border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
                    />

                    <button
                        onClick={handleSend}
                        disabled={loading}
                        className="bg-cyan-600 hover:bg-cyan-700 text-white px-6 rounded-lg disabled:opacity-50"
                    >
                        Send
                    </button>

                </div>

            </div>

        </DashboardLayout>
    );
};

export default ResumeChat;