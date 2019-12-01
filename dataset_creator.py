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

        self.timer.timeout.connect(self.viewCam)
        self.button_capture.clicked.connect(self.controlTimer)

        try:
            connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
            db_cursor = connection.cursor()
            db_cursor.execute("SELECT s_enroll FROM studentdetails")
            query_result = db_cursor.fetchall()
            for row in query_result:
                print(str(row[0]))
                self.comboBox.addItem(str(row[0]))

        except Exception as e:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Exception caught!")
            messageBox.setText(str(e))
            messageBox.setIcon(QMessageBox.Critical)

    def viewCam(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.label_camera_feed.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            self.button_capture.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.button_capture.setText("Start")

    def retranslateUi(self, form_dataset_creator):
        _translate = QtCore.QCoreApplication.translate
        self.label_camera_feed.setText(_translate("form_dataset_creator", "To start live camera feed, click \"Capture\" button."))
        self.button_capture.setText(_translate("form_dataset_creator", "Capture"))

    # def get_profile(s_id, s_name):
    def get_profile(self):
        s_enroll = self.comboBox.currentText()
        print(s_enroll)
        try:
            self.create_dataset(s_enroll)
        except Exception as e:
            print(str(e))

    def create_dataset(self, s_enroll):
        image_version = 0
        while True:
            ret, image = self.video_feed.read()
            q_image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
            self.label_camera_feed.setPixmap(QPixmap.fromImage(q_image))
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.image_classifier.detectMultiScale(image, 1.3, 5)
            assure_path_exists('dataset/')
            for (x, y, w, h) in faces:
                cv2.imwrite("dataset/" + str(s_enroll) + "." + str(image_version) + ".jpg", grayscale_image[y:y + h, x:x + w])
                # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                image_version = image_version + 1
                # cv2.waitKey(100)
            # cv2.imshow("Face", image)
            # cv2.waitKey(1)
            if image_version > 100:
                self.video_feed.release()
                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dataset = QtWidgets.QWidget()
    dataset_creator = datasetCreator()
    dataset_creator.setupUi(dataset)
    dataset.show()

    sys.exit(app.exec_())
