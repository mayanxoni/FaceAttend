
from datetime import date

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from ErrorMessg import Ui_Dialog


class Ui_manual_attendance(object):
    def __init__(self, UserName, Subject, Semester):
            self.UserName = UserName
            self.Subject = Subject
            self.Semester = Semester

    def setupUi(self, manual_attendance):
        manual_attendance.setObjectName("manual_attendance")
        manual_attendance.resize(905, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        manual_attendance.setWindowIcon(icon)
        self.grid_layout = QtWidgets.QGridLayout(manual_attendance)
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout_1 = QtWidgets.QGridLayout()
        self.grid_layout_1.setObjectName("grid_layout_1")
        self.button_back = QtWidgets.QPushButton(manual_attendance)
        self.button_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon1)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.grid_layout_1.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_manual_attendance = QtWidgets.QLabel(manual_attendance)
        self.label_manual_attendance.setObjectName("label_manual_attendance")
        self.grid_layout_1.addWidget(self.label_manual_attendance, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_spacer = QtWidgets.QLabel(manual_attendance)
        self.label_spacer.setText("")
        self.label_spacer.setObjectName("label_spacer")
        self.grid_layout_1.addWidget(self.label_spacer, 0, 2, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_1, 0, 0, 1, 3)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout()
        self.vertical_layout_3.setObjectName("vertical_layout_3")
        self.checkbox_3 = QtWidgets.QCheckBox(manual_attendance)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkbox_3.setIcon(icon2)
        self.checkbox_3.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_3.setObjectName("checkbox_3")
        self.vertical_layout_3.addWidget(self.checkbox_3)
        self.label_3 = QtWidgets.QLabel(manual_attendance)
        self.label_3.setObjectName("label_3")
        self.vertical_layout_3.addWidget(self.label_3)
        self.grid_layout_2.addLayout(self.vertical_layout_3, 0, 4, 1, 1)
        self.vertical_layout_8 = QtWidgets.QVBoxLayout()
        self.vertical_layout_8.setObjectName("vertical_layout_8")
        self.checkbox_8 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_8.setIcon(icon2)
        self.checkbox_8.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_8.setObjectName("checkbox_8")
        self.vertical_layout_8.addWidget(self.checkbox_8)
        self.label_8 = QtWidgets.QLabel(manual_attendance)
        self.label_8.setObjectName("label_8")
        self.vertical_layout_8.addWidget(self.label_8)
        self.grid_layout_2.addLayout(self.vertical_layout_8, 2, 4, 1, 1)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout()
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.checkbox_2 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_2.setIcon(icon2)
        self.checkbox_2.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_2.setObjectName("checkbox_2")
        self.vertical_layout_2.addWidget(self.checkbox_2)
        self.label_2 = QtWidgets.QLabel(manual_attendance)
        self.label_2.setObjectName("label_2")
        self.vertical_layout_2.addWidget(self.label_2)
        self.grid_layout_2.addLayout(self.vertical_layout_2, 0, 2, 1, 1)
        self.vertical_layout_7 = QtWidgets.QVBoxLayout()
        self.vertical_layout_7.setObjectName("vertical_layout_7")
        self.checkbox_7 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_7.setIcon(icon2)
        self.checkbox_7.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_7.setObjectName("checkbox_7")
        self.vertical_layout_7.addWidget(self.checkbox_7)
        self.label_7 = QtWidgets.QLabel(manual_attendance)
        self.label_7.setObjectName("label_7")
        self.vertical_layout_7.addWidget(self.label_7)
        self.grid_layout_2.addLayout(self.vertical_layout_7, 2, 2, 1, 1)
        self.vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.vertical_layout_1.setObjectName("vertical_layout_1")
        self.checkbox_1 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_1.setIcon(icon2)
        self.checkbox_1.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_1.setObjectName("checkbox_1")
        self.vertical_layout_1.addWidget(self.checkbox_1)
        self.label_1 = QtWidgets.QLabel(manual_attendance)
        self.label_1.setObjectName("label_1")
        self.vertical_layout_1.addWidget(self.label_1)
        self.grid_layout_2.addLayout(self.vertical_layout_1, 0, 0, 1, 1)
        self.vertical_layout_5 = QtWidgets.QVBoxLayout()
        self.vertical_layout_5.setObjectName("vertical_layout_5")
        self.checkbox_5 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_5.setIcon(icon2)
        self.checkbox_5.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_5.setObjectName("checkbox_5")
        self.vertical_layout_5.addWidget(self.checkbox_5)
        self.label_5 = QtWidgets.QLabel(manual_attendance)
        self.label_5.setObjectName("label_5")
        self.vertical_layout_5.addWidget(self.label_5)
        self.grid_layout_2.addLayout(self.vertical_layout_5, 0, 8, 1, 1)
        self.v_line_4 = QtWidgets.QFrame(manual_attendance)
        self.v_line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_4.setObjectName("v_line_4")
        self.grid_layout_2.addWidget(self.v_line_4, 0, 7, 1, 1)
        self.h_line_1 = QtWidgets.QFrame(manual_attendance)
        self.h_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_1.setObjectName("h_line_1")
        self.grid_layout_2.addWidget(self.h_line_1, 1, 0, 1, 1)
        self.vertical_layout_10 = QtWidgets.QVBoxLayout()
        self.vertical_layout_10.setObjectName("vertical_layout_10")
        self.checkbox_10 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_10.setIcon(icon2)
        self.checkbox_10.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_10.setObjectName("checkbox_10")
        self.vertical_layout_10.addWidget(self.checkbox_10)
        self.label_10 = QtWidgets.QLabel(manual_attendance)
        self.label_10.setObjectName("label_10")
        self.vertical_layout_10.addWidget(self.label_10)
        self.grid_layout_2.addLayout(self.vertical_layout_10, 2, 8, 1, 1)
        self.vertical_layout_4 = QtWidgets.QVBoxLayout()
        self.vertical_layout_4.setObjectName("vertical_layout_4")
        self.checkbox_4 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_4.setIcon(icon2)
        self.checkbox_4.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_4.setObjectName("checkbox_4")
        self.vertical_layout_4.addWidget(self.checkbox_4)
        self.label_4 = QtWidgets.QLabel(manual_attendance)
        self.label_4.setObjectName("label_4")
        self.vertical_layout_4.addWidget(self.label_4)
        self.grid_layout_2.addLayout(self.vertical_layout_4, 0, 6, 1, 1)
        self.v_line_1 = QtWidgets.QFrame(manual_attendance)
        self.v_line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_1.setObjectName("v_line_1")
        self.grid_layout_2.addWidget(self.v_line_1, 0, 1, 1, 1)
        self.vertical_layout_9 = QtWidgets.QVBoxLayout()
        self.vertical_layout_9.setObjectName("vertical_layout_9")
        self.checkbox_9 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_9.setIcon(icon2)
        self.checkbox_9.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_9.setObjectName("checkbox_9")
        self.vertical_layout_9.addWidget(self.checkbox_9)
        self.label_9 = QtWidgets.QLabel(manual_attendance)
        self.label_9.setObjectName("label_9")
        self.vertical_layout_9.addWidget(self.label_9)
        self.grid_layout_2.addLayout(self.vertical_layout_9, 2, 6, 1, 1)
        self.v_line_5 = QtWidgets.QFrame(manual_attendance)
        self.v_line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_5.setObjectName("v_line_5")
        self.grid_layout_2.addWidget(self.v_line_5, 2, 1, 1, 1)
        self.vertical_layout_6 = QtWidgets.QVBoxLayout()
        self.vertical_layout_6.setObjectName("vertical_layout_6")
        self.checkbox_6 = QtWidgets.QCheckBox(manual_attendance)
        self.checkbox_6.setIcon(icon2)
        self.checkbox_6.setIconSize(QtCore.QSize(64, 64))
        self.checkbox_6.setObjectName("checkbox_6")
        self.vertical_layout_6.addWidget(self.checkbox_6)
        self.label_6 = QtWidgets.QLabel(manual_attendance)
        self.label_6.setObjectName("label_6")
        self.vertical_layout_6.addWidget(self.label_6)
        self.grid_layout_2.addLayout(self.vertical_layout_6, 2, 0, 1, 1)
        self.v_line_7 = QtWidgets.QFrame(manual_attendance)
        self.v_line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_7.setObjectName("v_line_7")
        self.grid_layout_2.addWidget(self.v_line_7, 2, 5, 1, 1)
        self.v_line_3 = QtWidgets.QFrame(manual_attendance)
        self.v_line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_3.setObjectName("v_line_3")
        self.grid_layout_2.addWidget(self.v_line_3, 0, 5, 1, 1)
        self.v_line_6 = QtWidgets.QFrame(manual_attendance)
        self.v_line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_6.setObjectName("v_line_6")
        self.grid_layout_2.addWidget(self.v_line_6, 2, 3, 1, 1)
        self.v_line_2 = QtWidgets.QFrame(manual_attendance)
        self.v_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_2.setObjectName("v_line_2")
        self.grid_layout_2.addWidget(self.v_line_2, 0, 3, 1, 1)
        self.v_line_8 = QtWidgets.QFrame(manual_attendance)
        self.v_line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.v_line_8.setObjectName("v_line_8")
        self.grid_layout_2.addWidget(self.v_line_8, 2, 7, 1, 1)
        self.h_line_2 = QtWidgets.QFrame(manual_attendance)
        self.h_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_2.setObjectName("h_line_2")
        self.grid_layout_2.addWidget(self.h_line_2, 1, 2, 1, 1)
        self.h_line_3 = QtWidgets.QFrame(manual_attendance)
        self.h_line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_3.setObjectName("h_line_3")
        self.grid_layout_2.addWidget(self.h_line_3, 1, 4, 1, 1)
        self.h_line_4 = QtWidgets.QFrame(manual_attendance)
        self.h_line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_4.setObjectName("h_line_4")
        self.grid_layout_2.addWidget(self.h_line_4, 1, 6, 1, 1)
        self.h_line_5 = QtWidgets.QFrame(manual_attendance)
        self.h_line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.h_line_5.setObjectName("h_line_5")
        self.grid_layout_2.addWidget(self.h_line_5, 1, 8, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 10, 0, 2, 3)
        self.button_update = QtWidgets.QPushButton(manual_attendance)
        self.button_update.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon3)
        self.button_update.setIconSize(QtCore.QSize(32, 32))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.grid_layout.addWidget(self.button_update, 13, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_update_icon = QtWidgets.QLabel(manual_attendance)
        self.label_update_icon.setText("")
        self.label_update_icon.setPixmap(QtGui.QPixmap("assets/file.png"))
        self.label_update_icon.setScaledContents(True)
        self.label_update_icon.setObjectName("label_update_icon")
        self.grid_layout.addWidget(self.label_update_icon, 8, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_placeholder = QtWidgets.QLabel(manual_attendance)
        self.label_placeholder.setObjectName("label_placeholder")
        self.grid_layout.addWidget(self.label_placeholder, 9, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(manual_attendance)
        self.funcHide()
        self.FuncloadData()
        self.cb[0].stateChanged.connect(lambda: self.FuncChecking(0))
        self.cb[1].stateChanged.connect(lambda: self.FuncChecking(1))
        self.cb[2].stateChanged.connect(lambda: self.FuncChecking(2))
        self.cb[3].stateChanged.connect(lambda: self.FuncChecking(3))
        self.cb[4].stateChanged.connect(lambda: self.FuncChecking(4))
        self.cb[5].stateChanged.connect(lambda: self.FuncChecking(5))
        self.cb[6].stateChanged.connect(lambda: self.FuncChecking(6))
        self.cb[7].stateChanged.connect(lambda: self.FuncChecking(7))
        self.cb[8].stateChanged.connect(lambda: self.FuncChecking(8))
        self.cb[9].stateChanged.connect(lambda: self.FuncChecking(9))
        self.button_back.clicked.connect(lambda :self.FuncBack(manual_attendance))
        self.button_update.clicked.connect(lambda :self.FuncTakeAttend(manual_attendance))



        QtCore.QMetaObject.connectSlotsByName(manual_attendance)
        manual_attendance.setTabOrder(self.checkbox_1, self.checkbox_2)
        manual_attendance.setTabOrder(self.checkbox_2, self.checkbox_3)
        manual_attendance.setTabOrder(self.checkbox_3, self.checkbox_4)
        manual_attendance.setTabOrder(self.checkbox_4, self.checkbox_5)
        manual_attendance.setTabOrder(self.checkbox_5, self.checkbox_6)
        manual_attendance.setTabOrder(self.checkbox_6, self.checkbox_7)
        manual_attendance.setTabOrder(self.checkbox_7, self.checkbox_8)
        manual_attendance.setTabOrder(self.checkbox_8, self.checkbox_9)
        manual_attendance.setTabOrder(self.checkbox_9, self.checkbox_10)
        manual_attendance.setTabOrder(self.checkbox_10, self.button_update)
        manual_attendance.setTabOrder(self.button_update, self.button_back)


    def retranslateUi(self, manual_attendance):
        _translate = QtCore.QCoreApplication.translate
        manual_attendance.setWindowTitle(_translate("manual_attendance", "Manual Attendance"))
        self.label_manual_attendance.setText(_translate("manual_attendance", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#888a85;\">MANUAL ATTENDANCE</span></p></body></html>"))
        self.checkbox_3.setText(_translate("manual_attendance", "Roll No: 3"))
        self.label_3.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_8.setText(_translate("manual_attendance", "Roll No: 8"))
        self.label_8.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_2.setText(_translate("manual_attendance", "Roll No: 2"))
        self.label_2.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_7.setText(_translate("manual_attendance", "Roll No: 7"))
        self.label_7.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_1.setText(_translate("manual_attendance", "Roll No: 1"))
        self.label_1.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_5.setText(_translate("manual_attendance", "Roll No: 5"))
        self.label_5.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_10.setText(_translate("manual_attendance", "Roll No: 10"))
        self.label_10.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_4.setText(_translate("manual_attendance", "Roll No: 4"))
        self.label_4.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_9.setText(_translate("manual_attendance", "Roll No: 9"))
        self.label_9.setText(_translate("manual_attendance", "TextLabel"))
        self.checkbox_6.setText(_translate("manual_attendance","Roll No: 6"))
        self.label_6.setText(_translate("manual_attendance", "TextLabel"))
        self.label_placeholder.setText(_translate("manual_attendance", "Check or uncheck the boxes to change the status of the attendance record of the student:"))
        self.cb = [self.checkbox_1, self.checkbox_2, self.checkbox_3, self.checkbox_4, self.checkbox_5, self.checkbox_6,
                   self.checkbox_7, self.checkbox_8, self.checkbox_9, self.checkbox_10]
        self.rollarr = [self.label_1,self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,self.label_7, self.label_8,self.label_9,self.label_10]
        self.attendance = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def funcHide(self):
        for i in range(10):
            self.cb[i].hide()
            self.rollarr[i].hide()

    def FuncloadData(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("""SELECT rollnum,name,pic FROM studentdetails WHERE  semester = %s order by rollnum""",(self.Semester,))
            myresult = mycursor.fetchall()
            if myresult is None:
                self.ErrorReport(str("No Students in this semester"))
            else:
                i = 0
                pixmap1 = []
                namearr = []
                for row in myresult:
                    pixmap1.append(QPixmap("pic/"+row[2]))
                    self.icon4 = QtGui.QIcon()
                    self.icon4.addPixmap(pixmap1[i], QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    self.cb[i].setIcon(self.icon4)
                    rn = row[0]
                    nm = row[1]
                    namearr.append(rn+'. '+nm)
                    print(namearr[i])
                    self.rollarr[i].setText(namearr[i])
                    self.cb[i].show()
                    self.rollarr[i].show()
                    i = i + 1
        except mysql.connector.Error as err:
            self.ErrorReport(format(err))


    def FuncChecking(self,x):
            if  self.cb[x].isChecked() == True:
                self.cb[x].setText("Is Present")
                self.cb[x].setStyleSheet("color: Green")
                self.attendance[x] = 1
            else:
                self.cb[x].setText("Is Absent")
                self.cb[x].setStyleSheet("color: red")
                self.attendance[x] = 0

    def FuncTakeAttend(self,manual_attendance):
        today = date.today()
        self.attendance[10] = today
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='collegeattend',
                                                 user='root',
                                                 password='')
            cursor = connection.cursor()
            string = "(`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `classdate`)"
            tab = "`" + str(self.Subject) + "`" + string
            cursor.execute("INSERT INTO "+ str(tab) +" VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)",(self.attendance[0],self.attendance[1],self.attendance[2],self.attendance[3],self.attendance[4],self.attendance[5],self.attendance[6],self.attendance[7],self.attendance[8],self.attendance[9],self.attendance[10],))
            connection.commit()
            manual_attendance.close()
            print("Record inserted successfully into "+ str(tab) + "table")
        except mysql.connector.Error as error:
            self.ErrorReport(format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def FuncBack(self,manual_attendance):
        manual_attendance.close()


    def ErrorReport(self,message):
        messageBox = QtWidgets.QMessageBox()
        ui = Ui_Dialog(message)
        ui.setupUi(messageBox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manual_attendance = QtWidgets.QWidget()
    ui = Ui_manual_attendance()
    ui.setupUi(manual_attendance)
    manual_attendance.show()
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