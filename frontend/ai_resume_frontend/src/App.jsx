import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const uploadResume = async () => {
    if (!file) {
      alert("Please upload a resume first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/upload-resume",
        formData
      );

      setResult(response.data.analysis);
    } catch (error) {
      console.error(error);
      alert("Error analyzing resume");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="card">
        <h1>🤖 AI Resume Analyzer</h1>

        <div className="upload">
          <input type="file" onChange={handleFileChange} />
        </div>

        <button onClick={uploadResume} className="analyze-btn">
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {result && (
          <div className="result">
            <h2>Analysis Result</h2>
            <pre>{result}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;