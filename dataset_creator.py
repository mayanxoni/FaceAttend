import os
import sys

import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox


def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


class datasetCreator(object):

    def __init__(self):
        self.image_version = 0
        self.s_name = None
        self.classifier_path = "classifier.xml"
        self.image_classifier = cv2.CascadeClassifier(self.classifier_path)
        self.video_feed = cv2.VideoCapture(0)


    def setupUi(self, form_dataset_creator):
        form_dataset_creator.setObjectName("form_dataset_creator")
        form_dataset_creator.resize(720, 480)
        form_dataset_creator.setFixedSize(720, 480)
        form_dataset_creator.setWindowTitle("Dataset Creator")
        icon = QtGui.QIcon()
        self.timer = QTimer()
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
        self.button_capture.setObjectName("button_capture")
        self.verticalLayout.addWidget(self.button_capture)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(form_dataset_creator)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(form_dataset_creator)
        # self.button_capture.clicked.connect(self.get_profile)

        assure_path_exists('dataset/')
        self.timer.timeout.connect(self.viewCam)
        self.button_capture.clicked.connect(self.controlTimer)

        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
            self.db_cursor = self.connection.cursor()
            self.db_cursor.execute("SELECT s_enroll FROM studentdetails")
            self.query_result = self.db_cursor.fetchall()
            for row in self.query_result:
                print(str(row[0]))
                self.comboBox.addItem(str(row[0]))

        except Exception as e:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Exception caught!")
            messageBox.setText(str(e))
            messageBox.setIcon(QMessageBox.Critical)

    def viewCam(self):
        self.db_cursor.execute("SELECT s_roll FROM studentdetails WHERE s_enroll = " + (str(self.comboBox.currentText())))
        self.query_result1 = self.db_cursor.fetchall()
        for row1 in self.query_result1:
            print(str(row1[0]))
            self.s_name = str(row1[0])
        ret, image = self.video_feed.read()
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.label_camera_feed.setPixmap(QPixmap.fromImage(qImg))
        faces = self.image_classifier.detectMultiScale(gray_image, 1.3, 5)
        for (x, y, w, h) in faces:
            print(str(self.s_name) + " " + str(self.image_version))
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imwrite("dataset/" + str(self.s_name) + "." + str(self.image_version) + ".jpg", gray_image[y:y + h, x:x + w])
            self.image_version = self.image_version + 1

    def controlTimer(self):
        if not self.timer.isActive():
            self.timer.start(20)
            self.button_capture.setText("Stop")
            self.button_capture.hide()
            self.comboBox.hide()
        else:
            self.timer.stop()
            self.video_feed.release()
            self.button_capture.setText("Start")

    def retranslateUi(self, form_dataset_creator):
        _translate = QtCore.QCoreApplication.translate
        self.label_camera_feed.setText(_translate("form_dataset_creator", "To start live camera feed, click \"Capture\" button.\nClose the window when you're done training the model."))
        self.button_capture.setText(_translate("form_dataset_creator", "Capture"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dataset = QtWidgets.QWidget()
    dataset_creator = datasetCreator()
    dataset_creator.setupUi(dataset)
    dataset.show()

    sys.exit(app.exec_())
