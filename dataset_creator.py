import os
import sys

import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
import numpy as np
from PIL import Image


class datasetCreator(object):

    def __init__(self,datasetCreator):
        self.datasetCreator = datasetCreator
        self.image = None
        self.image_version = 0
        self.classifier_path = "classifier.xml"
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.image_classifier = cv2.CascadeClassifier(self.classifier_path)

        """STRINGS"""
        self.stop = "Stop"
        self.failsafe_warning = "Sorry, no unregistered student found.\n\nIf this seems strange to you, " \
                                "please contact system administrator,\nand go back to Dashboard. "
        self.success_message = "Dataset created!\nStudent face registered and is ready for attendance."
        self.default_label = "To start live camera feed, click \"Capture\" button.\nClose the window when you're " \
                             "done training the model. "
        self.button_dashboard_text = "Dashboard"
        self.button_capture_text = "Capture"

    def setupUi(self, form_dataset_creator):
        self.timer = QTimer()
        form_dataset_creator.setObjectName("form_dataset_creator")
        form_dataset_creator.resize(720, 480)
        form_dataset_creator.setFixedSize(720, 480)
        form_dataset_creator.setWindowTitle("Dataset Creator")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_dataset_creator.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form_dataset_creator)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(form_dataset_creator)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_camera_feed = QtWidgets.QLabel(form_dataset_creator)
        self.label_camera_feed.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_camera_feed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_camera_feed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camera_feed.setObjectName("label_camera_feed")
        self.verticalLayout.addWidget(self.label_camera_feed)
        self.button_capture = QtWidgets.QPushButton(form_dataset_creator)
        self.button_dashboard = QtWidgets.QPushButton(form_dataset_creator)
        self.button_dashboard.setObjectName("button_dashboard")
        self.button_capture.setObjectName("button_capture")
        self.verticalLayout.addWidget(self.button_capture)
        self.verticalLayout.addWidget(self.button_dashboard)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_camera_feed.setText(self.default_label)
        self.button_dashboard.setText(self.button_dashboard_text)
        self.button_capture.setText(self.button_capture_text)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(form_dataset_creator)
        self.timer.timeout.connect(self.view_cam)
        self.button_capture.clicked.connect(self.controlTimer)
        self.button_dashboard.clicked.connect(self.BackToDashboard)
        self.connect_db()
        self.fetch_enroll()

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", passwd="",
                                                      database="collegeattend")
            self.db_cursor = self.connection.cursor()

        except Exception as e:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Exception Caught!")
            messageBox.setText(str(e))
            messageBox.setIcon(QMessageBox.Critical)

    def fetch_enroll(self):
        self.failsafe_query = "SELECT * FROM unreg_students"
        self.db_cursor.execute(self.failsafe_query)
        self.rows = self.db_cursor.fetchall()
        if not self.rows:
            self.label_camera_feed.setText(self.failsafe_warning)
            self.comboBox.hide()
            self.button_capture.hide()
        else:
            self.s_enroll_query = "SELECT s_enroll FROM unreg_students"
            self.db_cursor.execute(self.s_enroll_query)
            self.query_result = self.db_cursor.fetchall()
            for row in self.query_result:
                print(str(row[0]))
                self.comboBox.addItem(str(row[0]))

    def assure_path_exists(self, path):
        self.directory = os.path.dirname(path)
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def view_cam(self):
        ret, self.image = self.camera_feed.read()
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        height, width, channel = self.image.shape
        step = channel * width
        q_img = QImage(self.image.data, width, height, step, QImage.Format_RGB888)
        self.label_camera_feed.setPixmap(QPixmap.fromImage(q_img))
        self.assure_path_exists("dataset/")
        self.main_logic()

    def controlTimer(self):
        if not self.timer.isActive():
            self.camera_feed = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.timer.start(1)
            self.button_capture.setText(self.stop)
            self.comboBox.hide()
            self.button_dashboard.hide()
        else:
            self.timer.stop()
            self.camera_feed.release()
            self.label_camera_feed.setText(self.success_message)
            self.button_dashboard.show()
            self.button_capture.hide()
            self.faces, self.ids = self.trainer_logic("dataset")
            self.recognizer.train(self.faces, np.array(self.ids))
            self.assure_path_exists("trainer/")
            self.recognizer.save("trainer/trainer.yml")
            delete_query = "DELETE FROM unreg_students WHERE s_enroll = " + self.comboBox.currentText()
            self.db_cursor.execute(delete_query)
            self.connection.commit()

    def main_logic(self):
        self.db_cursor.execute(
            "SELECT enrollement FROM studentdetails WHERE enrollement = " + (str(self.comboBox.currentText())))
        self.query_result1 = self.db_cursor.fetchall()

        for row1 in self.query_result1:
            self.s_roll = str(row1[0])

        self.faces = self.image_classifier.detectMultiScale(self.image, 1.3, 5)
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        for (x, y, w, h) in self.faces:
            print(str(self.s_roll) + " " + str(self.image_version))
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imwrite("dataset/" + str(self.s_roll) + "." + str(self.image_version) + ".jpg",
                        self.gray_image[y:y + h, x:x + w])
            self.image_version = self.image_version + 1

    def trainer_logic(self, path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        list_face_samples = []
        list_id = []
        for image_path in image_paths:
            img_pil = Image.open(image_path).convert('L')
            img_numpy = np.array(img_pil, 'uint8')
            image_id = int(os.path.split(image_path)[-1].split(".")[0])
            print(image_path)
            faces_in_images = self.image_classifier.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces_in_images:
                list_face_samples.append(img_numpy[y:y + h, x:x + w])
                list_id.append(image_id)
        return list_face_samples, list_id

    def BackToDashboard(self):
        self.datasetCreator.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dataset = QtWidgets.QWidget()
    dataset_creator = datasetCreator()
    dataset_creator.setupUi(dataset)
    dataset.show()
    sys.exit(app.exec_())
