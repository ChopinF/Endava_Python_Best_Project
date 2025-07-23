import { useState } from "react";
import { retrieveFactorial, populateFactorialCache } from "../services/api";

export default function Factorial() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState(null);
  const [message, setMessage] = useState("");

  const handleRetrieve = async (e) => {
    e.preventDefault();
    setMessage("");
    try {
      const res = await retrieveFactorial(Number(number));
      setResult(res.data);
    } catch (err) {
      alert("Failed to retrieve factorial.");
    }
  };

  const handlePopulate = async () => {
    setMessage("");
    try {
      await populateFactorialCache(Number(number));
      setMessage(`✅ Factorial cache populated up to ${number}`);
    } catch (err) {
      alert("Failed to populate factorial cache.");
    }
  };

  return (
    <div>
      <h2 style={{ textAlign: "center" }}>Factorial</h2>
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
          <button type="submit">Get Factorial</button>
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
