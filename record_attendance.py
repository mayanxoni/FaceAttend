# from dashboard import Ui_form_dashboard
from PyQt5 import QtCore, QtGui, QtWidgets
from  manual_attendance import Ui_manual_attendance
import  mysql.connector

from ErrorMessg import Ui_Dialog


class Ui_form_record_attendance(object):
    def __init__(self,UserName):
        # self.dash = Ui_form_dashboard()
        self.UserName =  UserName
    def setupUi(self, form_record_attendance):
        form_record_attendance.setObjectName("form_record_attendance")
        form_record_attendance.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_record_attendance.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(form_record_attendance)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.button_back = QtWidgets.QPushButton(form_record_attendance)
        self.button_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon1)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.grid_layout.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.grid_layout)
        self.label_record_attendance = QtWidgets.QLabel(form_record_attendance)
        self.label_record_attendance.setObjectName("label_record_attendance")
        self.verticalLayout.addWidget(self.label_record_attendance)
        self.label_attendance_icon = QtWidgets.QLabel(form_record_attendance)
        self.label_attendance_icon.setText("")
        self.label_attendance_icon.setPixmap(QtGui.QPixmap("assets/register.png"))
        self.label_attendance_icon.setObjectName("label_attendance_icon")
        self.verticalLayout.addWidget(self.label_attendance_icon, 0, QtCore.Qt.AlignHCenter)
        self.label_placeholder_1 = QtWidgets.QLabel(form_record_attendance)
        self.label_placeholder_1.setObjectName("label_placeholder_1")
        self.verticalLayout.addWidget(self.label_placeholder_1, 0, QtCore.Qt.AlignHCenter)
        self.comboBox = QtWidgets.QComboBox(form_record_attendance)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_placeholder_2 = QtWidgets.QLabel(form_record_attendance)
        self.label_placeholder_2.setObjectName("label_placeholder_2")
        self.verticalLayout.addWidget(self.label_placeholder_2, 0, QtCore.Qt.AlignHCenter)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.button_take_manual = QtWidgets.QPushButton(form_record_attendance)
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
        self.divider_line = QtWidgets.QFrame(form_record_attendance)
        self.divider_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.divider_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_line.setObjectName("divider_line")
        self.horizontal_layout.addWidget(self.divider_line)
        self.button_take_auto = QtWidgets.QPushButton(form_record_attendance)
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
        self.label_spacer_bottom = QtWidgets.QLabel(form_record_attendance)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.verticalLayout.addWidget(self.label_spacer_bottom)
        self.label_spacer_bottom.raise_()
        self.label_record_attendance.raise_()
        self.label_attendance_icon.raise_()
        self.comboBox.raise_()
        self.label_placeholder_1.raise_()
        self.label_placeholder_2.raise_()

        self.retranslateUi(form_record_attendance)
        self.FuncLoadSub()
        QtCore.QMetaObject.connectSlotsByName(form_record_attendance)
        form_record_attendance.setTabOrder(self.button_take_manual, self.button_take_auto)
        self.button_back.clicked.connect(lambda :self.FuncBack(form_record_attendance))
        self.button_take_manual.clicked.connect(self.FuncSelectedSub)


    def retranslateUi(self, form_record_attendance):
        _translate = QtCore.QCoreApplication.translate
        form_record_attendance.setWindowTitle(_translate("form_record_attendance", "Record Attendance"))
        self.label_record_attendance.setText(_translate("form_record_attendance", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#888a85;\">RECORD ATTENDANCE</span></p></body></html>"))
        self.label_placeholder_1.setText(_translate("form_record_attendance", "Select the subject for which you wish to record attendance:"))
        self.label_placeholder_2.setText(_translate("form_record_attendance", "Select the mode of attendance you prefer:"))
        self.button_take_manual.setToolTip(_translate("form_record_attendance", "Subject Allotment"))
        self.button_take_manual.setText(_translate("form_record_attendance", "Manual Attendance"))
        self.button_take_auto.setToolTip(_translate("form_record_attendance", "Performance Analysis"))
        self.button_take_auto.setText(_translate("form_record_attendance", "Automatic Attendance"))

    def FuncLoadSub(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("""SELECT * FROM subjectteacher where teacherid = %s""", (self.UserName,))
            myresult = mycursor.fetchone()
            if myresult is None:
                self.ErrorReport(str("No subject alloted to you!"))
            else:
                for row in myresult:
                    if row != self.UserName:
                        if row:
                            self.comboBox.addItem(row)
        except mysql.connector.Error as e:
            print(format(e))

    def FuncSelectedSub(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("""SELECT semestername FROM collgdatatable WHERE %s IN(subject1,subject2,
                            subject3,subject4,subject5,subject6,subject7)""", (self.comboBox.currentText(),))
            myresult = mycursor.fetchone()
            if myresult is None:
                self.ErrorReport(str("you must select correct subject!"))
            else:
                for row in myresult:
                    semester = row
                    print(semester)
                    self.WinManual = QtWidgets.QMainWindow()
                    self.ui = Ui_manual_attendance(self.UserName,self.comboBox.currentText(),semester)
                    self.ui.setupUi(self.WinManual)
                    self.WinManual.show()
        except mysql.connector.Error as e:
            print(format(e))


    def FuncBack(self,form_record_attendance):
        print("button hit")
        # self.WinDash = QtWidgets.QWidget()
        # self.ui = Ui_form_dashboard(self.UserName)
        # self.ui.setupUi(self.WinDash)
        form_record_attendance.hide()
        # self.dash.CallForShow()

        # self.WinDash.show()


    def ErrorReport(self,message):
        messageBox = QtWidgets.QMessageBox()
        ui = Ui_Dialog(message)
        ui.setupUi(messageBox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_record_attendance = QtWidgets.QWidget()
    ui = Ui_form_record_attendance()
    ui.setupUi(form_record_attendance)
    form_record_attendance.show()
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
