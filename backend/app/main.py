from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from tensorflow.keras.models import load_model

from tensorflow.keras.preprocessing import image
import numpy as np
import os

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

        if len(contents) > 5 * 1024 * 1024:

            return {
                "success": False,
                "error": "File too large"
            }
        
        os.makedirs(
            "uploads",
            exist_ok=True
        )

        file_path = os.path.join(
            "uploads",
            file.file
        )

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

@app.post("/predict")
async def predict_image(
    file: UploadFile = File(...)
):
    allowed_extensions = (
    ".jpg",
    ".jpeg",
    ".png"
    )

    if not file.filename.lower().endswith(
        allowed_extensions
    ):
        return {
        "error": "Invalid image format"
        }
    
    contents = await file.read()

    file_path = os.path.join(
    "uploads",
    file.filename
    )
    with open(
        file_path,
        "wb"
    ) as f:
        f.write(contents)

    img = image.load_img(
    file_path,
    target_size=(224,224)
    )
    img_array = image.img_to_array(
    img
    )
    
    img_array = np.expand_dims(
    img_array,
    axis=0
    )

    img_array = img_array / 255.0

    prediction = model.predict(
    img_array
    )

    prediction = model.predict(
        img_array
    )

    # Adjust based on your class mapping

    if prediction[0][0] > 0.5:
        label = "Real"
    else:
        label = "Fake"

    confidence = float(
        prediction[0][0]
    ) * 100

    return {
        "prediction": label,
        "confidence": round(
            confidence,
            2
        )
    }






@app.post("/analyze")
async def analyze_image(
    file: UploadFile = File(...)
):

    allowed_extensions = (
        ".jpg",
        ".jpeg",
        ".png"
    )

    if not file.filename.lower().endswith(
        allowed_extensions
    ):
        return {
            "success": False,
            "error": "Only JPG, JPEG and PNG files are allowed"
        }
    if not file.filename:
        return {
            "success": False,
            "error": "No file selected"
        }

    try:

        contents = await file.read()
        file_size = len(contents)
        if file_size > 5 * 1024 * 1024:
            return {
                "success": False,
                "error": "File size exceeds 5 MB"
            }

        file_path = os.path.join(
            "uploads",
            file.filename
        )

        with open(
            file_path,
            "wb"
        ) as f:
            f.write(contents)

        img = image.load_img(
            file_path,
            target_size=(224,224)
        )

        img_array = image.img_to_array(
            img
        )

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        img_array = img_array / 255.0

        prediction = model.predict(
            img_array
        )

        # Adjust according to your class mapping

        if prediction[0][0] > 0.5:
            label = "Real"
        else:
            label = "Fake"

        confidence = (
            float(prediction[0][0])
            * 100
        )

        return {
            "prediction": label,
            "confidence": round(
                confidence,
                2
            )
        }

    except Exception as e:
        return {
            "error": str(e)
        }