import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);

  return (
    <div>
      <h1>Deepfake Detector</h1>

      <input
        type="file"
        accept="image/*"
        onChange={(event) => {
          const selectedFile =
            event.target.files[0];

          setFile(selectedFile);

          if (selectedFile) {
            setPreview(
              URL.createObjectURL(selectedFile)
            );
          }
        }}
      />

      <p>
        {file
          ? file.name
          : "No file selected"}
      </p>

      {preview && (
        <img
          src={preview}
          alt="Preview"
          width="300"
        />
      )}

      <br />
      <br />

      <button>Detect</button>
    </div>
  );
}

export default App;