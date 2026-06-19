from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import numpy as np

model = load_model(
    "saved_models/deepfake_detector.keras"
)

image_path = "../test_images/test2.jpg"

img = image.load_img(
    image_path,
    target_size=(224,224)
)

img_array = image.img_to_array(img)

img_array = np.expand_dims(
    img_array,
    axis=0
)

img_array = img_array / 255.0

prediction = model.predict(
    img_array
)

confidence = prediction[0][0] * 100

if prediction[0][0] > 0.5:

    print("Prediction: Fake")

else:

    print("Prediction: Real")

print(
    f"Confidence: {confidence:.2f}%"
)