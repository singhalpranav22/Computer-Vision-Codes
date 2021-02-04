# Adding shapes and text
import cv2
import numpy as np
# Makes a matrix of 512x512x3 with all the values as 0 and allows values from 0 to 255
img = np.zeros((512,512,3),np.uint8)
# img[:]=255,0,0 //  to make the matrix colors in bgr format
# draw a line see the paramaeters
cv2.line(img,(0,0),(256,256),(123,43,211),1)
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(20,20),(240,240),(211,198,131))
cv2.putText(img,"Hello CVWorld",(270,40),cv2.FONT_HERSHEY_COMPLEX,1,(123,213,213))
cv2.imshow("Output",img)
cv2.waitKey(0)