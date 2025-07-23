import { getDB } from "../services/api"
import { useEffect, useState } from "react";

class Computation {
  constructor(operation, input, result, cached, apiKey, timestamp) {
    this.operation = operation;
    this.input = input;
    this.result = result;
    this.cached = cached;
    this.api_key = apiKey;
    this.timestamp = timestamp;
  }
}


class DeletedItem {
  constructor(key, value, reason = "manual delete", operation = "unknown", timestamp = new Date()) {
    this.key = key;
    this.value = value;
    this.reason = reason;
    this.operation = operation;
    this.timestamp = timestamp;
  }
}


export default function Db() {
  const [computations, setComputations] = useState([]);
  const [deletedItems, setDeletedItems] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await getDB();
        const comps = res.data.computations.map(
          (c) =>
            new Computation(c.operation, c.input, c.result, c.cached, c.api_key, c.timestamp)
        );
        const dels = res.data.deleted_items.map(
          (d) =>
            new DeletedItem(d.key, d.value, d.reason, d.operation, d.timestamp)
        );
        setComputations(comps);
        setDeletedItems(dels);
      } catch (err) {
        setError("Failed to fetch database contents.");
      }
    }

    fetchData();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2 style={{ textAlign: "center" }}>Database Snapshot</h2>

      {error && (
        <p style={{ color: "red", textAlign: "center" }}>{error}</p>
      )}

      <section>
        <h3>Computations</h3>
        {computations.length === 0 ? (
          <p>No computations found.</p>
        ) : (
          <ul>
            {computations.map((comp, index) => (
              <li key={index}>
                <strong>{comp.operation}</strong>({comp.input}) = {comp.result}{" "}
                [{comp.cached ? "Cached" : "Fresh"}] - {new Date(comp.timestamp).toLocaleString()}
              </li>
            ))}
          </ul>
        )}
      </section>

      <section style={{ marginTop: "30px" }}>
        <h3>Deleted Items</h3>
        {deletedItems.length === 0 ? (
          <p>No deleted items found.</p>
        ) : (
          <ul>
            {deletedItems.map((item, index) => (
              <li key={index}>
                <strong>{item.key}</strong>: {item.value} (
                {item.reason}, op: {item.operation}) -{" "}
                {new Date(item.timestamp).toLocaleString()}
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}

