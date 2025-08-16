import axios from "axios";

const API = axios.create({
  baseURL: "https://pro-ofhh.onrender.com", // use Render backend URL
  headers: { "Content-Type": "application/json" }
});

export default API;

