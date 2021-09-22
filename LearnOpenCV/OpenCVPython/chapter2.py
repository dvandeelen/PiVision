import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8) # all the values to be 1

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to Grayscale
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200) # treshhold values, change this higher to get less lines
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)   # increse this vlue increases the thickness of the lines
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny) # edge detector
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
