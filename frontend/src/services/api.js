import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000", // Your FastAPI base
  headers: {
    name: "key", // Required API key header
  },
});

export const retrieveFactorial = (number) =>
  API.post("/fact/retrieve", { number });

export const retrieveFibonacci = (number) =>
  API.post("/fibo/retrieve", { number });

export const retrievePower = (type, a, b) =>
  API.post(`/pow/${type}`, { a, b });

export const getSupportedTypes = () =>
  API.get("/pow/");

export const populateFibonacciCache = (number) =>
  API.post("/fibo", { number });

export const populateFactorialCache = (number) =>
  API.post("/fact", { number });

export const clearCache = (type) =>
  API.delete(`/${type}`);
