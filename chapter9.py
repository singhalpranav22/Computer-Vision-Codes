# face detection code in web cam
import cv2
facecascade = cv2.CascadeClassifier("res/haarcascade.xml");
cap = cv2.VideoCapture(1)
frameWidth = 640
frameHeight = 640
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    print(success)
    # img = cv2.resize(img,(640,640))
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("Result", img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break