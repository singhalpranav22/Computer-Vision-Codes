import cv2
print('Package Imported')

# img = cv2.imread("res/img1.jpeg")
# cv2.imshow("output",img)
# cv2.waitKey(0)
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
while True:
    success,img = cap.read()
    cv2.imshow("video",img)
    cv2.waitKey(1)
    if 0xFF == ord('q'):
        break











