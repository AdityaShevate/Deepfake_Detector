import { useState } from "react";

function ImageUpload() {

  const [preview, setPreview] = useState(null);

  const handleFileChange = (event) => {

    const file = event.target.files[0];

    if (file) {

      const imageUrl =
        URL.createObjectURL(file);

      setPreview(imageUrl);
    }
  };

  return (
  <div>

    <div className="upload-section">
      <h2>Upload Image</h2>

      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
      />
    </div>

    <div className="preview-section">
      <h2>Preview</h2>

      {preview ? (
        <img
          src={preview}
          alt="Preview"
        />
      ) : (
        <p>No image selected</p>
      )}
    </div>

  </div>
);
}
<button
  onClick={handleAnalyze}
>
  Analyze
</button>

export default ImageUpload;