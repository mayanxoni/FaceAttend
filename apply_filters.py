from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from update_attendance import UpdateAttendance


class ApplyFilters(object):

    def __init__(self, user_name):
        self.user_name = user_name
        self.combo_box_date = QtWidgets.QComboBox()
        self.combo_box_subject = QtWidgets.QComboBox()

    def setup_ui(self, apply_filters_object):
        apply_filters_object.setObjectName("apply_filters_object")
        apply_filters_object.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        apply_filters_object.setWindowIcon(icon)
        self.grid_layout = QtWidgets.QGridLayout(apply_filters_object)
        self.grid_layout.setObjectName("grid_layout")
        self.label_filter_icon = QtWidgets.QLabel(apply_filters_object)
        self.label_filter_icon.setText("")
        self.label_filter_icon.setPixmap(QtGui.QPixmap("assets/filter.png"))
        self.label_filter_icon.setScaledContents(True)
        self.label_filter_icon.setObjectName("label_filter_icon")
        self.grid_layout.addWidget(self.label_filter_icon, 8, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.button_select = QtWidgets.QPushButton(apply_filters_object)
        self.button_select.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/select.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_select.setIcon(icon1)
        self.button_select.setIconSize(QtCore.QSize(32, 32))
        self.button_select.setFlat(False)
        self.button_select.setObjectName("button_select")
        self.grid_layout.addWidget(self.button_select, 13, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(apply_filters_object)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.grid_layout.addWidget(self.label_spacer_bottom, 12, 1, 1, 1)
        self.grid_layout_1 = QtWidgets.QGridLayout()
        self.grid_layout_1.setObjectName("grid_layout_1")
        self.button_back = QtWidgets.QPushButton(apply_filters_object)
        self.button_back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon2)
        self.button_back.setIconSize(QtCore.QSize(32, 32))
        self.button_back.setFlat(True)
        self.button_back.setObjectName("button_back")
        self.grid_layout_1.addWidget(self.button_back, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_update_attendance = QtWidgets.QLabel(apply_filters_object)
        self.label_update_attendance.setObjectName("label_update_attendance")
        self.grid_layout_1.addWidget(self.label_update_attendance, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_spacer = QtWidgets.QLabel(apply_filters_object)
        self.label_spacer.setText("")
        self.label_spacer.setObjectName("label_spacer")
        self.grid_layout_1.addWidget(self.label_spacer, 0, 2, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_1, 0, 0, 1, 3)
        self.label_placeholder = QtWidgets.QLabel(apply_filters_object)
        self.label_placeholder.setObjectName("label_placeholder")
        self.grid_layout.addWidget(self.label_placeholder, 9, 1, 1, 1)
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.combo_box_date = QtWidgets.QComboBox(apply_filters_object)
        self.combo_box_date.setObjectName("combo_box_date")
        self.grid_layout_2.addWidget(self.combo_box_date, 1, 2, 1, 1)
        self.label_subject = QtWidgets.QLabel(apply_filters_object)
        self.label_subject.setObjectName("label_subject")
        self.grid_layout_2.addWidget(self.label_subject, 0, 1, 1, 1)
        self.label_date = QtWidgets.QLabel(apply_filters_object)
        self.label_date.setObjectName("label_date")
        self.grid_layout_2.addWidget(self.label_date, 0, 2, 1, 1)
        self.combo_box_subject = QtWidgets.QComboBox(apply_filters_object)
        self.combo_box_subject.setObjectName("combo_box_subject")
        self.grid_layout_2.addWidget(self.combo_box_subject, 1, 1, 1, 1)
        self.label_spacer_right = QtWidgets.QLabel(apply_filters_object)
        self.label_spacer_right.setText("")
        self.label_spacer_right.setObjectName("label_spacer_right")
        self.grid_layout_2.addWidget(self.label_spacer_right, 0, 3, 1, 1)
        self.label_spacer_left = QtWidgets.QLabel(apply_filters_object)
        self.label_spacer_left.setText("")
        self.label_spacer_left.setObjectName("label_spacer_left")
        self.grid_layout_2.addWidget(self.label_spacer_left, 0, 0, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_2, 10, 0, 1, 3)
        self.label_spacer_top = QtWidgets.QLabel(apply_filters_object)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.grid_layout.addWidget(self.label_spacer_top, 1, 1, 1, 1)

        apply_filters_object.setWindowTitle("Apply Filters")
        self.label_update_attendance.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; "
                                             "font-weight:600; color:#888a85;\">APPLY "
                                             "FILTERS</span></p></body></html>")
        self.label_placeholder.setText("Select the subject and the corresponding date for which you want to update "
                                       "the record:")
        self.label_subject.setText("Subject:")
        self.label_date.setText("Date:")

        self.update_subject()
        self.button_back.clicked.connect(lambda: self.back(apply_filters_object))
        self.combo_box_subject.currentTextChanged.connect(self.update_date)
        self.button_select.clicked.connect(self.button_update)
        QtCore.QMetaObject.connectSlotsByName(apply_filters_object)
        apply_filters_object.setTabOrder(self.button_select, self.button_back)

    def update_subject(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            db_cursor = connection.cursor()
            teacher_id_query = "SELECT * FROM subjectteacher WHERE teacherid = " + self.user_name
            db_cursor.execute(teacher_id_query)
            teacher_id_result = db_cursor.fetchone()
            if teacher_id_result is None:
                print("Error!")
            else:
                for row in teacher_id_result:
                    if row != self.user_name:
                        if row:
                            self.combo_box_subject.addItem(row)
        except mysql.connector.Error as er:
            print(er)

    def update_date(self, new_subject):
        print(new_subject)
        self.new_subject = new_subject
        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="collegeattend",
                user="root",
                passwd=""
            )
            db_cursor = connection.cursor()
            class_date_query = "SELECT classdate FROM `" + str(new_subject) + "` ORDER BY classdate ASC"
            print(class_date_query)
            db_cursor.execute(class_date_query)
            class_date_result = db_cursor.fetchall()
            if class_date_result is None:
                print("Error!")
            else:
                self.combo_box_date.clear()
                for i in class_date_result:
                    print(i[0])
                    self.combo_box_date.addItem(str(i[0]))
        except mysql.connector.Error as er:
            print(er)

    def button_update(self):
        global semester
        class_date = self.combo_box_date.currentText()
        print(str(class_date))
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=""
            )
            db_cursor = connection.cursor()
            semester_query = "SELECT semestername FROM collegeattend.collgdatatable WHERE " + self.new_subject + " IN(subject1, " \
                                                                                                     "subject2, " \
                                                                                                     "subject3," \
                                                                                                     "subject4," \
                                                                                                     "subject5," \
                                                                                                     "subject6," \
                                                                                                     "subject7) "
            db_cursor.execute(semester_query)
            query_result = db_cursor.fetchone()
            if query_result is None:
                print("Error!")
            else:
                for row in query_result:
                    semester = row
        except mysql.connector.Error as er:
            print(er)
        self.win_update_attend = QtWidgets.QWidget()
        self.ui = UpdateAttendance(self.user_name, semester, self.new_subject, class_date, )
        self.ui.setup_ui(self.win_update_attend)
        self.win_update_attend.show()

    @staticmethod
    def back(apply_filters_object):
        apply_filters_object.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    apply_filters_object = QtWidgets.QWidget()
    apply_filters = ApplyFilters()
    apply_filters.setup_ui(apply_filters_object)
    apply_filters_object.show()
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
