import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Mail, Lock, Sparkles } from "lucide-react";

import { loginUser } from "../api/auth";
import useAuth from "../hooks/useAuth";

export default function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    if (!email || !password) {
      alert("Please enter email and password.");
      return;
    }

    try {
      setLoading(true);

      const data = await loginUser(email, password);

      login(data.access_token);

      navigate("/dashboard");
    } catch (error) {
      console.error(error);

      alert("Invalid email or password.");
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

            Your <span className="text-blue-500">AI</span>

            <br />

            Career Assistant

          </h2>

          <p className="mt-8 text-slate-400 text-lg leading-8 max-w-lg">

            Everything you need to land your dream
            job, powered by Artificial Intelligence.

          </p>

        </div>

        {/* RIGHT */}

        <div className="flex justify-center">

          <div className="w-full max-w-lg bg-[#111827] rounded-3xl border border-slate-700 shadow-2xl p-10">

            <h1 className="text-4xl font-bold text-center">

              Welcome Back

            </h1>

            <p className="text-center text-slate-400 mt-3 mb-10">

              Sign in to continue

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
                placeholder="Enter your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="ml-3 flex-1 bg-transparent outline-none text-white"
              />

            </div>

            <button
              onClick={handleLogin}
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
              "
            >
              {loading ? "Signing In..." : "Sign In"}
            </button>

            <p className="text-center mt-8 text-slate-400">

              Don't have an account?

              <Link
                to="/register"
                className="ml-2 text-blue-500 hover:underline"
              >
                Create Account
              </Link>

            </p>

          </div>

        </div>

      </div>

    </div>
  );
}