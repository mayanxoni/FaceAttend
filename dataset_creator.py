import sys

import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox


class datasetCreator(object):

    def __init__(self):
        self.image_classifier = cv2.CascadeClassifier('classifier.xml')
        self.video_feed = cv2.VideoCapture(0)

    def setupUi(self, form_dataset_creator):
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
        self.button_capture.setObjectName("button_capture")
        self.verticalLayout.addWidget(self.button_capture)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(form_dataset_creator)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(form_dataset_creator)
        self.button_capture.clicked.connect(self.get_profile)

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
            # height, width, channel = image.shape
            # step = channel * width
            q_image = QImage(image, image.shape[1], image.shape[0], image.strides[0], QImage.Format_RGB888)
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.image_classifier.detectMultiScale(image, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.imwrite("dataset/" + str(s_enroll) + ".v" + str(image_version) + ".jpg", grayscale_image[y:y + h, x:x + w])
                # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                image_version = image_version + 1
                # cv2.waitKey(100)
            self.label_camera_feed.setPixmap(QPixmap.fromImage(q_image))
            # cv2.imshow("Face", image)
            # cv2.waitKey(1)
            if image_version > 20:
                self.video_feed.release()
                break


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dataset = QtWidgets.QWidget()
    dataset_creator = datasetCreator()
    dataset_creator.setupUi(dataset)
    dataset.show()

    sys.exit(app.exec_())