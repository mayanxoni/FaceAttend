import cv2
import os
import sqlite3
import pickle
from PIL import Image
import numpy as np


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


def getProfile(student_id):
    conn = sqlite3.connect("facebase.db")
    cmd = "SELECT * FROM students WHERE ID = " + str(student_id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
        profile = getProfile(Id)
        if profile is not None:
            cv2.putText(im, str(profile[0]), (x, y + h + 30), font, 1, (0, 0, 255), 3)
            cv2.putText(im, str(profile[1]), (x, y + h + 60), font, 1, (0, 0, 255), 3)
    cv2.imshow('im', im)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
