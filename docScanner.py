import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 768)
cap.set(10,150)
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    count = 0
    for cnt in contours:
        count+=1
        area = cv2.contourArea(cnt)
        print(area)
        if area > 1000:
            cv2.drawContours(fin, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
    print("count=")
    print(count)
def preprocessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(blur,200,200)
    kernerl = np.ones((5,5))
    imgdil = cv2.dilate(imgCanny,kernerl,iterations=2)
    imgErode = cv2.erode(imgdil,kernerl,iterations=1)
    return imgErode
while True:
    success,img = cap.read()
    fin = img.copy()
    img = preprocessing(img)

    getContours(img)
    cv2.imshow("Output",fin)
    if 0xFF == ord('q'):
        break
    cv2.waitKey(1)
