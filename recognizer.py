import os

import cv2
import mysql.connector


def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


font = cv2.FONT_HERSHEY_SIMPLEX
video_feed = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
assure_path_exists("trainer/")
recognizer.read("trainer/trainer.yml")
classifier_path = "classifier.xml"
faceCascade = cv2.CascadeClassifier(classifier_path)


def get_profile(s_enroll):
    try:
        connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT s_name FROM studentdetails WHERE s_enroll = " + str(s_enroll))
        query_result = db_cursor.fetchone()
        for row in query_result:
            print(row)
        student_profile = row
        return student_profile

    except Exception as e:
        print(e)
        # messageBox = QMessageBox()
        # messageBox.setWindowTitle("Exception caught!")
        # messageBox.setText(str(e))
        # messageBox.setIcon(QMessageBox.Critical)


while True:
    ret, image = video_feed.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray_image, 1.2, 5)
    for (x, y, w, h) in faces:
        student_id, confidence = recognizer.predict(gray_image[y:y + h, x:x + w])
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        profile = get_profile(student_id)
        if profile is not None:
            cv2.putText(image, profile, (x, y + h + 30), font, 1, (0, 0, 255), 3)
    cv2.imshow('Face', image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video_feed.release()
cv2.destroyAllWindows()
