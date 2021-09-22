import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # size of the image, maak een zwarte afbeelding
# print(img.shape)    # np.zeros((512, 512) is grayscale omdat deze maar 1 plane heeft
imgBlue = np.zeros((512, 512, 3), np.uint8)
print(imgBlue)
imgBlue[:] = 255, 0, 0  # first 255 is the value blue, : is for all values
# when change : to [200:300, 100:300] just a block will be blue

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # img.shape[0] max height, img.shape[1] max weight value, so you get a diagonal line
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # the 2 is the thickness, replace this by cv2.FILLED to fill this whole space
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3) # Place some text in the img


cv2.imshow("Image", img)
cv2.imshow("Image Blue", imgBlue)

cv2.waitKey(0)