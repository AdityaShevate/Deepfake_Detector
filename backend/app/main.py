from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from tensorflow.keras.models import load_model

app = FastAPI()

model = load_model(
    "models/deepfake_detector.keras"
)
print("Model Loaded Successfully")
def get_model():
    return model

@app.get("/")
def home():
    return {
        "message": "Deepfake Detection API Running"
    }

@app.post("/upload")
async def upload_image(
    file: UploadFile = File(...)
):
    allowed_extensions = (
    ".jpg",
    ".jpeg",
    ".png"
)
    if not file.filename.lower().endswith(
    allowed_extensions
):return {
        "error": "Only JPG, JPEG and PNG files are allowed"
    }
    
    try:
        contents = await file.read()

        with open(
            f"uploads/{file.filename}",
            "wb"
        ) as f:
            f.write(contents)

        return {
            "message": "Upload Successful",
            "filename": file.filename
        }
    
    except Exception as e:
        return{
        "error": str(e)
        }    

    size = len(contents)

    return {
        "message":"Upload Successful",
        "filename": file.filename,
        "size": size
    }
