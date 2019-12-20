import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from error_message import ErrorMessage


class SubjectAllotment(object):
    def setup_ui(self, subject_allotment_object):
        subject_allotment_object.setObjectName("subject_allotment_object")
        subject_allotment_object.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        subject_allotment_object.setWindowIcon(icon)
        self.gridLayout_4 = QtWidgets.QGridLayout(subject_allotment_object)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.list_widget_available = QtWidgets.QListWidget(subject_allotment_object)
        self.list_widget_available.setObjectName("list_widget_available")
        self.gridLayout_4.addWidget(self.list_widget_available, 6, 0, 11, 1)
        self.button_remove = QtWidgets.QPushButton(subject_allotment_object)
        self.button_remove.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_remove.setIcon(icon1)
        self.button_remove.setIconSize(QtCore.QSize(32, 32))
        self.button_remove.setFlat(False)
        self.button_remove.setObjectName("button_remove")
        self.gridLayout_4.addWidget(self.button_remove, 12, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.button_add = QtWidgets.QPushButton(subject_allotment_object)
        self.button_add.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add.setIcon(icon2)
        self.button_add.setIconSize(QtCore.QSize(32, 32))
        self.button_add.setFlat(False)
        self.button_add.setObjectName("button_add")
        self.gridLayout_4.addWidget(self.button_add, 10, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.button_select = QtWidgets.QPushButton(subject_allotment_object)
        self.button_select.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_select.setIcon(icon3)
        self.button_select.setIconSize(QtCore.QSize(32, 32))
        self.button_select.setFlat(False)
        self.button_select.setObjectName("button_select")
        self.gridLayout_4.addWidget(self.button_select, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_placeholder = QtWidgets.QLabel(subject_allotment_object)
        self.label_placeholder.setObjectName("label_placeholder")
        self.gridLayout_4.addWidget(self.label_placeholder, 2, 0, 1, 3, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.list_widget_allotted = QtWidgets.QListWidget(subject_allotment_object)
        self.list_widget_allotted.setObjectName("list_widget_allotted")
        self.gridLayout_4.addWidget(self.list_widget_allotted, 6, 2, 11, 1)
        self.label_teachers_icon = QtWidgets.QLabel(subject_allotment_object)
        self.label_teachers_icon.setText("")
        self.label_teachers_icon.setPixmap(QtGui.QPixmap("assets/group.png"))
        self.label_teachers_icon.setObjectName("label_teachers_icon")
        self.gridLayout_4.addWidget(self.label_teachers_icon, 0, 1, 1, 1)
        self.label_available = QtWidgets.QLabel(subject_allotment_object)
        self.label_available.setObjectName("label_available")
        self.gridLayout_4.addWidget(self.label_available, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_allotted = QtWidgets.QLabel(subject_allotment_object)
        self.label_allotted.setObjectName("label_allotted")
        self.gridLayout_4.addWidget(self.label_allotted, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.button_update = QtWidgets.QPushButton(subject_allotment_object)
        self.button_update.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon4)
        self.button_update.setIconSize(QtCore.QSize(32, 32))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.gridLayout_4.addWidget(self.button_update, 18, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(subject_allotment_object)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.gridLayout_4.addWidget(self.label_spacer_bottom, 15, 1, 1, 1)
        self.label_spacer_top = QtWidgets.QLabel(subject_allotment_object)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.gridLayout_4.addWidget(self.label_spacer_top, 9, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(subject_allotment_object)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_4.addWidget(self.comboBox, 3, 0, 1, 3)
        self.button_add.hide()
        self.button_update.hide()
        self.button_remove.hide()

        subject_allotment_object.setWindowTitle("Subject Allotment")
        self.label_placeholder.setText("You can allot or withhold the subject(s) by selecting name of the teacher "
                                       "from the list below:")
        self.label_available.setText("Available Subject(s)")
        self.label_allotted.setText("Allotted Subject(s)")

        self.load_user()
        self.prepare_subjects_list()
        self.button_select.clicked.connect(self.FuncOnSelectUser)
        self.button_add.clicked.connect(self.FuncAddButton)
        self.button_remove.clicked.connect(self.FuncRemoveButton)
        self.button_update.clicked.connect(self.update_subjects)
        QtCore.QMetaObject.connectSlotsByName(subject_allotment_object)
        subject_allotment_object.setTabOrder(self.comboBox, self.button_select)
        subject_allotment_object.setTabOrder(self.button_select, self.list_widget_available)
        subject_allotment_object.setTabOrder(self.list_widget_available, self.list_widget_allotted)
        subject_allotment_object.setTabOrder(self.list_widget_allotted, self.button_add)
        subject_allotment_object.setTabOrder(self.button_add, self.button_remove)
        subject_allotment_object.setTabOrder(self.button_remove, self.button_update)

    def load_user(self):
        self.teacher_id = []
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            details_query = "SELECT userid, teachername FROM userdatabase"
            db_cursor.execute(details_query)
            details_result = db_cursor.fetchall()
            if details_result is None:
                self.error_report(str("No user in database"))
            else:
                for row in details_result:
                    if row[0] != "Admin":
                        self.comboBox.addItem(str(row[1]))
                        self.teacher_id.append(str(row[0]))
        except mysql.connector.Error as er:
            print(er)
            self.error_report(format(er))

    def prepare_subjects_list(self):
        subjects_list = []
        reserved_subject_list = []
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            available_subjects_query = "SELECT subject1, subject2, subject3, subject4, subject5, subject6, subject7 " \
                                       "FROM collgdatatable"
            db_cursor.execute(available_subjects_query)
            available_subjects_result = db_cursor.fetchall()
            if available_subjects_result is None:
                self.error_report(str("All subjects have been allotted!"))
            else:
                for row in available_subjects_result:
                    for index1 in range(7):
                        if row[index1] != "":
                            subjects_list.append(str(row[index1]))
                subject_list_size1 = len(subjects_list)
        except mysql.connector.Error as e:
            print(e)
            self.error_report(format(e))

        # this is for the already alloted subjects
        try:
            db_cursor = connection.cursor()
            allotted_subjects_query = "SELECT subject1, subject2, subject3, subject4, subject5, subject6, subject7 " \
                                      "FROM subjectteacher"
            db_cursor.execute(allotted_subjects_query)
            allotted_subjects_result = db_cursor.fetchall()
            if allotted_subjects_result is None:
                print("Blank Object!")
                pass
            else:
                for row in allotted_subjects_result:
                    for index1 in range(7):
                        if row[index1] != "":
                            reserved_subject_list.append(str(row[index1]))
                subject_list_size2 = len(reserved_subject_list)
        except mysql.connector.Error as e:
            print(e)
            self.error_report(format(e))

        # this is the final list that is going to be shown
        final_subjects_list = []
        for index1 in range(subject_list_size1):
            flag = 0
            for index2 in range(subject_list_size2):
                if str(subjects_list[index1]) == str(reserved_subject_list[index2]):
                    flag = 1
            if flag == 0:
                final_subjects_list.append(str(subjects_list[index1]))

        final_subject_list_size = len(final_subjects_list)
        for index in range(final_subject_list_size):
            print(final_subjects_list[index])

        self.list_widget_available.addItems(final_subjects_list)

    def FuncOnSelectUser(self):
        self.list_widget_allotted.clear()
        subject_list = []
        current_index = self.comboBox.currentIndex()
        self.teacher_id = self.teacher_id[current_index]
        print(self.teacher_id)
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            subjects_query = "SELECT subject1, subject2, subject3, subject4, subject5, subject6, subject7 " \
                             "FROM subjectteacher WHERE teacherid = '" + str(self.teacher_id[current_index]) + "'"
            db_cursor.execute(subjects_query)
            subjects_result = db_cursor.fetchone()
            if subjects_result is None:
                "INSERT INTO `subjectteacher`(`teacherid`) VALUES ('" + str(self.teacher_id[current_index]) + "')"
                db_cursor.execute()
                connection.commit()
                self.error_report(str("Please select again!"))
            else:
                for row in subjects_result:
                    if row is not None:
                        subject_list.append(str(row))

                self.list_widget_allotted.addItems(subject_list)
                self.list_widget_allotted.show()
                self.button_add.show()
                self.button_remove.show()
        except mysql.connector.Error as e:
            print(e)
            self.error_report(str(format(e)))

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
                    self.error_report(str("Can't assign more then 7 subject"))

    def FuncRemoveButton(self):
        if self.list_widget_allotted.selectedItems():
            text = self.list_widget_allotted.currentItem().text()
            remv = self.list_widget_allotted.selectedItems()
            if not remv: return
            for item in remv:
                self.list_widget_allotted.takeItem(self.list_widget_allotted.row(item))
            self.list_widget_available.addItem(str(text))
            self.list_widget_allotted.setFocus()
            self.button_update.show()

    def update_subjects(self):
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
            update_teacher_subjects = "UPDATE `subjectteacher` SET `subject1` = " + items[0] + \
                                      ", `subject2` = " + items[1] + ", `subject3` = " + items[2] + \
                                      ", `subject4` = " + items[3] + ", `subject5` = " + items[4] + \
                                      ", `subject6` = " + items[5] + ", `subject7` = " + items[6] + \
                                      " WHERE `teacherid` = " + self.teacher_id
            cursor.execute(update_teacher_subjects)
            connection.commit()
            self.button_remove.hide()
            self.button_update.hide()
            self.button_add.hide()
            self.list_widget_allotted.clear()
            print("Record successfully inserted into " + str(self.teacher_id) + "table.")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))
            self.error_report(format(error))

    @staticmethod
    def error_report(message):
        message_box = QtWidgets.QMessageBox()
        ui = ErrorMessage(message)
        ui.setup_ui(message_box)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    subject_allotment_object = QtWidgets.QWidget()
    subject_allotment = SubjectAllotment()
    subject_allotment.setup_ui(subject_allotment_object)
    subject_allotment_object.show()
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
