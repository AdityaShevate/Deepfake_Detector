from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load trained model
model = load_model("saved_models/deepfake_detector.keras")

# Create validation dataset
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

validation_generator = datagen.flow_from_directory(
    "../datasets",
    target_size=(224, 224),
    batch_size=32,
    class_mode="binary",
    subset="validation"
)

# Evaluate model
loss, accuracy = model.evaluate(validation_generator)

print(f"Loss: {loss:.4f}")
print(f"Accuracy: {accuracy:.4f}")