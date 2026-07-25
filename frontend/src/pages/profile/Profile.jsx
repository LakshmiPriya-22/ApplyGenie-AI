import DashboardLayout from "../../components/layout/DashboardLayout";

const Profile = () => {
  return (
    <DashboardLayout>
      <div className="max-w-5xl mx-auto">

        <h1 className="text-3xl font-bold mb-2">
          My Profile
        </h1>

        <p className="text-gray-500 mb-8">
          View your profile information.
        </p>

        <div className="bg-white rounded-xl shadow-lg p-8">

          <div className="flex items-center gap-6">

            <img
              src="https://ui-avatars.com/api/?name=Renuka&background=06b6d4&color=fff"
              alt="Profile"
              className="w-28 h-28 rounded-full"
            />

            <div>

              <h2 className="text-2xl font-bold">
                Renuka Kamani
              </h2>

              <p className="text-gray-500">
                B.Tech IT Student
              </p>

              <p className="text-gray-500">
                renuka@email.com
              </p>

            </div>

          </div>

          <div className="grid md:grid-cols-2 gap-6 mt-10">

            <div className="bg-gray-100 p-5 rounded-lg">
              <h3 className="font-semibold">College</h3>
              <p>Shri Vishnu Engineering College for Women</p>
            </div>

            <div className="bg-gray-100 p-5 rounded-lg">
              <h3 className="font-semibold">Branch</h3>
              <p>Information Technology</p>
            </div>

            <div className="bg-gray-100 p-5 rounded-lg">
              <h3 className="font-semibold">CGPA</h3>
              <p>9.25</p>
            </div>

            <div className="bg-gray-100 p-5 rounded-lg">
              <h3 className="font-semibold">Graduation</h3>
              <p>2028</p>
            </div>

          </div>

        </div>

      </div>
    </DashboardLayout>
  );
};

export default Profile;