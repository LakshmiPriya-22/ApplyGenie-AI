import DashboardLayout from "../../components/layout/DashboardLayout";
import { useState } from "react";

const UploadResume = () => {
  const [file, setFile] = useState(null);

  const handleUpload = () => {
    if (!file) {
      alert("Please select a resume.");
      return;
    }

    alert(`Resume "${file.name}" uploaded successfully.`);
  };

  return (
    <DashboardLayout>

      <div className="max-w-3xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          Upload Resume
        </h1>

        <p className="text-gray-500 mb-8">
          Upload your latest resume to begin AI analysis.
        </p>

        <div className="bg-white rounded-xl shadow-lg p-8">

          <div className="border-2 border-dashed border-cyan-400 rounded-xl p-12 text-center">

            <h2 className="text-xl font-semibold mb-4">
              Drag & Drop Resume
            </h2>

            <p className="text-gray-500 mb-6">
              PDF only
            </p>

            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setFile(e.target.files[0])}
              className="mb-6"
            />

            {file && (
              <div className="mb-5">

                <p className="font-medium">
                  Selected File
                </p>

                <p className="text-cyan-600">
                  {file.name}
                </p>

              </div>
            )}

            <button
              onClick={handleUpload}
              className="bg-cyan-600 hover:bg-cyan-700 text-white px-8 py-3 rounded-lg"
            >
              Upload Resume
            </button>

          </div>

        </div>

      </div>

    </DashboardLayout>
  );
};

export default UploadResume;