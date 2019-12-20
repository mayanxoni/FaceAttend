import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from error_message import ErrorMessage
from automatic_attendance import AutomaticAttendance
from manual_attendance import ManualAttendance


class RecordAttendance(object):

    def __init__(self, user_name):
        # self.dash = Dashboard()
        self.user_name = user_name

    def setup_ui(self, record_attendance_object):
        record_attendance_object.setObjectName("record_attendance_object")
        record_attendance_object.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        record_attendance_object.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(record_attendance_object)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.button_back = QtWidgets.QPushButton(record_attendance_object)
        self.button_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon1)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.grid_layout.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.grid_layout)
        self.label_record_attendance = QtWidgets.QLabel(record_attendance_object)
        self.label_record_attendance.setObjectName("label_record_attendance")
        self.verticalLayout.addWidget(self.label_record_attendance)
        self.label_attendance_icon = QtWidgets.QLabel(record_attendance_object)
        self.label_attendance_icon.setText("")
        self.label_attendance_icon.setPixmap(QtGui.QPixmap("assets/register.png"))
        self.label_attendance_icon.setObjectName("label_attendance_icon")
        self.verticalLayout.addWidget(self.label_attendance_icon, 0, QtCore.Qt.AlignHCenter)
        self.label_placeholder_1 = QtWidgets.QLabel(record_attendance_object)
        self.label_placeholder_1.setObjectName("label_placeholder_1")
        self.verticalLayout.addWidget(self.label_placeholder_1, 0, QtCore.Qt.AlignHCenter)
        self.combo_box_teacher_id = QtWidgets.QComboBox(record_attendance_object)
        self.combo_box_teacher_id.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.combo_box_teacher_id)
        self.label_placeholder_2 = QtWidgets.QLabel(record_attendance_object)
        self.label_placeholder_2.setObjectName("label_placeholder_2")
        self.verticalLayout.addWidget(self.label_placeholder_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.button_take_manual = QtWidgets.QPushButton(record_attendance_object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_take_manual.sizePolicy().hasHeightForWidth())
        self.button_take_manual.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_take_manual.setIcon(icon2)
        self.button_take_manual.setIconSize(QtCore.QSize(64, 64))
        self.button_take_manual.setObjectName("button_take_manual")
        self.horizontal_layout.addWidget(self.button_take_manual)
        self.divider_line = QtWidgets.QFrame(record_attendance_object)
        self.divider_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.divider_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_line.setObjectName("divider_line")
        self.horizontal_layout.addWidget(self.divider_line)
        self.button_take_auto = QtWidgets.QPushButton(record_attendance_object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_take_auto.sizePolicy().hasHeightForWidth())
        self.button_take_auto.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/camera_capture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_take_auto.setIcon(icon3)
        self.button_take_auto.setIconSize(QtCore.QSize(64, 64))
        self.button_take_auto.setFlat(False)
        self.button_take_auto.setObjectName("button_take_auto")
        self.horizontal_layout.addWidget(self.button_take_auto)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.label_spacer_bottom = QtWidgets.QLabel(record_attendance_object)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.verticalLayout.addWidget(self.label_spacer_bottom)
        self.label_spacer_bottom.raise_()
        self.label_record_attendance.raise_()
        self.label_attendance_icon.raise_()
        self.combo_box_teacher_id.raise_()
        self.label_placeholder_1.raise_()
        self.label_placeholder_2.raise_()

        record_attendance_object.setWindowTitle("Record Attendance")
        self.label_record_attendance.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; "
                                             "font-weight:600; color:#888a85;\">RECORD "
                                             "ATTENDANCE</span></p></body></html>")
        self.label_placeholder_1.setText("Select the subject for which you wish to record attendance:")
        self.label_placeholder_2.setText("Select the mode of attendance you prefer:")
        self.button_take_manual.setToolTip("Subject Allotment")
        self.button_take_manual.setText("Manual Attendance")
        self.button_take_auto.setToolTip("Performance Analysis")
        self.button_take_auto.setText("Automatic Attendance")

        self.load_subject()
        # self.selected_subject()
        QtCore.QMetaObject.connectSlotsByName(record_attendance_object)
        record_attendance_object.setTabOrder(self.button_take_manual, self.button_take_auto)
        self.button_back.clicked.connect(lambda: self.back(record_attendance_object))
        self.button_take_manual.clicked.connect(self.manual_attendance)
        self.button_take_auto.clicked.connect(self.automatic_attendance)

    def load_subject(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            teacher_id_query = "SELECT * FROM subjectteacher where teacherid = " + self.user_name
            db_cursor.execute(teacher_id_query)
            teacher_id_query = db_cursor.fetchone()
            if teacher_id_query is None:
                self.error_report(str("No subject alloted to you!"))
            else:
                for row in teacher_id_query:
                    if row != self.user_name:
                        if row:
                            self.combo_box_teacher_id.addItem(row)
        except mysql.connector.Error as e:
            print(format(e))

    def selected_subject(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            self.db_cursor = self.connection.cursor()
            semester_query = "SELECT semestername FROM collgdatatable WHERE " + \
                             self.combo_box_teacher_id.currentText + \
                             " IN(subject1, subject2, subject3, subject4, subject5, subject6, subject7)"
            self.db_cursor.execute(semester_query)
            self.semester_result = self.db_cursor.fetchone()
        except mysql.connector.Error as e:
            print(format(e))

    def manual_attendance(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            self.db_cursor = self.connection.cursor()
            semester_query = "SELECT semestername FROM collgdatatable WHERE " + \
                             self.combo_box_teacher_id.currentText + \
                             " IN(subject1, subject2, subject3, subject4, subject5, subject6, subject7)"
            self.db_cursor.execute(semester_query)
            self.semester_result = self.db_cursor.fetchone()
            if self.semester_result is None:
                self.error_report(str("You must select correct subject!"))
            else:
                for self.row in self.semester_result:
                    self.semester = self.row
                    print(self.semester)
                    self.win_manual_attendance = QtWidgets.QWidget()
                    self.ui = ManualAttendance(self.user_name, self.combo_box_teacher_id.currentText(), self.semester)
                    self.ui.setup_ui(self.win_manual_attendance)
                    self.win_manual_attendance.show()
        except mysql.connector.Error as e:
            print(format(e))

    def automatic_attendance(self):
        if self.semester_result is None:
            self.error_report(str("you must select correct subject!"))
        else:
            for self.row in self.semester_result:
                self.semester = self.row
                print(self.semester)
                self.win_auto = QtWidgets.QWidget()
                self.ui = AutomaticAttendance(self.user_name, self.combo_box_teacher_id.currentText(), self.semester)
                self.ui.setup_ui(self.win_auto)
                self.win_auto.show()

    @staticmethod
    def back(record_attendance_object):
        print("Button hit")
        # self.WinDash = QtWidgets.QWidget()
        # self.ui = Dashboard(self.user_name)
        # self.ui.setup_ui(self.WinDash)
        record_attendance_object.hide()
        # self.dash.CallForShow()

        # self.WinDash.show()

    def error_report(self, message):
        message_box = QtWidgets.QMessageBox()
        ui = ErrorMessage(message)
        ui.setup_ui(message_box)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    record_attendance_object = QtWidgets.QWidget()
    record_attendance = RecordAttendance()
    record_attendance.setup_ui(record_attendance_object)
    record_attendance_object.show()
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
