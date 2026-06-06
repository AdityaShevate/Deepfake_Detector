import cv2
img = cv2.imread("person.jpg")
#print(img)  #to print the pixel values of the image

#cv2.imshow("Person", img)  #to display the image in a window
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#print(img.shape)   #to print the dimensions of the image (height, width, channels)

#resized = cv2.resize(img,(224,224))  #to resize the image to a specific size (width, height)
#cv2.imshow("Resized", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#gray = cv2.cvtColor(
#    img,
 #   cv2.COLOR_BGR2GRAY
#)                        #to convert the image to grayscale
#cv2.imshow("Gray", gray)
#cv2.waitKey(0)
#cv2.imwrite(
#    "gray_person.jpg",
#    gray
#)                        #to save the grayscale image to a file


#cv2.rectangle(
#    img,
#    (100,100),
#    (300,300),
#    (0,255,0),
#    3
#)                      #to draw a rectangle on the image (image, top-left corner, bottom-right corner, color (BGR), thickness)
#cv2.imshow("Rectangle", img)
#cv2.waitKey(0)

