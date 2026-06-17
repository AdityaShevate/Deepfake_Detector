import cv2

img = cv2.imread("group.jpg")

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=4
)
print(faces)
print(
    "Faces Detected:",
    len(faces)
)

for (x,y,w,h) in faces:

    print("Face Found")

    print("X:",x)

    print("Y:",y)

    print("Width:",w)

    print("Height:",h)

    cv2.rectangle(
        img,
        (x,y),
        (x+w,y+h),
        (0,255,0),
        3
    )
cv2.imshow("Face",img)
cv2.waitKey(0)

count = 0

for (x,y,w,h) in faces:

    face = img[y:y+h,x:x+w]
    cv2.imwrite(
        f"face_{count}.jpg",
        face
    )
    count += 1