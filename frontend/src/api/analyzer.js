import api from "./axios";

export const getLatestAnalysis = async () => {

  const response = await api.get("/analyzer/latest");

  console.log("========== AXIOS RESPONSE ==========");
  console.log(response);

  console.log("========== RESPONSE.DATA ==========");
  console.log(response.data);

  console.log("TYPE:", typeof response.data);

  return response.data;
};