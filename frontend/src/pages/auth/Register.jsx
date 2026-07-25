import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const Register = () => {
  const navigate = useNavigate();

  const { register } = useAuth();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    if (
      formData.password !==
      formData.confirmPassword
    ) {
      setError("Passwords do not match");
      return;
    }

    setLoading(true);

    try {

      await register(formData);

      navigate("/login");

    } catch (err) {

      setError(err.detail || "Registration Failed");

    }

    setLoading(false);

  };

  return (

    <div className="min-h-screen grid lg:grid-cols-2">

      {/* Left */}

      <div className="hidden lg:flex bg-cyan-600 text-white flex-col justify-center items-center p-16">

        <h1 className="text-5xl font-bold">
          ApplyGenie AI
        </h1>

        <p className="mt-6 text-lg text-center max-w-md">
          Create your account and start your AI Placement Journey.
        </p>

      </div>

      {/* Right */}

      <div className="flex items-center justify-center bg-gray-100">

        <div className="bg-white w-full max-w-md p-8 rounded-xl shadow-xl">

          <h2 className="text-3xl font-bold mb-2">
            Create Account
          </h2>

          <p className="text-gray-500 mb-8">
            Register to continue
          </p>

          <form
            className="space-y-5"
            onSubmit={handleSubmit}
          >

            <input
              type="text"
              name="name"
              placeholder="Full Name"
              className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
              value={formData.name}
              onChange={handleChange}
            />

            <input
              type="email"
              name="email"
              placeholder="Email"
              className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
              value={formData.email}
              onChange={handleChange}
            />

            <input
              type="password"
              name="password"
              placeholder="Password"
              className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
              value={formData.password}
              onChange={handleChange}
            />

            <input
              type="password"
              name="confirmPassword"
              placeholder="Confirm Password"
              className="w-full border rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-cyan-500"
              value={formData.confirmPassword}
              onChange={handleChange}
            />

            {error && (
              <p className="text-red-500">
                {error}
              </p>
            )}

            <button
              className="w-full bg-cyan-600 hover:bg-cyan-700 text-white py-3 rounded-lg font-semibold"
            >
              {loading ? "Creating..." : "Register"}
            </button>

          </form>

          <p className="text-center mt-6">

            Already have an account?

            <Link
              to="/login"
              className="text-cyan-600 ml-2"
            >
              Login
            </Link>

          </p>

        </div>

      </div>

    </div>

  );
};

export default Register;