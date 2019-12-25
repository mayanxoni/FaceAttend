import os

import cv2
import mysql.connector


def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read("trainer/trainer.yml")
classifier_path = "classifier.xml"
image_classifier = cv2.CascadeClassifier(classifier_path)


def get_profile(s_roll):
    try:
        # connection = mysql.connector.connect(host="remotemysql.com", user="QFXScvqy83", passwd="M0XDbV1MvD", database="QFXScvqy83")
        connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
        db_cursor = connection.cursor()
        print(str(s_roll))
        db_cursor.execute("SELECT name FROM studentdetails WHERE enrollement = " + str(s_roll))
        query_result = db_cursor.fetchone()
        student_profile = None
        for row in query_result:
            student_profile = row
        print(student_profile)
        connection.close()
        return student_profile

    except Exception as e:
        print(e)


camera_feed = cv2.VideoCapture(0, cv2.CAP_DSHOW)
font = cv2.FONT_HERSHEY_SIMPLEX
profiles = {}

while True:
    ret, image = camera_feed.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = image_classifier.detectMultiScale(gray_image, 1.2, 5)
    for (x, y, w, h) in faces:
        student_id, confidence = recognizer.predict(gray_image[y:y + h, x:x + w])
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print(str(student_id))
        profile = get_profile(student_id)
        if profile is not None:
            cv2.putText(image, profile, (x, y + h + 30), font, 1, (0, 0, 255), 3)
            cv2.putText(image, "Accuracy: {0:.2f}%".format(round(100 - confidence, 2)), (x, y + h + 60), font, 1, (0, 0, 255), 3)
    cv2.imshow('Face', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        print("exit")
        break

camera_feed.release()
cv2.destroyAllWindows()
