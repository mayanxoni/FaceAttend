import cv2
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class AutomaticAttendance(object):

    def __init__(self,UserName, Subject, Semester,Record,automatic):
        self.UserName = UserName
        self.Subject = Subject
        self.Semester = Semester
        self.record = Record
        self.automatic = automatic
        self.classifier_path = "classifier.xml"
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.image_classifier = cv2.CascadeClassifier(self.classifier_path)
        self.recognizer.read("trainer/trainer.yml")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.return_value = None

        """STRINGS"""
        self.stop = "Stop"
        self.failsafe_warning = "Sorry, no unregistered student found.\n\nIf this seems strange to you, " \
                                "please contact system administrator,\nand go back to Dashboard. "
        self.success_message = "Attendance recorded!"
        self.default_label = "To start live camera feed, click \"Capture\" button.\n\nPLEASE BE AWARE BEFORE CLICKING " \
                             "\"Capture\". YOU CAN ONLY CLICK THAT BUTTON ONCE FOR TODAY."
        self.button_dashboard_text = "Dashboard"
        self.button_capture_text = "Capture"
        self.last_text = "Attendance is already recorded for today.\nPlease come back tomorrow!"

    def setupUi(self, form_camera_feed):
        self.timer = QTimer()
        form_camera_feed.setObjectName("form_camera_feed")
        form_camera_feed.resize(720, 480)
        form_camera_feed.setFixedSize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.button_dashboard.setToolTip("Go back to dashboard.")
        self.button_capture = QtWidgets.QPushButton(form_camera_feed)
        self.layout_vertical.addWidget(self.button_capture)
        self.layout_vertical.addWidget(self.button_dashboard)
        self.button_capture.setObjectName("button_capture")
        self.button_capture.setToolTip("Please read the instructions carefully!")
        self.horizontalLayout.addLayout(self.layout_vertical)
        form_camera_feed.setWindowTitle("Automatic Attendance")
        self.label_camera_feed.setText(self.default_label)
        self.button_dashboard.setText(self.button_dashboard_text)
        self.button_capture.setText(self.button_capture_text)
        self.timer.timeout.connect(self.view_cam)
        self.button_capture.clicked.connect(self.control_timer)
        self.button_dashboard.clicked.connect(self.BackToDashboard)
        QtCore.QMetaObject.connectSlotsByName(form_camera_feed)
        self.connect_db()
        self.students_list = []
        self.non_duplicate_list = []
        self.sorted_list = []

    def connect_db(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="collegeattend"
            )
            self.db_cursor = self.connection.cursor()
            check_query = "SELECT * FROM "+self.Subject+" WHERE classdate = (SELECT CURDATE())"
            self.db_cursor.execute(check_query)
            check_result = self.db_cursor.fetchall()
            if check_result:
                self.label_camera_feed.setText(self.last_text)
                self.button_capture.hide()

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
            insert_query = "INSERT INTO `"+self.Subject+"` VALUES (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, (SELECT CURDATE()))"
            self.db_cursor.execute(insert_query)
            self.connection.commit()
            for num in self.students_list:
                if num not in self.non_duplicate_list:
                    self.non_duplicate_list.append(num)
            self.sorted_list = sorted(self.non_duplicate_list)
            print(self.sorted_list)
            self.alert_box()
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

    def main_logic(self):
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.faces = self.image_classifier.detectMultiScale(self.gray_image, 1.2, 5)
        for (x, y, w, h) in self.faces:
            enroll_no, confidence = self.recognizer.predict(self.gray_image[y:y + h, x:x + w])
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            print(str(enroll_no))
            roll_no = self.validate_roll_no(enroll_no)
            self.students_list.append(roll_no)

    def validate_roll_no(self, enroll):
        print(str(enroll))
        self.db_cursor.execute("SELECT rollnum FROM studentdetails WHERE enrollement = " + str(enroll) + " and  semester = '"+self.Semester+"'")
        query_result = self.db_cursor.fetchone()
        for row in query_result:
            self.return_value = row
        print(self.return_value)
        return self.return_value

    def alert_box(self):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setText("Attendance has been recorded for today. Please verify the attendance and scrutinise it using "
                      "the Update menu from Dashboard if there is any scope of it.")
        alert.setWindowTitle("Attendance recorded successfully successfully!")
        alert.setStandardButtons(QMessageBox.Ok)
        return_value = alert.exec()
        if return_value == QMessageBox.Ok:
            current_item = 0
            while current_item < len(self.sorted_list):
                update_query = "UPDATE `"+self.Subject+"` SET `" + str(self.sorted_list[current_item]) + "` = 1 WHERE `classdate` = (SELECT CURDATE())"
                self.db_cursor.execute(update_query)
                self.connection.commit()
                current_item += 1

    def BackToDashboard(self):
        self.automatic.close()
        self.record.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_camera_feed = QtWidgets.QWidget()
    ui = AutomaticAttendance()
    ui.setupUi(form_camera_feed)
    form_camera_feed.show()
    sys.exit(app.exec_())
