import { useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import resumeService from "../../services/resumeService";

const ResumeChat = () => {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!question.trim()) return;

    const userMessage = {
      role: "user",
      content: question,
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      const response = await resumeService.resumeChat({
        question: question,
      });

      const aiMessage = {
        role: "assistant",
        content: response,
      };

      setMessages((prev) => [...prev, aiMessage]);

      setQuestion("");
    } catch (error) {
      console.error(error);
      alert("Failed to get response.");
    }

    setLoading(false);
  };

  return (
    <DashboardLayout>
      <div className="max-w-5xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Resume Chat
        </h1>

        <p className="text-gray-500 mb-6">
          Ask anything about your resume.
        </p>

        <div className="bg-white rounded-xl shadow-lg h-[500px] overflow-y-auto p-6 space-y-4">

          {messages.length === 0 && (
            <p className="text-gray-500">
              Start a conversation with your AI Resume Assistant.
            </p>
          )}

          {messages.map((msg, index) => (
            <div
              key={index}
              className={`p-4 rounded-lg max-w-[80%] ${
                msg.role === "user"
                  ? "bg-cyan-500 text-white ml-auto"
                  : "bg-gray-200 text-black"
              }`}
            >
              {msg.content}
            </div>
          ))}

          {loading && (
            <p className="text-gray-500">
              AI is typing...
            </p>
          )}

        </div>

        <div className="flex gap-3 mt-6">

          <input
            type="text"
            placeholder="Ask a question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            className="flex-1 border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
          />

          <button
            onClick={handleSend}
            className="bg-cyan-600 hover:bg-cyan-700 text-white px-6 rounded-lg"
          >
            Send
          </button>

        </div>

      </div>
    </DashboardLayout>
  );
};

export default ResumeChat;