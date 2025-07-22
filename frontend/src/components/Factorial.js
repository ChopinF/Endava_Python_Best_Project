import { useState } from "react";
import { retrieveFactorial } from "../services/api";

export default function Factorial() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await retrieveFactorial(Number(number));
      setResult(res.data);
    } catch (err) {
      alert("Error retrieving factorial.");
    }
  };

  return (
    <div>
      <h2>Factorial</h2>
      <form onSubmit={handleSubmit}>
  <input
    type="number"
    placeholder="Enter a number"
    value={number}
    onChange={(e) => setNumber(e.target.value)}
    required
  />
  <button type="submit">Get Factorial</button>
</form>
      {result && (
        <p>
          Answer: {result.answer} (Cached: {result.cached ? "Yes" : "No"})
        </p>
      )}
    </div>
  );
}