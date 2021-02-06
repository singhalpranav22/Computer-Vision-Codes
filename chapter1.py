# #Read Image
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("Resources/img1.jpeg")
# # DISPLAY
# cv2.imshow("output-name",img)
# cv2.waitKey(0)
# # Read Video
# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture("Resources/vid2.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#          break
# Read Webcam
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break