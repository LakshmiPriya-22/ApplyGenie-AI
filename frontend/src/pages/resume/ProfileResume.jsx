import { useState } from "react";
import DashboardLayout from "../components/layout/DashboardLayout";
import { uploadResume } from "../api/resume";

export default function ProfileResume() {

  const [file, setFile] = useState(null);

  const handleUpload = async () => {

    if (!file) {
      alert("Select a PDF");
      return;
    }

    try {

      await uploadResume(file);

      alert("Resume Uploaded Successfully");

    } catch (err) {

      console.log(err);

      alert("Upload Failed");

    }

  };

  return (

    <DashboardLayout>

      <h1 className="text-4xl font-bold mb-8">

        Profile & Resume

      </h1>

      <div className="bg-[#111827] rounded-2xl p-8">

        <input

          type="file"

          accept=".pdf"

          onChange={(e)=>setFile(e.target.files[0])}

        />

        <button

          onClick={handleUpload}

          className="mt-6 bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-xl"

        >

          Upload Resume

        </button>

      </div>

    </DashboardLayout>

  );

}