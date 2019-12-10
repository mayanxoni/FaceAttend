import os
import sys

import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox


class datasetCreator(object):

    def __init__(self):
        self.image = None
        self.image_version = 0
        self.classifier_path = "classifier.xml"
        self.image_classifier = cv2.CascadeClassifier(self.classifier_path)

    def setupUi(self, form_dataset_creator):
        self.timer = QTimer()
        form_dataset_creator.setObjectName("form_dataset_creator")
        form_dataset_creator.resize(720, 480)
        form_dataset_creator.setFixedSize(720, 480)
        form_dataset_creator.setWindowTitle("Dataset Creator")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/FaceAttend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label_camera_feed.setText("To start live camera feed, click \"Capture\" button.\nClose the window when you're done training the model.")
        self.button_dashboard.setText("Go to Dashboard")
        self.button_capture.setText("Capture")
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(form_dataset_creator)
        self.timer.timeout.connect(self.view_cam)
        self.button_capture.clicked.connect(self.controlTimer)
        self.connect_db()
        self.fetch_enroll()

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
            self.db_cursor = self.connection.cursor()

        except Exception as e:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Exception Caught!")
            messageBox.setText(str(e))
            messageBox.setIcon(QMessageBox.Critical)

    def fetch_enroll(self):
        self.s_enroll_query = "SELECT s_enroll FROM studentdetails"
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
            self.camera_feed = cv2.VideoCapture(0)
            self.timer.start(1)
            self.button_capture.setText("Stop")
            self.comboBox.hide()
            self.button_dashboard.hide()
        else:
            self.timer.stop()
            self.camera_feed.release()
            self.button_dashboard.show()
            self.button_capture.hide()

    def main_logic(self):
        self.db_cursor.execute("SELECT s_roll FROM studentdetails WHERE s_enroll = " + (str(self.comboBox.currentText())))
        self.query_result1 = self.db_cursor.fetchall()

        for row1 in self.query_result1:
            self.s_roll = str(row1[0])
        faces = self.image_classifier.detectMultiScale(self.image, 1.3, 5)
        for (x, y, w, h) in faces:
            print(str(self.s_roll) + " " + str(self.image_version))
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imwrite("dataset/" + str(self.s_roll) + "." + str(self.image_version) + ".jpg", self.image[y:y + h, x:x + w])
            self.image_version = self.image_version + 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dataset = QtWidgets.QWidget()
    dataset_creator = datasetCreator()
    dataset_creator.setupUi(dataset)
    dataset.show()

    sys.exit(app.exec_())
