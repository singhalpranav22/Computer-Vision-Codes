import cv2
import numpy as np

img = cv2.imread("res/img1.jpeg")
cv2.imshow("Main Image", img)
kernel = np.ones((5, 5), np.uint8)
# cv has BGR convention and the code below turn image to gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# code for blur
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# code for blur of the gray image
im = cv2.GaussianBlur(img, (19, 19), 1)
# This canny function gives images in the form of edges
imgCanny = cv2.Canny(img, 150, 200)
# Dialte thickens the edges of the cannny image
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# Erode thins the canny image
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Blurred",im)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
