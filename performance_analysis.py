import mysql.connector
from error_message import ErrorMessage
from bar_chart import BarChart
from PyQt5 import QtCore, QtGui, QtWidgets


class PerformanceAnalysis(object):
    def setup_ui(self, performance_analysis_object):
        performance_analysis_object.setObjectName("performance_analysis_object")
        performance_analysis_object.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        performance_analysis_object.setWindowIcon(icon)
        self.grid_layout = QtWidgets.QGridLayout(performance_analysis_object)
        self.grid_layout.setObjectName("grid_layout")
        self.label_spacer_bottom = QtWidgets.QLabel(performance_analysis_object)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.grid_layout.addWidget(self.label_spacer_bottom, 13, 1, 1, 1)
        self.label_spacer_top = QtWidgets.QLabel(performance_analysis_object)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.grid_layout.addWidget(self.label_spacer_top, 8, 1, 1, 1)
        self.form_layout = QtWidgets.QFormLayout()
        self.form_layout.setObjectName("form_layout")
        self.radio_enrollment = QtWidgets.QRadioButton(performance_analysis_object)
        self.radio_enrollment.setText("")
        self.radio_enrollment.setObjectName("radio_enrollment")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radio_enrollment)
        self.line_edit_enrollment = QtWidgets.QLineEdit(performance_analysis_object)
        self.line_edit_enrollment.setEnabled(False)
        self.line_edit_enrollment.setObjectName("line_edit_enrollment")
        self.form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_enrollment)
        self.radio_semester = QtWidgets.QRadioButton(performance_analysis_object)
        self.radio_semester.setText("")
        self.radio_semester.setObjectName("radio_semester")
        self.form_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.radio_semester)
        self.combo_box_semester = QtWidgets.QComboBox(performance_analysis_object)
        self.combo_box_semester.setEnabled(False)
        self.combo_box_semester.setObjectName("combo_box_semester")
        self.form_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combo_box_semester)
        self.combo_box_roll = QtWidgets.QComboBox(performance_analysis_object)
        self.combo_box_roll.setEnabled(False)
        self.combo_box_roll.setObjectName("combo_box_roll")
        self.form_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.combo_box_roll)
        self.label_placeholder_2 = QtWidgets.QLabel(performance_analysis_object)
        self.label_placeholder_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_placeholder_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_placeholder_2.setObjectName("label_placeholder_2")
        self.form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_placeholder_2)
        self.label_spacer_middle = QtWidgets.QLabel(performance_analysis_object)
        self.label_spacer_middle.setText("")
        self.label_spacer_middle.setObjectName("label_spacer_middle")
        self.form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_spacer_middle)
        self.grid_layout.addLayout(self.form_layout, 11, 1, 1, 1)
        self.button_update = QtWidgets.QPushButton(performance_analysis_object)
        self.button_update.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon1)
        self.button_update.setIconSize(QtCore.QSize(32, 32))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.grid_layout.addWidget(self.button_update, 15, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_spacer_beneath = QtWidgets.QLabel(performance_analysis_object)
        self.label_spacer_beneath.setText("")
        self.label_spacer_beneath.setObjectName("label_spacer_beneath")
        self.grid_layout.addWidget(self.label_spacer_beneath, 12, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacerItem, 11, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_back = QtWidgets.QPushButton(performance_analysis_object)
        self.button_back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon2)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.gridLayout.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_performance_analysis = QtWidgets.QLabel(performance_analysis_object)
        self.label_performance_analysis.setObjectName("label_performance_analysis")
        self.gridLayout.addWidget(self.label_performance_analysis, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(performance_analysis_object)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.grid_layout.addLayout(self.gridLayout, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacerItem1, 11, 0, 1, 1)
        self.label_graph_icon = QtWidgets.QLabel(performance_analysis_object)
        self.label_graph_icon.setText("")
        self.label_graph_icon.setPixmap(QtGui.QPixmap("assets/analytics.png"))
        self.label_graph_icon.setScaledContents(True)
        self.label_graph_icon.setObjectName("label_graph_icon")
        self.grid_layout.addWidget(self.label_graph_icon, 9, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_placeholder_1 = QtWidgets.QLabel(performance_analysis_object)
        self.label_placeholder_1.setObjectName("label_placeholder_1")
        self.grid_layout.addWidget(self.label_placeholder_1, 10, 1, 1, 1)

        performance_analysis_object.setWindowTitle("Performance Analysis")
        self.line_edit_enrollment.setPlaceholderText("Enrollment Number")
        self.label_placeholder_1.setText("You can check the performance of any student by their Enrollment Number:")
        self.label_placeholder_2.setText("Or, by their Semester and Roll Number:")
        self.label_performance_analysis.setText("<html><head/><body><p align=\"center\"><span style=\" "
                                                "font-size:16pt; font-weight:600; color:#888a85;\">PERFORMANCE "
                                                "ANALYSIS</span></p></body></html>")

        QtCore.QMetaObject.connectSlotsByName(performance_analysis_object)
        self.button_update.clicked.connect(self.student_details)
        self.radio_semester.toggled.connect(self.toggle_radio)
        self.radio_enrollment.toggled.connect(self.toggle_radio)
        self.combo_box_semester.currentIndexChanged.connect(self.load_roll)
        self.button_back.clicked.connect(lambda: self.back(performance_analysis_object))

    def toggle_radio(self):
        if self.radio_enrollment.isChecked():
            self.line_edit_enrollment.setEnabled(True)
        elif self.radio_semester.isChecked():
            self.combo_box_semester.setEnabled(True)
            self.load_data()

    def load_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            semester_query = "SELECT distinct semester FROM `studentdetails`"
            print(semester_query)
            db_cursor.execute(semester_query)
            semester_result = db_cursor.fetchall()
            if semester_result is None:
                self.error_report(str("Error!"))
            else:
                for x in semester_result:
                    self.combo_box_semester.addItems(x)
        except mysql.connector.Error as e:
            print(e)

    def load_roll(self):
        self.combo_box_roll.setEnabled(True)
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            roll_query = "SELECT  distinct rollnum FROM `studentdetails` where semester = '" + \
                         self.combo_box_semester.currentText() + "'"
            print(roll_query)
            db_cursor.execute(roll_query)
            roll_result = db_cursor.fetchall()
            if roll_result is None:
                self.error_report(str("Error!"))
            else:
                for x in roll_result:
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

    def student_details(self):
        if self.radio_enrollment.isChecked():
            if str(self.line_edit_enrollment.text()) != "":
                try:
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        database="collegeattend",
                        passwd=""
                    )
                    mycursor = mydb.cursor()
                    mycursor.execute(
                        "SELECT * FROM studentdetails where enrollement = " + str(self.line_edit_enrollment.text()))
                    myresult = mycursor.fetchone()
                    if myresult is None:
                        self.error_report(str("No such student present here!"))
                    else:
                        self.roll = myresult[0]
                        self.semester = myresult[5]
                        for x in myresult:
                            print(x)

                        self.fetch_subjects()
                except mysql.connector.Error as e:
                    print(e.errno)
                    print(e.sqlstate)
                    print("Error from Def Student Enroll".format(e))
            else:
                self.error_report(str(""))

        elif self.radio_semester.isChecked():
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                db_cursor = connection.cursor()
                details_query = "SELECT * FROM `studentdetails` WHERE rollnum = " + \
                                str(self.combo_box_roll.currentText()) + " AND semester = '" + \
                                str(self.combo_box_semester.currentText()) + "'"
                print(details_query)
                db_cursor.execute(details_query)
                details_result = db_cursor.fetchone()
                if details_result is None:
                    self.error_report(str("Error!"))
                else:
                    self.roll = details_result[0]
                    self.semester = details_result[5]
                    for x in details_result:
                        print(x)
                    self.fetch_subjects()
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Student combo Box".format(e))
        else:
            self.error_report()

    def fetch_subjects(self):
        self.subjects_list = []
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            subjects_query = "SELECT subject1, subject2, subject3, subject4, subject5, subject6, subject7 FROM " \
                             "`collgdatatable` WHERE semestername= '" + str(self.semester) + "'"
            print(subjects_query)
            db_cursor.execute(subjects_query)
            subjects_result = db_cursor.fetchone()
            if subjects_result is None:
                self.error_report()
            else:
                for x in subjects_result:
                    self.subjects_list.append(str(x))
                # print(len(self.ListSubj))
                # for i in range(len(self.ListSubj)):
                #     print(self.ListSubj[i])
                self.AvgSem()
        except mysql.connector.Error as e:
            print(e.errno)
            print(e.sqlstate)
            print("Error from Def FindSUb ".format(e))

    def AvgSem(self):
        self.student_attended_list = []
        self.total_classes_list = []
        for i in range(7):
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                db_cursor = connection.cursor()
                classdate_query = "SELECT COUNT(`" + str(self.roll) + "`) FROM `" + str(self.subjects_list[i]) + "` WHERE `" + str(
                    self.roll) + "` = '1'"
                print(classdate_query)
                db_cursor.execute(classdate_query)
                classdate_result = db_cursor.fetchone()
                if classdate_result is None:
                    self.student_attended_list.append(str("Not"))
                else:
                    for x in classdate_result:
                        self.student_attended_list.append(str(classdate_result[0]))
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Avg  and student total".format(e))

        for i in range(7):
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                db_cursor = connection.cursor()
                classdate_query = "SELECT COUNT(`classdate`) FROM `" + str(self.subjects_list[i]) + "`"
                print(classdate_query)
                db_cursor.execute(classdate_query)
                classdate_result = db_cursor.fetchone()
                if classdate_result is None:
                    self.total_classes_list.append(str("hot"))
                else:
                    for x in classdate_result:
                        self.total_classes_list.append(str(classdate_result[0]))
            except mysql.connector.Error as e:
                print(e.errno)
                print(e.sqlstate)
                print("Error from Def Avg Total block".format(e))

        print(len(self.total_classes_list))
        print(len(self.student_attended_list))
        self.percentage_list = []
        print("Total Classes")
        for j in range(len(self.total_classes_list)):
            self.percentage_list.append(int(self.student_attended_list[j]) / int(self.total_classes_list[j]) * 100)
        print("Student Present")
        for k in range(len(self.percentage_list)):
            print(self.percentage_list[k])

        self.win_bar_chart = QtWidgets.QMainWindow()
        self.ui = BarChart(self.percentage_list, self.subjects_list)
        self.ui.setup_ui(self.win_bar_chart)
        self.win_bar_chart.show()

    def out_string(self):
        return self.percentage_list

    @staticmethod
    def back(performance_analysis):
        performance_analysis.close()
        # self.WinAdmin = QtWidgets.QWidget()
        # self.ui = AdminPanel()
        # self.ui.setup_ui(self.WinAdmin)
        # self.WinAdmin.show()

    @staticmethod
    def error_report(message):
        message_box = QtWidgets.QMessageBox()
        ui = ErrorMessage(message)
        ui.setup_ui(message_box)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    performance_analysis_object = QtWidgets.QWidget()
    performance_analysis = PerformanceAnalysis()
    performance_analysis.setup_ui(performance_analysis_object)
    performance_analysis_object.show()
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
