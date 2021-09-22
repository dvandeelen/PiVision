import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")
print(img.shape)    # first value Height, second Weight, last value channels = RGB = 3 planes

imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

imgCropped = img[0:119, 352:500]   # crob an immage , start en eindpunt, eerts height than weight

cv2.imshow("Image", img)
# cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)