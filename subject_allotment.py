import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

from ErrorMessg import Ui_Dialog


class Ui_subject_allotment(object):
    def setupUi(self, subject_allotment):
        subject_allotment.setObjectName("subject_allotment")
        subject_allotment.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        subject_allotment.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(subject_allotment)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.list_widget_available = QtWidgets.QListWidget(subject_allotment)
        self.list_widget_available.setObjectName("list_widget_available")
        self.gridLayout_4.addWidget(self.list_widget_available, 6, 0, 11, 1)
        self.button_remove = QtWidgets.QPushButton(subject_allotment)
        self.button_remove.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_remove.setIcon(icon1)
        self.button_remove.setIconSize(QtCore.QSize(32, 32))
        self.button_remove.setFlat(False)
        self.button_remove.setObjectName("button_remove")
        self.gridLayout_4.addWidget(self.button_remove, 12, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.button_add = QtWidgets.QPushButton(subject_allotment)
        self.button_add.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add.setIcon(icon2)
        self.button_add.setIconSize(QtCore.QSize(32, 32))
        self.button_add.setFlat(False)
        self.button_add.setObjectName("button_add")
        self.gridLayout_4.addWidget(self.button_add, 10, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.button_select = QtWidgets.QPushButton(subject_allotment)
        self.button_select.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_select.setIcon(icon3)
        self.button_select.setIconSize(QtCore.QSize(32, 32))
        self.button_select.setFlat(False)
        self.button_select.setObjectName("button_select")
        self.gridLayout_4.addWidget(self.button_select, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_placeholder = QtWidgets.QLabel(subject_allotment)
        self.label_placeholder.setObjectName("label_placeholder")
        self.gridLayout_4.addWidget(self.label_placeholder, 2, 0, 1, 3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.list_widget_allotted = QtWidgets.QListWidget(subject_allotment)
        self.list_widget_allotted.setObjectName("list_widget_allotted")
        self.gridLayout_4.addWidget(self.list_widget_allotted, 6, 2, 11, 1)
        self.label_teachers_icon = QtWidgets.QLabel(subject_allotment)
        self.label_teachers_icon.setText("")
        self.label_teachers_icon.setPixmap(QtGui.QPixmap("assets/group.png"))
        self.label_teachers_icon.setObjectName("label_teachers_icon")
        self.gridLayout_4.addWidget(self.label_teachers_icon, 0, 1, 1, 1)
        self.label_available = QtWidgets.QLabel(subject_allotment)
        self.label_available.setObjectName("label_available")
        self.gridLayout_4.addWidget(self.label_available, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_allotted = QtWidgets.QLabel(subject_allotment)
        self.label_allotted.setObjectName("label_allotted")
        self.gridLayout_4.addWidget(self.label_allotted, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.button_update = QtWidgets.QPushButton(subject_allotment)
        self.button_update.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon4)
        self.button_update.setIconSize(QtCore.QSize(32, 32))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.gridLayout_4.addWidget(self.button_update, 18, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(subject_allotment)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.gridLayout_4.addWidget(self.label_spacer_bottom, 15, 1, 1, 1)
        self.label_spacer_top = QtWidgets.QLabel(subject_allotment)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.gridLayout_4.addWidget(self.label_spacer_top, 9, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(subject_allotment)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 3, 0, 1, 3)
        self.button_add.hide()
        self.button_update.hide()
        self.button_remove.hide()

        self.retranslateUi(subject_allotment)
        self.FuncLoadUser()
        self.FuncPrepareList()
        self.button_select.clicked.connect(self.FuncOnSelectUser)
        self.button_add.clicked.connect(self.FuncAddButton)
        self.button_remove.clicked.connect(self.FuncRemoveButton)
        self.button_update.clicked.connect(self.FuncUpdateButton)
        QtCore.QMetaObject.connectSlotsByName(subject_allotment)
        subject_allotment.setTabOrder(self.comboBox, self.button_select)
        subject_allotment.setTabOrder(self.button_select, self.list_widget_available)
        subject_allotment.setTabOrder(self.list_widget_available, self.list_widget_allotted)
        subject_allotment.setTabOrder(self.list_widget_allotted, self.button_add)
        subject_allotment.setTabOrder(self.button_add, self.button_remove)
        subject_allotment.setTabOrder(self.button_remove, self.button_update)

    def retranslateUi(self, subject_allotment):
        _translate = QtCore.QCoreApplication.translate
        subject_allotment.setWindowTitle(_translate("subject_allotment", "Subject Allotment"))
        self.label_placeholder.setText(_translate("subject_allotment", "You can allot or withhold the subject(s) by selecting name of the teacher from the list below:"))
        self.label_available.setText(_translate("subject_allotment", "Available Subject(s)"))
        self.label_allotted.setText(_translate("subject_allotment", "Allotted Subject(s)"))


    def FuncLoadUser(self):
        self.id = []
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            cursor = db.cursor()
            cursor.execute("select userid,teachername from userdatabase")
            result = cursor.fetchall()
            if result is None:
                self.ErrorReport(str("No user in database"))
            else:
                for row in result:
                    if row[0] != "Admin":
                        self.comboBox.addItem(str(row[1]))
                        self.id.append(str(row[0]))
        except mysql.connector.Error as er:
            print(er)
            self.ErrorReport(format(er))

    def FuncPrepareList(self):
        AllSubjects = []
        ReservedSubject = []
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("select subject1,subject2,subject3,subject4,subject5,subject6,subject7 from collgdatatable")
            myresult = mycursor.fetchall()
            if myresult is None:
                self.ErrorReport(str("No more subject for allocation."))
            else:
                for row in myresult:
                    for i in range(7):
                        if row[i] != "":
                            AllSubjects.append(str(row[i]))
                stp1 = len(AllSubjects)
        except mysql.connector.Error as e:
            print(e)
            self.ErrorReport(format(e))

        # this is for the already alloted subjects
        try:
            mycursor = mydb.cursor()
            mycursor.execute("select subject1,subject2,subject3,subject4,subject5,subject6,subject7 from subjectteacher")
            myresult = mycursor.fetchall()
            if myresult is None:
                print("object blank ")
                pass
            else:
                for row in myresult:
                    for i in range(7):
                        if row[i] != "":
                            ReservedSubject.append(str(row[i]))
                stp2 = len(ReservedSubject)
        except mysql.connector.Error as e:
            print(e)
            self.ErrorReport(format(e))

        # this is the final list that is going to be shown
        finalList = []
        for i in range(stp1):
            flag = 0
            for j in range(stp2):
                if str(AllSubjects[i]) == str(ReservedSubject[j]):
                    flag = 1
            if flag == 0:
                finalList.append(str(AllSubjects[i]))

        r = len(finalList)
        for p in range(r):
            print(finalList[p])

        self.list_widget_available.addItems(finalList)


    def FuncOnSelectUser(self):
        self.list_widget_allotted.clear()
        subList = []
        ind = self.comboBox.currentIndex()
        self.tid = self.id[ind]
        print(self.tid)
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("select subject1,subject2,subject3,subject4,subject5,subject6,subject7 from subjectteacher where teacherid = '" + str(self.id[ind]) + "'")
            myresult = mycursor.fetchone()
            if myresult is None:
                mycursor.execute("INSERT INTO `subjectteacher`(`teacherid`) VALUES ('" + str(self.id[ind]) + "')")
                mydb.commit()
                self.ErrorReport(str("Please select again"))
            else:
                for row in myresult:
                    if row is not None:
                        subList.append(str(row))

                self.list_widget_allotted.addItems(subList)
                self.list_widget_allotted.show()
                self.button_add.show()
                self.button_remove.show()
        except mysql.connector.Error as e:
            print(e)
            self.ErrorReport(str(format(e)))

    def FuncAddButton(self):
        if self.list_widget_available.selectedItems():
            text = self.list_widget_available.currentItem().text()
            add = self.list_widget_available.selectedItems()
            if not add: return
            for item in add:
                if self.list_widget_allotted.count() < 7:
                    self.list_widget_available.takeItem(self.list_widget_available.row(item))
                    self.list_widget_allotted.addItem(str(text))
                    self.button_update.show()
                else:
                    self.ErrorReport(str("Can't assign more then 7 subject"))

    def FuncRemoveButton(self):
        if self.list_widget_allotted.selectedItems():
            text = self.list_widget_allotted.currentItem().text()
            remv = self.list_widget_allotted.selectedItems()
            if not  remv: return
            for item in remv:
                self.list_widget_allotted.takeItem(self.list_widget_allotted.row(item))
            self.list_widget_available.addItem(str(text))
            self.list_widget_allotted.setFocus()
            self.button_update.show()

    def FuncUpdateButton(self):
        items = []
        for index in range(self.list_widget_allotted.count()):
            items.append(self.list_widget_allotted.item(index).text())
        print("all the list member")
        for i in range(len(items)):
            print(items[i])
        stp4 = len(items)
        empty = [None, None, None, None, None, None, None, None]
        items.extend(empty)

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='collegeattend',
                                                 user='root',
                                                 password='')
            cursor = connection.cursor()
            cursor.execute("UPDATE `subjectteacher` SET `subject1`=%s,`subject2`=%s,`subject3`=%s,`subject4`=%s,`subject5`=%s,`subject6`=%s,`subject7`=%s WHERE `teacherid`=%s",
                (items[0], items[1], items[2], items[3], items[4], items[5], items[6], self.tid,))
            connection.commit()
            self.button_remove.hide()
            self.button_update.hide()
            self.button_add.hide()
            self.list_widget_allotted.clear()
            print("Record inserted successfully into " + str(self.tid) + "table")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
            self.ErrorReport(format(error))

    def ErrorReport(self,message):
        messageBox = QtWidgets.QMessageBox()
        ui = Ui_Dialog(message)
        ui.setupUi(messageBox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    subject_allotment = QtWidgets.QWidget()
    ui = Ui_subject_allotment()
    ui.setupUi(subject_allotment)
    subject_allotment.show()
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
