import Factorial from "./components/Factorial";
import Fibonacci from "./components/Fibonacci";
import Power from "./components/Power";
import React, { useState } from "react";
import "./App.css";


function App() {
  const [selectedForm, setSelectedForm] = useState(null);
  const renderForm = () => {
    if (selectedForm === "factorial") return <Factorial />;
    if (selectedForm === "fibonacci") return <Fibonacci />;
    if (selectedForm === "power") return <Power />;
    return null;
  };
  return (
    <div className="app-container">
      <h1>Endava Math Frontend</h1>

      <div className="button-row">
        <button className="nav-button" onClick={() => setSelectedForm("factorial")}>
          Factorial
        </button>
        <button className="nav-button" onClick={() => setSelectedForm("fibonacci")}>
          Fibonacci
        </button>
        <button className="nav-button" onClick={() => setSelectedForm("power")}>
          Power
        </button>
      </div>

      <div className="form-section">
        {renderForm()}
      </div>
    </div>
  );
}

export default App;