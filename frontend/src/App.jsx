import { useState } from "react";
import DetectButton from "./components/DetectButton";
import LoadingSpinner from "./components/LoadingSpinner";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ImageUpload from "./components/ImageUpload";
import ResultCard from "./components/ResultCard";

function App() {

  const [prediction, setPrediction] = useState("No Result");
  const [confidence, setConfidence] = useState(0);
  const [loading, setLoading] = useState(false);

  return (
    <div>
      <Header />

      <ImageUpload />

      <DetectButton
  onDetect={() => {

    setLoading(true);

    setTimeout(() => {
      setLoading(false);
    }, 3000);

  }}
/>
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

      <ResultCard
        prediction={prediction}
        confidence={confidence}
      />

      <Footer />
    </div>
  );
}

export default App;