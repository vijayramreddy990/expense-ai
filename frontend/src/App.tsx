import { useState, useEffect } from "react";

type HealthResponse = {
  status: string;
};

function App() {
  const [status, setStatus] = useState("Checking .....");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/health")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data: HealthResponse) => {
        setStatus(data.status);
      })
      .catch((error) => {
        console.error("Error fetching health status:", error);
        setStatus("Error fetching status");
      });
  }, []);

  return (
    <main>
      <h1>AI Expense Agent</h1>
      <p>Backend Status: {status}</p>
    </main>
  );
}

export default App;
