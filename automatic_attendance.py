import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox


class automaticAttendance(object):

    def __init__(self):
        self.classifier_path = "classifier.xml"
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.image_classifier = cv2.CascadeClassifier(self.classifier_path)
        self.recognizer.read("trainer/trainer.yml")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.student_profile = None

        """STRINGS"""
        self.stop = "Stop"
        self.failsafe_warning = "Sorry, no unregistered student found.\n\nIf this seems strange to you, " \
                                "please contact system administrator,\nand go back to Dashboard. "
        self.success_message = "Attendance recorded!"
        self.default_label = "To start live camera feed, click \"Capture\" button."
        self.button_dashboard_text = "Dashboard"
        self.button_capture_text = "Capture"

    def setupUi(self, form_camera_feed):
        self.timer = QTimer()
        form_camera_feed.setObjectName("form_camera_feed")
        form_camera_feed.resize(720, 480)
        form_camera_feed.setFixedSize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/FaceAttend.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_camera_feed.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form_camera_feed)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_vertical = QtWidgets.QVBoxLayout()
        self.layout_vertical.setObjectName("layout_vertical")
        self.label_camera_feed = QtWidgets.QLabel(form_camera_feed)
        self.label_camera_feed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_camera_feed.setObjectName("label_image")
        self.layout_vertical.addWidget(self.label_camera_feed, 0, QtCore.Qt.AlignHCenter)
        self.button_dashboard = QtWidgets.QPushButton(form_camera_feed)
        self.button_dashboard.setObjectName("button_dashboard")
        self.button_capture = QtWidgets.QPushButton(form_camera_feed)
        self.layout_vertical.addWidget(self.button_capture)
        self.layout_vertical.addWidget(self.button_dashboard)
        self.button_capture.setObjectName("button_capture")
        self.horizontalLayout.addLayout(self.layout_vertical)
        form_camera_feed.setWindowTitle("Automatic Attendance")
        self.label_camera_feed.setText(self.default_label)
        self.button_dashboard.setText(self.button_dashboard_text)
        self.button_capture.setText(self.button_capture_text)
        self.timer.timeout.connect(self.view_cam)
        self.button_capture.clicked.connect(self.control_timer)
        QtCore.QMetaObject.connectSlotsByName(form_camera_feed)
        self.connect_db()

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="collegeattend")
            self.db_cursor = self.connection.cursor()

        except Exception as e:
            messageBox = QMessageBox()
            messageBox.setWindowTitle("Exception Caught!")
            messageBox.setText(str(e))
            messageBox.setIcon(QMessageBox.Critical)

    def control_timer(self):
        if not self.timer.isActive():
            self.camera_feed = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.timer.start(1)
            self.button_capture.setText(self.stop)
            self.button_dashboard.hide()
        else:
            self.timer.stop()
            self.camera_feed.release()
            self.label_camera_feed.setText(self.success_message)
            self.button_dashboard.show()
            self.button_capture.hide()

    def view_cam(self):
        ret, self.image = self.camera_feed.read()
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        height, width, channel = self.image.shape
        step = channel * width
        q_img = QImage(self.image.data, width, height, step, QImage.Format_RGB888)
        self.label_camera_feed.setPixmap(QPixmap.fromImage(q_img))
        print("worked1")
        self.main_logic()
        print("worked2")

    def main_logic(self):
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.faces = self.image_classifier.detectMultiScale(self.gray_image, 1.2, 5)
        for (x, y, w, h) in self.faces:
            student_id, confidence = self.recognizer.predict(self.gray_image[y:y + h, x:x + w])
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            profile = self.get_profile(student_id)
            if profile is not None:
                cv2.putText(self.image, profile, (x, y + h + 30), self.font, 1, (0, 0, 255), 3)
                cv2.putText(self.image, "Accuracy: {0:.2f}%".format(round(100 - confidence, 2)), (x, y + h + 60), self.font, 1, (0, 0, 255), 3)

    def get_profile(self, s_roll):
        self.db_cursor.execute("SELECT name FROM studentdetails WHERE enrollement = " + str(s_roll))
        query_result = self.db_cursor.fetchone()
        for row in query_result:
            self.student_profile = row
        return self.student_profile

    def fetch_details(self, student_id):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_camera_feed = QtWidgets.QWidget()
    ui = automaticAttendance()
    ui.setupUi(form_camera_feed)
    form_camera_feed.show()
    sys.exit(app.exec_())
