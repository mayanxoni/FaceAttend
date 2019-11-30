import cv2
import os
import sqlite3


def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read("trainer/trainer.yml")
cascadePath = "classifier.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)


def get_profile(student_id):
    connection = sqlite3.connect("database/facebase.db")
    command = "SELECT * FROM students WHERE ID = " + str(student_id)
    cursor = connection.execute(command)
    student_profile = None
    for row in cursor:
        student_profile = row
    connection.close()
    return student_profile


font = cv2.FONT_HERSHEY_SIMPLEX
video_feed = cv2.VideoCapture(0)

while True:
    ret, image = video_feed.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray_image, 1.2, 5)
    for (x, y, w, h) in faces:
        student_id, confidence = recognizer.predict(gray_image[y:y + h, x:x + w])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        profile = get_profile(student_id)
        if profile is not None:
            cv2.putText(image, str(profile[0]), (x, y + h + 30), font, 1, (0, 0, 255), 3)
            cv2.putText(image, str(profile[1]), (x, y + h + 60), font, 1, (0, 0, 255), 3)
    cv2.imshow('Face', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video_feed.release()
cv2.destroyAllWindows()
