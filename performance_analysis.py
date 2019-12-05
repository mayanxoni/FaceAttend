# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'performance_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import  mysql.connector

from ErrorMessg import Ui_Dialog
from bar_chart import  Ui_Chart
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_performance_analysis(object):
    def setupUi(self, performance_analysis):
        performance_analysis.setObjectName("performance_analysis")
        performance_analysis.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        performance_analysis.setWindowIcon(icon)
        self.grid_layout = QtWidgets.QGridLayout(performance_analysis)
        self.grid_layout.setObjectName("grid_layout")
        self.label_spacer_bottom = QtWidgets.QLabel(performance_analysis)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.grid_layout.addWidget(self.label_spacer_bottom, 13, 1, 1, 1)
        self.label_spacer_top = QtWidgets.QLabel(performance_analysis)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.grid_layout.addWidget(self.label_spacer_top, 8, 1, 1, 1)
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.radio_enrollment = QtWidgets.QRadioButton(performance_analysis)
        self.radio_enrollment.setText("")
        self.radio_enrollment.setObjectName("radio_enrollment")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radio_enrollment)
        self.line_edit_enrollment = QtWidgets.QLineEdit(performance_analysis)
        self.line_edit_enrollment.setEnabled(False)
        self.line_edit_enrollment.setObjectName("line_edit_enrollment")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_enrollment)
        self.radio_semester = QtWidgets.QRadioButton(performance_analysis)
        self.radio_semester.setText("")
        self.radio_semester.setObjectName("radio_semester")
        self.form_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.radio_semester)
        self.combo_box_semester = QtWidgets.QComboBox(performance_analysis)
        self.combo_box_semester.setEnabled(False)
        self.combo_box_semester.setObjectName("combo_box_semester")
        self.form_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combo_box_semester)
        self.combo_box_roll = QtWidgets.QComboBox(performance_analysis)
        self.combo_box_roll.setEnabled(False)
        self.combo_box_roll.setObjectName("combo_box_roll")
        self.form_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.combo_box_roll)
        self.label_placeholder_2 = QtWidgets.QLabel(performance_analysis)
        self.label_placeholder_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_placeholder_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_placeholder_2.setObjectName("label_placeholder_2")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_placeholder_2)
        self.label_spacer_middle = QtWidgets.QLabel(performance_analysis)
        self.label_spacer_middle.setText("")
        self.label_spacer_middle.setObjectName("label_spacer_middle")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_spacer_middle)
        self.grid_layout.addLayout(self.form_layout, 11, 1, 1, 1)
        self.button_update = QtWidgets.QPushButton(performance_analysis)
        self.button_update.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon1)
        self.button_update.setIconSize(QtCore.QSize(32, 32))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.grid_layout.addWidget(self.button_update, 15, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_spacer_beneath = QtWidgets.QLabel(performance_analysis)
        self.label_spacer_beneath.setText("")
        self.label_spacer_beneath.setObjectName("label_spacer_beneath")
        self.grid_layout.addWidget(self.label_spacer_beneath, 12, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacerItem, 11, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_back = QtWidgets.QPushButton(performance_analysis)
        self.button_back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon2)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.gridLayout.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_performance_analysis = QtWidgets.QLabel(performance_analysis)
        self.label_performance_analysis.setObjectName("label_performance_analysis")
        self.gridLayout.addWidget(self.label_performance_analysis, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(performance_analysis)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.grid_layout.addLayout(self.gridLayout, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacerItem1, 11, 0, 1, 1)
        self.label_graph_icon = QtWidgets.QLabel(performance_analysis)
        self.label_graph_icon.setText("")
        self.label_graph_icon.setPixmap(QtGui.QPixmap("assets/analytics.png"))
        self.label_graph_icon.setScaledContents(True)
        self.label_graph_icon.setObjectName("label_graph_icon")
        self.grid_layout.addWidget(self.label_graph_icon, 9, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_placeholder_1 = QtWidgets.QLabel(performance_analysis)
        self.label_placeholder_1.setObjectName("label_placeholder_1")
        self.grid_layout.addWidget(self.label_placeholder_1, 10, 1, 1, 1)

        self.retranslateUi(performance_analysis)
        QtCore.QMetaObject.connectSlotsByName(performance_analysis)
        self.button_update.clicked.connect(self.FuncStudentDetails)
        self.radio_semester.toggled.connect(self.FuncRadio)
        self.radio_enrollment.toggled.connect(self.FuncRadio)
        self.combo_box_semester.currentIndexChanged.connect(self.FuncLoadRollNum)
        self.button_back.clicked.connect(lambda :self.FuncBack(performance_analysis))

    def retranslateUi(self, performance_analysis):
        _translate = QtCore.QCoreApplication.translate
        performance_analysis.setWindowTitle(_translate("performance_analysis", "Performance Analysis"))
        self.line_edit_enrollment.setPlaceholderText(_translate("performance_analysis", "Enrollment Number"))
        self.label_placeholder_2.setText(_translate("performance_analysis", "Or, choose Semester and Roll Number:"))
        self.label_performance_analysis.setText(_translate("performance_analysis", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#888a85;\">PERFORMANCE ANALYSIS</span></p></body></html>"))
        self.label_placeholder_1.setText(_translate("performance_analysis", "You can check the performance of any student by their Enrollment Number:"))

    def FuncRadio(self):
        if self.radio_enrollment.isChecked() == True:
            self.line_edit_enrollment.setEnabled(True)
        elif self.radio_semester.isChecked() == True:
            self.combo_box_semester.setEnabled(True)
            self.FuncLoadData()

    def FuncLoadData(self):
        try:
            mydatabase = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            cursor = mydatabase.cursor()
            sql = "SELECT  distinct semester FROM `studentdetails`"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            if result is None:
                self.ErrorReport(str("error "))
            else:
                for x in result:
                    self.combo_box_semester.addItems(x)
        except mysql.connector.Error as e:
            print(e)


    def FuncLoadRollNum(self):
        self.combo_box_roll.setEnabled(True)
        try:
            mydatabase = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            cursor = mydatabase.cursor()
            sql = "SELECT  distinct rollnum FROM `studentdetails` where semester = '"+self.combo_box_semester.currentText()+"'"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            if result is None:
                self.ErrorReport(str("error "))
            else:
                for x in result:
                    self.combo_box_roll.addItems(x)
        except mysql.connector.Error as e:
            print(e)

    #     mydb = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         database="collegeattend",
    #         passwd=""
    #     )
    #     mycursor = mydb.cursor()
    #     mycursor.execute("SELECT name FROM studentdetails")
    #     myresult = mycursor.fetchall()
    #     for row in myresult:
    #         self.combo_box_roll.addItem(row[0])


    def FuncStudentDetails(self):
        if self.radio_enrollment.isChecked() == True:
            if  str(self.line_edit_enrollment.text()) != "":
                try:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        database="collegeattend",
                        passwd=""
                    )
                    mycursor = mydb.cursor()
                    mycursor.execute("SELECT * FROM studentdetails where enrollement = "+str(self.line_edit_enrollment.text()))
                    myresult = mycursor.fetchone()
                    if myresult is None:
                        self.ErrorReport()
                    else:
                        self.RollNUM = myresult[0]
                        self.ListSEM = myresult[5]
                        for x in myresult:
                            print(x)

                        self.FindSub()
                except mysql.connector.Error as e:
                    print(e.errno)
                    print(e.sqlstate)
                    print("Error from Def Student Enoll".format(e))
            else:
                self.ErrorReport()



        elif self.radio_semester.isChecked() == True:
            try:
                mydatabase = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                cursor = mydatabase.cursor()
                sql = "SELECT * FROM `studentdetails` where  rollnum = " + str(self.combo_box_roll.currentText()) + " and semester = '" + str(self.combo_box_semester.currentText())+"'"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result is None:
                    self.ErrorReport(str("Error"))
                else:
                    self.RollNUM = result[0]
                    self.ListSEM = result[5]
                    for x in result:
                        print(x)

                    self.FindSub()
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Student combo Box".format(e))
        else:
           self.ErrorReport()



    def FindSub(self):
        self.ListSubj = []
        try:
            mydatabase = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            cursor = mydatabase.cursor()
            sql = "SELECT subject1,subject2,subject3,subject4,subject5,subject6,subject7 FROM `collgdatatable` where  semestername= '" + str(self.ListSEM) + "'"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result is None:
                self.ErrorReport()
            else:
                for x in result:
                    self.ListSubj.append(str(x))

                # print(len(self.ListSubj))
                # for i in range(len(self.ListSubj)):
                #     print(self.ListSubj[i])
                self.AvgSem()
        except mysql.connector.Error as e:
            print(e.errno)
            print(e.sqlstate)
            print("Error from Def FindSUb ".format(e))

    def AvgSem(self):
        self.SutTotalAttd = []
        self.ToTalClass = []
        for i in range(7):
            try:
                mydatabase = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                cursor = mydatabase.cursor()
                sql = "SELECT COUNT(`"+str(self.RollNUM)+"`) FROM `"+str(self.ListSubj[i])+"` where  `"+str(self.RollNUM)+"` = '1'"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result is None:
                    self.SutTotalAttd.append(str("Not"))
                else:
                    for x in result:
                        self.SutTotalAttd.append(str(result[0]))
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Avg  and student total".format(e))

        for i in range(7):
            try:
                mydatabase = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                cursor = mydatabase.cursor()
                sql = "SELECT COUNT(`classdate`) FROM `"+str(self.ListSubj[i])+"`"
                print(sql)
                cursor.execute(sql)
                result = cursor.fetchone()
                if result is None:
                    self.ToTalClass.append(str("hot"))
                else:
                    for x in result:
                        self.ToTalClass.append(str(result[0]))
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Avg Total block".format(e))

        print(len(self.ToTalClass))
        print(len(self.SutTotalAttd))
        self.Percentage =  []
        print("total class")
        for j in range(len(self.ToTalClass)):
             self.Percentage.append(int(self.SutTotalAttd[j])/int(self.ToTalClass[j])*100)
        print("student Present")
        for k in range(len(self.Percentage)):
            print(self.Percentage[k])

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Chart(self.Percentage,self.ListSubj)
        self.ui.setupUi(self.window)
        self.window.show()


    def Outstring(self):
        return  self.Percentage

    def FuncBack(self,performance_analysis):
        performance_analysis.close()
        # self.WinAdmin = QtWidgets.QWidget()
        # self.ui = Ui_form_admin_panel()
        # self.ui.setupUi(self.WinAdmin)
        # self.WinAdmin.show()


    def ErrorReport(self,message):
        messageBox = QtWidgets.QMessageBox()
        ui = Ui_Dialog(message)
        ui.setupUi(messageBox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    performance_analysis = QtWidgets.QWidget()
    ui = Ui_performance_analysis()
    ui.setupUi(performance_analysis)
    performance_analysis.show()
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
