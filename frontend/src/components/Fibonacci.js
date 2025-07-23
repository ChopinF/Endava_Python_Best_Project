import { useState } from "react";
import { retrieveFibonacci, populateFibonacciCache } from "../services/api";

export default function Fibonacci() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState(null);
  const [message, setMessage] = useState("");

  const handleRetrieve = async (e) => {
    e.preventDefault();
    setMessage("");
    try {
      const res = await retrieveFibonacci(Number(number));
      setResult(res.data);
    } catch (err) {
      alert("Failed to retrieve Fibonacci number.");
    }
  };

  const handlePopulate = async () => {
    setMessage("");
    try {
      await populateFibonacciCache(Number(number));
      setMessage(`✅ Cache populated up to Fibonacci(${number})`);
    } catch (err) {
      alert("Failed to populate Fibonacci cache.");
    }
  };

  return (
    <div>
      <h2 style={{ textAlign: "center" }}>Fibonacci</h2>
      <form
        onSubmit={handleRetrieve}
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        <input
          type="number"
          placeholder="Enter a number"
          value={number}
          onChange={(e) => setNumber(e.target.value)}
          required
        />
        <div style={{ display: "flex", gap: "20px" }}>
          <button type="submit">Get Fibonacci</button>
          <button type="button" onClick={handlePopulate}>
            Populate Cache
          </button>
        </div>
      </form>

      {result && (
        <p style={{ textAlign: "center", marginTop: "30px", fontSize: "18px" }}>
          Answer: {result.answer} (Cached: {result.cached ? "Yes" : "No"})
        </p>
      )}

      {message && (
        <p style={{ textAlign: "center", marginTop: "20px", color: "#00cc66" }}>
          {message}
        </p>
      )}
    </div>
  );
}
