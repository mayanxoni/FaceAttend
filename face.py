import cv2
import numpy as np

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

id = input("Enter User ID: ")
ver = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        ver = ver + 1
        cv2.imwrite("dataSet/user_"+str(id)+"_version_"+str(ver)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.waitKey(100)
    cv2.imshow("Face", img)
    cv2.waitKey(1)
    if(ver > 20):
        break

cam.release()
cv2.destroyAllWindows()