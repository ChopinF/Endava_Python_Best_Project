import { useState } from "react";
import { retrievePower } from "../services/api";

export default function Power() {
  const [a, setA] = useState("");
  const [b, setB] = useState("");
  const [type, setType] = useState("int");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await retrievePower(type, a, b);
      setResult(res.data);
    } catch (err) {
      alert("Error performing power operation.");
    }
  };

  return (
    <div>
      <h2 style={{ textAlign: "center" }}>Power (a ^ b)</h2>
      <form
        onSubmit={handleSubmit}
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        <select
          value={type}
          onChange={(e) => setType(e.target.value)}
          style={{
            padding: "10px",
            borderRadius: "8px",
            fontSize: "16px",
            backgroundColor: "#f0f0f0",
            border: "none",
          }}
        >
          <option value="int">int</option>
          <option value="float">float</option>
          <option value="complex">complex</option>
        </select>

        <input
          type="text"
          value={a}
          onChange={(e) => setA(e.target.value)}
          placeholder="Base (a)"
          required
        />
        <input
          type="text"
          value={b}
          onChange={(e) => setB(e.target.value)}
          placeholder="Exponent (b)"
          required
        />

        <button type="submit">Calculate</button>
      </form>

      {result && (
        <p style={{ textAlign: "center", marginTop: "30px", fontSize: "18px" }}>
          Answer: {result.answer} <br />
          (Cached: {result.cached ? "Yes" : "No"})
        </p>
      )}
    </div>
  );
}
