import cv2
import numpy as np

def blankcallable(a):
    pass

#Create a blank black image
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("MyImage")

#Create Tracker Bars for Red Green Blue
cv2.createTrackbar("Red","MyImage",0,255,blankcallable)
cv2.createTrackbar("Green","MyImage",0,255,blankcallable)
cv2.createTrackbar("Blue","MyImage",0,255,blankcallable)

r = 0
g = 0
b = 0

#Read Second Image
img2 = cv2.imread("img2.jpg")
b2,g2,r2 = cv2.split(img2)
b2_orig,g2_orig,r2_orig = cv2.split(img2)
cv2.namedWindow("Output")

while(True):
    cv2.imshow("MyImage", img)
    cv2.imshow("Output", img2)

    #Set color to the image
    img[:] = [b,g,r]

    b2 = b2 - b
    g2 = g2 - g
    r2 = r2 - r

    img2 = cv2.merge((b2, g2, r2))

    #Put text on the image
    cv2.putText(img, "Press r to reset", (10, 50), cv2.QT_FONT_NORMAL, 1, (200, 200, 200), 1)
    k = cv2.waitKey(3) & 0xFF

    #Get Tracker Bar position
    r = cv2.getTrackbarPos("Red", "MyImage")
    b = cv2.getTrackbarPos("Blue", "MyImage")
    g = cv2.getTrackbarPos("Green", "MyImage")

    #Reset the trackbar position
    if(k == ord('r')):
        r = cv2.setTrackbarPos("Red", "MyImage",0)
        b = cv2.setTrackbarPos("Blue", "MyImage",0)
        g = cv2.setTrackbarPos("Green", "MyImage",0)

        b2 = b2_orig
        g2 = g2_orig
        r2 = r2_orig

    elif(k == ord('q')):
        break
    elif(k == 27):
        break

cv2.destroyAllWindows()



