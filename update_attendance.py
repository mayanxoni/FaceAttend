import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from error_message import ErrorMessage


class UpdateAttendance(object):

    def __init__(self, user_name, semester, subject, date):
        self.user_name = user_name
        self.semester = semester
        self.subject = subject
        self.date = date

    def setup_ui(self, update_attendance_object):
        update_attendance_object.setObjectName("update_attendance_object")
        update_attendance_object.resize(905, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        update_attendance_object.setWindowIcon(icon)
        self.grid_layout = QtWidgets.QGridLayout(update_attendance_object)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout_1 = QtWidgets.QGridLayout()
        self.grid_layout_1.setObjectName("grid_layout_1")
        self.button_back = QtWidgets.QPushButton(update_attendance_object)
        self.button_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon1)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.grid_layout_1.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_update_attendance = QtWidgets.QLabel(update_attendance_object)
        self.label_update_attendance.setObjectName("label_update_attendance")
        self.grid_layout_1.addWidget(self.label_update_attendance, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_spacer = QtWidgets.QLabel(update_attendance_object)
        self.label_spacer.setText("")
        self.label_spacer.setObjectName("label_spacer")
        self.grid_layout_1.addWidget(self.label_spacer, 0, 2, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_1, 0, 0, 1, 3)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.vertical_layout_3.setObjectName("vertical_layout_3")
        self.checkbox_3 = QtWidgets.QCheckBox(update_attendance_object)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkbox_3.setIcon(icon2)
        self.checkbox_3.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_3.setObjectName("checkbox_3")
        self.vertical_layout_3.addWidget(self.checkbox_3)
        self.label_3 = QtWidgets.QLabel(update_attendance_object)
        self.label_3.setObjectName("label_3")
        self.vertical_layout_3.addWidget(self.label_3)
        self.grid_layout_2.addLayout(self.vertical_layout_3, 0, 4, 1, 1)
        self.vertical_layout_8 = QtWidgets.QVBoxLayout()
        self.vertical_layout_8.setObjectName("vertical_layout_8")
        self.checkbox_8 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_8.setIcon(icon2)
        self.checkbox_8.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_8.setObjectName("checkbox_8")
        self.vertical_layout_8.addWidget(self.checkbox_8)
        self.label_8 = QtWidgets.QLabel(update_attendance_object)
        self.label_8.setObjectName("label_8")
        self.vertical_layout_8.addWidget(self.label_8)
        self.grid_layout_2.addLayout(self.vertical_layout_8, 2, 4, 1, 1)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.checkbox_2 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_2.setIcon(icon2)
        self.checkbox_2.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_2.setObjectName("checkbox_2")
        self.vertical_layout_2.addWidget(self.checkbox_2)
        self.label_2 = QtWidgets.QLabel(update_attendance_object)
        self.label_2.setObjectName("label_2")
        self.vertical_layout_2.addWidget(self.label_2)
        self.grid_layout_2.addLayout(self.vertical_layout_2, 0, 2, 1, 1)
        self.vertical_layout_7 = QtWidgets.QVBoxLayout()
        self.vertical_layout_7.setObjectName("vertical_layout_7")
        self.checkbox_7 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_7.setIcon(icon2)
        self.checkbox_7.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_7.setObjectName("checkbox_7")
        self.vertical_layout_7.addWidget(self.checkbox_7)
        self.label_7 = QtWidgets.QLabel(update_attendance_object)
        self.label_7.setObjectName("label_7")
        self.vertical_layout_7.addWidget(self.label_7)
        self.grid_layout_2.addLayout(self.vertical_layout_7, 2, 2, 1, 1)
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.checkbox_1 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_1.setIcon(icon2)
        self.checkbox_1.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_1.setObjectName("checkbox_1")
        self.vertical_layout_1.addWidget(self.checkbox_1)
        self.label_1 = QtWidgets.QLabel(update_attendance_object)
        self.label_1.setObjectName("label_1")
        self.vertical_layout_1.addWidget(self.label_1)
        self.grid_layout_2.addLayout(self.vertical_layout_1, 0, 0, 1, 1)
        self.vertical_layout_5 = QtWidgets.QVBoxLayout()
        self.vertical_layout_5.setObjectName("vertical_layout_5")
        self.checkbox_5 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_5.setIcon(icon2)
        self.checkbox_5.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_5.setObjectName("checkbox_5")
        self.vertical_layout_5.addWidget(self.checkbox_5)
        self.label_5 = QtWidgets.QLabel(update_attendance_object)
        self.label_5.setObjectName("label_5")
        self.vertical_layout_5.addWidget(self.label_5)
        self.grid_layout_2.addLayout(self.vertical_layout_5, 0, 8, 1, 1)
        self.v_line_4 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_4.setObjectName("v_line_4")
        self.grid_layout_2.addWidget(self.v_line_4, 0, 7, 1, 1)
        self.h_line_1 = QtWidgets.QFrame(update_attendance_object)
        self.h_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_1.setObjectName("h_line_1")
        self.grid_layout_2.addWidget(self.h_line_1, 1, 0, 1, 1)
        self.vertical_layout_10 = QtWidgets.QVBoxLayout()
        self.vertical_layout_10.setObjectName("vertical_layout_10")
        self.checkbox_10 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_10.setIcon(icon2)
        self.checkbox_10.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_10.setObjectName("checkbox_10")
        self.vertical_layout_10.addWidget(self.checkbox_10)
        self.label_10 = QtWidgets.QLabel(update_attendance_object)
        self.label_10.setObjectName("label_10")
        self.vertical_layout_10.addWidget(self.label_10)
        self.grid_layout_2.addLayout(self.vertical_layout_10, 2, 8, 1, 1)
        self.vertical_layout_4 = QtWidgets.QVBoxLayout()
        self.vertical_layout_4.setObjectName("vertical_layout_4")
        self.checkbox_4 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_4.setIcon(icon2)
        self.checkbox_4.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_4.setObjectName("checkbox_4")
        self.vertical_layout_4.addWidget(self.checkbox_4)
        self.label_4 = QtWidgets.QLabel(update_attendance_object)
        self.label_4.setObjectName("label_4")
        self.vertical_layout_4.addWidget(self.label_4)
        self.grid_layout_2.addLayout(self.vertical_layout_4, 0, 6, 1, 1)
        self.v_line_1 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_1.setObjectName("v_line_1")
        self.grid_layout_2.addWidget(self.v_line_1, 0, 1, 1, 1)
        self.vertical_layout_9 = QtWidgets.QVBoxLayout()
        self.vertical_layout_9.setObjectName("vertical_layout_9")
        self.checkbox_9 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_9.setIcon(icon2)
        self.checkbox_9.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_9.setObjectName("checkbox_9")
        self.vertical_layout_9.addWidget(self.checkbox_9)
        self.label_9 = QtWidgets.QLabel(update_attendance_object)
        self.label_9.setObjectName("label_9")
        self.vertical_layout_9.addWidget(self.label_9)
        self.grid_layout_2.addLayout(self.vertical_layout_9, 2, 6, 1, 1)
        self.v_line_5 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_5.setObjectName("v_line_5")
        self.grid_layout_2.addWidget(self.v_line_5, 2, 1, 1, 1)
        self.vertical_layout_6 = QtWidgets.QVBoxLayout()
        self.vertical_layout_6.setObjectName("vertical_layout_6")
        self.checkbox_6 = QtWidgets.QCheckBox(update_attendance_object)
        self.checkbox_6.setIcon(icon2)
        self.checkbox_6.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_6.setObjectName("checkbox_6")
        self.vertical_layout_6.addWidget(self.checkbox_6)
        self.label_6 = QtWidgets.QLabel(update_attendance_object)
        self.label_6.setObjectName("label_6")
        self.vertical_layout_6.addWidget(self.label_6)
        self.grid_layout_2.addLayout(self.vertical_layout_6, 2, 0, 1, 1)
        self.v_line_7 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_7.setObjectName("v_line_7")
        self.grid_layout_2.addWidget(self.v_line_7, 2, 5, 1, 1)
        self.v_line_3 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_3.setObjectName("v_line_3")
        self.grid_layout_2.addWidget(self.v_line_3, 0, 5, 1, 1)
        self.v_line_6 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_6.setObjectName("v_line_6")
        self.grid_layout_2.addWidget(self.v_line_6, 2, 3, 1, 1)
        self.v_line_2 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_2.setObjectName("v_line_2")
        self.grid_layout_2.addWidget(self.v_line_2, 0, 3, 1, 1)
        self.v_line_8 = QtWidgets.QFrame(update_attendance_object)
        self.v_line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_8.setObjectName("v_line_8")
        self.grid_layout_2.addWidget(self.v_line_8, 2, 7, 1, 1)
        self.h_line_2 = QtWidgets.QFrame(update_attendance_object)
        self.h_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_2.setObjectName("h_line_2")
        self.grid_layout_2.addWidget(self.h_line_2, 1, 2, 1, 1)
        self.h_line_3 = QtWidgets.QFrame(update_attendance_object)
        self.h_line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_3.setObjectName("h_line_3")
        self.grid_layout_2.addWidget(self.h_line_3, 1, 4, 1, 1)
        self.h_line_4 = QtWidgets.QFrame(update_attendance_object)
        self.h_line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_4.setObjectName("h_line_4")
        self.grid_layout_2.addWidget(self.h_line_4, 1, 6, 1, 1)
        self.h_line_5 = QtWidgets.QFrame(update_attendance_object)
        self.h_line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_5.setObjectName("h_line_5")
        self.grid_layout_2.addWidget(self.h_line_5, 1, 8, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 10, 0, 2, 3)
        self.button_update = QtWidgets.QPushButton(update_attendance_object)
        self.button_update.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon3)
        self.button_update.setIconSize(QtCore.QSize(32, 32))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.grid_layout.addWidget(self.button_update, 13, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_update_icon = QtWidgets.QLabel(update_attendance_object)
        self.label_update_icon.setText("")
        self.label_update_icon.setPixmap(QtGui.QPixmap("assets/reload.png"))
        self.label_update_icon.setScaledContents(True)
        self.label_update_icon.setObjectName("label_update_icon")
        self.grid_layout.addWidget(self.label_update_icon, 8, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_placeholder = QtWidgets.QLabel(update_attendance_object)
        self.label_placeholder.setObjectName("label_placeholder")
        self.grid_layout.addWidget(self.label_placeholder, 9, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        update_attendance_object.setWindowTitle("Performance Analysis")
        self.label_update_attendance.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; "
                                             "font-weight:600; color:#888a85;\">UPDATE "
                                             "ATTENDANCE</span></p></body></html>")
        self.checkbox_3.setText("CheckBox")
        self.label_3.setText("TextLabel")
        self.checkbox_8.setText("CheckBox")
        self.label_8.setText("TextLabel")
        self.checkbox_2.setText("CheckBox")
        self.label_2.setText("TextLabel")
        self.checkbox_7.setText("CheckBox")
        self.label_7.setText("TextLabel")
        self.checkbox_1.setText("CheckBox")
        self.label_1.setText("TextLabel")
        self.checkbox_5.setText("CheckBox")
        self.label_5.setText("TextLabel")
        self.checkbox_10.setText("CheckBox")
        self.label_10.setText("TextLabel")
        self.checkbox_4.setText("CheckBox")
        self.label_4.setText("TextLabel")
        self.checkbox_9.setText("CheckBox")
        self.label_9.setText("TextLabel")
        self.checkbox_6.setText("CheckBox")
        self.label_6.setText("TextLabel")
        self.label_placeholder.setText(
            "Check or uncheck the boxes to change the status of the attendance record of the student:")

        self.hide()
        self.load_attendance()
        self.load_data()
        self.check_box_list[0].stateChanged.connect(lambda: self.check_attendance(0))
        self.check_box_list[1].stateChanged.connect(lambda: self.check_attendance(1))
        self.check_box_list[2].stateChanged.connect(lambda: self.check_attendance(2))
        self.check_box_list[3].stateChanged.connect(lambda: self.check_attendance(3))
        self.check_box_list[4].stateChanged.connect(lambda: self.check_attendance(4))
        self.check_box_list[5].stateChanged.connect(lambda: self.check_attendance(5))
        self.check_box_list[6].stateChanged.connect(lambda: self.check_attendance(6))
        self.check_box_list[7].stateChanged.connect(lambda: self.check_attendance(7))
        self.check_box_list[8].stateChanged.connect(lambda: self.check_attendance(8))
        self.check_box_list[9].stateChanged.connect(lambda: self.check_attendance(9))
        self.button_update.clicked.connect(lambda: self.FuncUpdateAttend(update_attendance_object))
        self.button_back.clicked.connect(lambda: self.back(update_attendance_object))

        QtCore.QMetaObject.connectSlotsByName(update_attendance_object)
        update_attendance_object.setTabOrder(self.checkbox_1, self.checkbox_2)
        update_attendance_object.setTabOrder(self.checkbox_2, self.checkbox_3)
        update_attendance_object.setTabOrder(self.checkbox_3, self.checkbox_4)
        update_attendance_object.setTabOrder(self.checkbox_4, self.checkbox_5)
        update_attendance_object.setTabOrder(self.checkbox_5, self.checkbox_6)
        update_attendance_object.setTabOrder(self.checkbox_6, self.checkbox_7)
        update_attendance_object.setTabOrder(self.checkbox_7, self.checkbox_8)
        update_attendance_object.setTabOrder(self.checkbox_8, self.checkbox_9)
        update_attendance_object.setTabOrder(self.checkbox_9, self.checkbox_10)
        update_attendance_object.setTabOrder(self.checkbox_10, self.button_update)
        update_attendance_object.setTabOrder(self.button_update, self.button_back)

        self.check_box_list = [self.checkbox_1, self.checkbox_2, self.checkbox_3, self.checkbox_4, self.checkbox_5,
                               self.checkbox_6,
                               self.checkbox_7, self.checkbox_8, self.checkbox_9, self.checkbox_10]
        self.roll_list = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,
                          self.label_7, self.label_8, self.label_9, self.label_10]
        self.attendance_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def hide(self):
        for i in range(10):
            self.check_box_list[i].hide()
            self.roll_list[i].hide()

    def load_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            details_query = "SELECT rollnum,name,pic FROM studentdetails WHERE  semester = " + self.semester + \
                            " order by rollnum"
            db_cursor.execute(details_query)
            details_result = db_cursor.fetchall()
            if details_result is None:
                self.error_report(str("No Students in this semester"))
            else:
                i = 0
                pixmap_list = []
                name_list = []
                for row in details_result:
                    pixmap_list.append(QPixmap("pic/" + row[2]))
                    self.icon4 = QtGui.QIcon()
                    self.icon4.addPixmap(pixmap_list[i], QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.check_box_list[i].setIcon(self.icon4)
                    roll = row[0]
                    name = row[1]
                    name_list.append(roll + '. ' + name)
                    print(name_list[i])
                    self.roll_list[i].setText(name_list[i])
                    self.check_box_list[i].show()
                    self.roll_list[i].show()
                    i = i + 1
        except mysql.connector.Error as err:
            self.error_report(format(err))

    def load_attendance(self):
        db = mysql.connector.connect(
            host="localhost",
            database="collegeattend",
            user="root",
            passwd=""
        )
        cursor = db.cursor()
        chosen_date_query = "SELECT * FROM `" + str(self.subject) + "` WHERE  classdate = " + self.date
        cursor.execute(chosen_date_query)
        chosen_date_result = cursor.fetchall()
        for i in chosen_date_result:
            for j in range(5):
                self.attendance_list[j] = i[j]
                print(str(self.attendance_list[j]))
                if self.attendance_list[j] == 1:
                    self.check_box_list[j].setText("Is Present")
                    self.check_box_list[j].setStyleSheet("color: Green")
                    self.check_box_list[j].setChecked(True)
                else:
                    self.check_box_list[j].setText("Is Absent")
                    self.check_box_list[j].setStyleSheet("color: red")

    def check_attendance(self, x):
        if self.check_box_list[x].isChecked():
            self.check_box_list[x].setText("Is Present")
            self.check_box_list[x].setStyleSheet("color: Green")
            self.attendance_list[x] = 1
        else:
            self.check_box_list[x].setText("Is Absent")
            self.check_box_list[x].setStyleSheet("color: red")
            self.attendance_list[x] = 0

    def FuncUpdateAttend(self, update_attendance):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='collegeattend',
                                                 user='root',
                                                 password='')
            db_cursor = connection.cursor()
            update_query = "UPDATE `" + str(self.subject) + "` SET `1` = " + self.attendance_list[0] + ", `2` = " + \
                           self.attendance_list[1] + ", `3` = " + self.attendance_list[2] + ", `4` = " + \
                           self.attendance_list[3] + ", `5` = " + self.attendance_list[4] + ", `6` = " + \
                           self.attendance_list[5] + ", `7` = " + self.attendance_list[6] + ", `8` = " + \
                           self.attendance_list[7] + ", `9` = " + self.attendance_list[8] + ", `10` = " + \
                           self.attendance_list[9] + ", `classdate` = " + self.date + ")"
            db_cursor.execute(update_query)
            connection.commit()
            update_attendance.close()
            print("Record successfully inserted into " + str(self.subject) + "table")
        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

    @staticmethod
    def back(update_attendance):
        update_attendance.close()

    def error_report(self, message):
        message_box = QtWidgets.QMessageBox()
        ui = ErrorMessage(message)
        ui.setup_ui(message_box)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    update_attendance_object = QtWidgets.QWidget()
    update_attendance = UpdateAttendance()
    update_attendance.setup_ui(update_attendance_object)
    update_attendance_object.show()
    sys._excepthook = sys.excepthook


    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook
    sys.exit(app.exec_())
