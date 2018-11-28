import cv2
import numpy as np

#Create a black image, a window and bind the function to window

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')

#close on pressing Esc key
while(1):
    cv2.imshow("image", img)
    if(cv2.waitKey(20) & 0xFF ==27):
        break
cv2.destroyAllWindows()
