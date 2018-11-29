import cv2
import numpy as np

def blankcallable(a):
    pass

#Create a blank black image
img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("My Image")

#Create Tracker Bars for Red Green Blue
cv2.createTrackBar("Red","MyImage",0,255,blankcallable)
cv2.createTrackBar("Green","MyImage",0,255,blankcallable)
cv2.createTrackBar("Blue","MyImage",0,255,blankcallable)

r = 0
g = 0
b = 0

#Read Second Image
