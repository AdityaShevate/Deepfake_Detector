import cv2

path = "../datasets/real/Real_Dataset/real_00001.jpg"

img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    print("Image loaded successfully")
    print("Shape:", img.shape)