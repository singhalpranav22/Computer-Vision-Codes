# These are the four corners of the queen image in pixels
# 1 :3672,637
# 2 : 5165,1318
# 3 : 1523,1970
# 4 :2975,2883

import cv2
import numpy as np

img = cv2.imread("res/img3.jpg")
width, height = 250,350 # Final width and the height for the image
pts1 = np.float32([[3672,637],[5165,1318],[1523,1970],[2975,2883]])
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
# draws image according to the perspective image
imgFinal = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Normal",img)
cv2.imshow("Final",imgFinal)
cv2.waitKey(0)