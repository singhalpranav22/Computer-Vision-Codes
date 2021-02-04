import cv2
import numpy as np
img = cv2.imread("res/img2.jpg")
# Width comes first, than height comes
img = cv2.resize(img,(480,640))
cv2.imshow("Eiffel Tower",img)
imgcropped = img[0:400,0:600]
cv2.imshow("cropped image",imgcropped)
print(img.shape)
cv2.waitKey(0)
