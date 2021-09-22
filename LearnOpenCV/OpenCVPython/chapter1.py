# import cv2
# print("Package imported")

# ####################### READ IMAGE ############################
import cv2
# # LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg", img)
cv2.waitKey(0)

# ######################## READ VIDEO #############################
# import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success, img = cap.read()   # succes or not
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# ######################## READ WEBCAM  ############################
# import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)  # id for width
cap.set(4, frameHeight)  # id for height
cap.set(10, 50)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
