import { useEffect, useState } from "react";
import DashboardLayout from "../../components/layout/DashboardLayout";
import profileService from "../../services/profileService";

const Profile = () => {

  const [profile, setProfile] = useState(null);
  const [editing, setEditing] = useState(false);

  const [form, setForm] = useState({
    full_name: "",
    phone: "",
    college: "",
    degree: "",
    branch: "",
    current_year: "",
    cgpa: "",
    headline: "",
    bio: "",
    linkedin: "",
    github: "",
    portfolio: "",
  });

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {

      const data = await profileService.getProfile();

      setProfile(data);

      setForm({
        full_name: data.full_name || "",
        phone: data.phone || "",
        college: data.college || "",
        degree: data.degree || "",
        branch: data.branch || "",
        current_year: data.current_year || "",
        cgpa: data.cgpa || "",
        headline: data.headline || "",
        bio: data.bio || "",
        linkedin: data.linkedin || "",
        github: data.github || "",
        portfolio: data.portfolio || "",
      });

    } catch (err) {
      console.error(err);
    }
  };

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSave = async () => {

    try {

      await profileService.updateProfile(form);

      setEditing(false);

      fetchProfile();

      alert("Profile Updated Successfully");

    } catch (err) {

      console.error(err);

      alert("Failed to update profile");

    }

  };

  if (!profile)
    return (
      <DashboardLayout>
        <div className="text-white p-10">
          Loading...
        </div>
      </DashboardLayout>
    );

  return (
    <DashboardLayout>

      <div className="max-w-6xl mx-auto">

        <div className="bg-[#111827] rounded-2xl p-10">

          <div className="flex items-center gap-8">

            <img
              src={
                profile.profile_image
                  ? profile.profile_image
                  : "https://cdn-icons-png.flaticon.com/512/149/149071.png"
              }
              alt=""
              className="w-36 h-36 rounded-full object-cover"
            />

            <div>

              <h1 className="text-4xl font-bold">
                {profile.full_name}
              </h1>

              <p className="text-cyan-400 mt-2">
                {profile.headline}
              </p>

            </div>

          </div>

          <hr className="my-8 border-gray-700" />

          <div className="grid grid-cols-2 gap-6">

            <input
              name="full_name"
              value={form.full_name}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="Full Name"
            />

            <input
              name="phone"
              value={form.phone}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="Phone"
            />

            <input
              name="college"
              value={form.college}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="College"
            />

            <input
              name="degree"
              value={form.degree}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="Degree"
            />

            <input
              name="branch"
              value={form.branch}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="Branch"
            />

            <input
              name="current_year"
              value={form.current_year}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="Current Year"
            />

            <input
              name="cgpa"
              value={form.cgpa}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="CGPA"
            />

            <input
              name="linkedin"
              value={form.linkedin}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="LinkedIn"
            />

            <input
              name="github"
              value={form.github}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="GitHub"
            />

            <input
              name="portfolio"
              value={form.portfolio}
              onChange={handleChange}
              disabled={!editing}
              className="p-3 rounded bg-gray-800"
              placeholder="Portfolio"
            />

          </div>

          <textarea
            name="bio"
            value={form.bio}
            onChange={handleChange}
            disabled={!editing}
            rows="5"
            className="mt-6 w-full p-4 rounded bg-gray-800"
            placeholder="Bio"
          />

          <div className="flex gap-4 mt-8">

            {!editing ? (

              <button
                onClick={() => setEditing(true)}
                className="bg-cyan-600 px-6 py-3 rounded-xl"
              >
                Edit Profile
              </button>

            ) : (

              <button
                onClick={handleSave}
                className="bg-green-600 px-6 py-3 rounded-xl"
              >
                Save Changes
              </button>

            )}

          </div>

        </div>

      </div>

    </DashboardLayout>
  );

};

export default Profile;