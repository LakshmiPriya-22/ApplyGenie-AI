import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import DashboardLayout from "../../components/layout/DashboardLayout";

import {
  uploadResume,
  getMyResume,
  deleteResume,
} from "../../api/resume";

export default function ProfileResume() {

  const navigate = useNavigate();

  const [resume, setResume] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);

  useEffect(() => {
    loadResume();
  }, []);

  const loadResume = async () => {
    try {
      const data = await getMyResume();
      setResume(data);
    } catch {
      setResume(null);
    }
  };

  const handleUpload = async () => {

    if (!selectedFile) {
      alert("Please select a PDF.");
      return;
    }

    try {

      await uploadResume(selectedFile);

      alert("Resume Uploaded Successfully");

      setSelectedFile(null);

      loadResume();

    } catch (err) {

      console.log(err);

      alert("Upload Failed");

    }

  };

  const handleDelete = async () => {

    if (!window.confirm("Delete this resume?")) return;

    try {

      await deleteResume(resume.id);

      alert("Resume Deleted Successfully");

      setResume(null);

    } catch (err) {

      console.log(err);

      alert("Delete Failed");

    }

  };

  const handleView = () => {

    window.open(
      `http://127.0.0.1:8000/uploads/${resume.filename}`,
      "_blank"
    );

  };

  const handleAnalyze = () => {

    navigate("/resume-analysis");

  };

  return (

    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-8">

        Profile & Resume

      </h1>

      <div className="bg-[#111827] rounded-2xl p-8">

        {resume ? (

          <>

            <h2 className="text-2xl font-semibold mb-5">

              Uploaded Resume

            </h2>

            <div className="bg-slate-800 rounded-xl p-5">

              <h3 className="text-xl font-semibold">

                📄 {resume.filename}

              </h3>

              <p className="text-slate-400 mt-2">

                Resume uploaded successfully.

              </p>

              <div className="flex gap-4 mt-6 flex-wrap">

                <button
                  onClick={handleView}
                  className="bg-blue-600 hover:bg-blue-700 px-5 py-3 rounded-lg"
                >
                  View Resume
                </button>

                <button
                  onClick={handleAnalyze}
                  className="bg-green-600 hover:bg-green-700 px-5 py-3 rounded-lg"
                >
                  Analyze Resume
                </button>

                <button
                  onClick={handleDelete}
                  className="bg-red-600 hover:bg-red-700 px-5 py-3 rounded-lg"
                >
                  Delete Resume
                </button>

              </div>

            </div>

          </>

        ) : (

          <>

            <h2 className="text-2xl font-semibold mb-6">

              Upload Resume

            </h2>

            <input
              type="file"
              accept=".pdf"
              onChange={(e) => setSelectedFile(e.target.files[0])}
              className="mb-6"
            />

            <br />

            <button
              onClick={handleUpload}
              className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg"
            >
              Upload Resume
            </button>

          </>

        )}

      </div>

    </DashboardLayout>

  );

}