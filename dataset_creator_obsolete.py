import cv2
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from camera_feed_layout import *

image_classifier = cv2.CascadeClassifier('classifier.xml')
video_feed = cv2.VideoCapture(0)


def get_profile(s_id, s_name):
    try:
        connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
        db_cursor = connection.cursor()
        db_cursor.execute("SELECT s_id, s_name FROM student WHERE s_id = '" + str(s_id) + "' AND s_name = '"
                          + str(s_name) + "'")
        query_result = db_cursor.fetchone()

        if query_result is None:
            db_cursor.execute("INSERT INTO student(s_id, s_name) VALUES(" + s_id + ", '" + str(s_name) + "')")
            create_dataset()
        else:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Exception caught!")
            messageBox.setText("User already exists!")
            messageBox.setIcon(QMessageBox.Critical)

        connection.commit()
        connection.close()
    except Exception as e:
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Exception caught!")
        messageBox.setText(str(e))
        messageBox.setIcon(QMessageBox.Critical)

student_id = input("Enter User ID: ")
student_name = input("Enter Username: ")
get_profile(student_id, student_name)


def create_dataset():
    image_version = 0
    while True:
        ret, image = video_feed.read()
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = image_classifier.detectMultiScale(grayscale_image, 1.3, 5)
        for(x, y, w, h) in faces:
            cv2.imwrite("dataset/" + str(student_name) + "." + str(student_id) + ".version." + str(image_version) + ".jpg", grayscale_image[y:y + h, x:x + w])
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            image_version = image_version + 1
            cv2.waitKey(100)
        cv2.imshow("Face", image)
        cv2.waitKey(1)
        if image_version > 20:
            break

    video_feed.release()
    cv2.destroyAllWindows()

