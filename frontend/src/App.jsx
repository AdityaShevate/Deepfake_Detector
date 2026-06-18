import Header from "./components/Header";
import Footer from "./components/Footer";
import UploadButton from "./components/UploadButton";
import ImageUpload from "./components/ImageUpload";
import ResultCard from "./components/ResultCard";

function App() {
  return (
    <div>
      <Header />
      <ImageUpload />
      <button>Detect</button>
      <ResultCard />
      <Footer />
    </div>
  );
}

export default App;