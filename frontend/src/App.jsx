import { useState } from "react";
import DetectButton from "./components/DetectButton";
import LoadingSpinner from "./components/LoadingSpinner";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ImageUpload from "./components/ImageUpload";
import ResultCard from "./components/ResultCard";
import api from "./services/api";

function App() {

  const [prediction, setPrediction] = useState("No Result");
  const [confidence, setConfidence] = useState(0);
  const [loading, setLoading] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);
  const handleDetect = async () => {

  const formData =
    new FormData();

  formData.append(
    "image",
    selectedFile
  );

  const response =
    await api.post(
      "/predict",
      formData
    );

  console.log(response.data);

};

  return (
    <div>
      <Header />

      <ImageUpload />

      
{
  loading && (
    <p>Analyzing Image...</p>
  )
}
<LoadingSpinner/>

      <button
        onClick={() => {
          setPrediction("Fake");
          setConfidence(93);
        }}
      >
        Test Result
      </button>
      <DetectButton
  onDetect={handleDetect}
/>
  

      <ResultCard
        prediction={prediction}
        confidence={confidence}
      />

      <Footer />
    </div>
  );
}

export default App;