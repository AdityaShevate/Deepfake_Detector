CNN = Convolutional Neural Network

Used for:
- Image classification
- Face recognition
- Deepfake detection

Input:
Image

Output:
Real / Fake




# CNN Architecture

Input:
224x224x3

Layers:

Conv2D(32)

MaxPooling2D

Conv2D(64)

MaxPooling2D

Flatten

Dense(128)

Dense(1)