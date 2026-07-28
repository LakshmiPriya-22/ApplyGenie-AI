import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Mail, Lock, Sparkles } from "lucide-react";

import { registerUser } from "../api/auth";

export default function Register() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const handleRegister = async () => {
    if (!email || !password) {
      alert("Please enter email and password.");
      return;
    }

    try {
      setLoading(true);

      await registerUser({
        email,
        password,
      });

      alert("Registration Successful!");

      navigate("/");

    } catch (error) {
  console.error("Registration Error:", error);

  if (error.response) {
    console.log("Status:", error.response.status);
    console.log("Data:", error.response.data);

    alert(JSON.stringify(error.response.data));
  } else {
    alert(error.message);
  }
} finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#030712] flex items-center justify-center px-8">

      <div className="w-full max-w-7xl grid lg:grid-cols-[0.9fr_1.1fr] gap-20 items-center">

        {/* LEFT */}

        <div>

          <div className="flex items-center gap-3 mb-16">

            <div className="w-11 h-11 rounded-xl bg-[#111827] border border-slate-700 flex items-center justify-center">
              <Sparkles size={20} />
            </div>

            <h1 className="text-3xl font-bold">
              ApplyGenie AI
            </h1>

          </div>

          <h2 className="text-5xl font-bold leading-tight">

            Start Your <span className="text-blue-500">AI</span>

            <br />

            Career Journey

          </h2>

          <p className="mt-8 text-slate-400 text-lg leading-8 max-w-lg">

            Create your account and unlock AI-powered
            resume analysis, job matching and interview preparation.

          </p>

        </div>

        {/* RIGHT */}

        <div className="flex justify-center">

          <div className="w-full max-w-lg bg-[#111827] rounded-3xl border border-slate-700 shadow-2xl p-10">

            <h1 className="text-4xl font-bold text-center">
              Create Account
            </h1>

            <p className="text-center text-slate-400 mt-3 mb-10">
              Join ApplyGenie AI
            </p>

            {/* EMAIL */}

            <label className="text-sm text-slate-300">
              Email
            </label>

            <div className="mt-2 h-14 rounded-xl border border-slate-700 bg-[#1E293B] flex items-center px-4">

              <Mail className="text-slate-400" />

              <input
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="ml-3 flex-1 bg-transparent outline-none text-white"
              />

            </div>

            {/* PASSWORD */}

            <label className="text-sm text-slate-300 mt-6 block">
              Password
            </label>

            <div className="mt-2 h-14 rounded-xl border border-slate-700 bg-[#1E293B] flex items-center px-4">

              <Lock className="text-slate-400" />

              <input
                type="password"
                placeholder="Create password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="ml-3 flex-1 bg-transparent outline-none text-white"
              />

            </div>

            {/* REGISTER BUTTON */}

            <button
              onClick={handleRegister}
              disabled={loading}
              className="
                mt-8
                h-14
                w-full
                rounded-xl
                bg-blue-600
                hover:bg-blue-700
                transition
                font-semibold
                text-white
                disabled:opacity-60
                disabled:cursor-not-allowed
              "
            >
              {loading ? "Creating Account..." : "Create Account"}
            </button>

            <p className="text-center mt-8 text-slate-400">

              Already have an account?

              <Link
                to="/"
                className="ml-2 text-blue-500 hover:underline"
              >
                Sign In
              </Link>

            </p>

          </div>

        </div>

      </div>

    </div>
  );
}