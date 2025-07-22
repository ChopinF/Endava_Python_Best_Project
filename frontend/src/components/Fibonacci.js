import { useState } from "react";
import { retrieveFibonacci } from "../services/api";

export default function Fibonacci() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await retrieveFibonacci(Number(number));
      setResult(res.data);
    } catch (err) {
      alert("Error retrieving Fibonacci.");
    }
  };

  return (
    <div>
      <h2>Fibonacci</h2>
      <form onSubmit={handleSubmit}>
  <input
    type="number"
    placeholder="Enter a number"
    value={number}
    onChange={(e) => setNumber(e.target.value)}
    required
  />
  <button type="submit">Get Fibonacci</button>
</form>
      {result && (
        <p>
          Answer: {result.answer} (Cached: {result.cached ? "Yes" : "No"})
        </p>
      )}
    </div>
  );
}