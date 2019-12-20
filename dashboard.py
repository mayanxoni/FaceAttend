from PyQt5 import QtCore, QtGui, QtWidgets
from record_attendance import RecordAttendance
from apply_filters import ApplyFilters


class Dashboard(object):

    def __init__(self, user_name, form):
        self.form = form
        self.user_name = user_name

    def setup_ui(self, dashboard_object):
        dashboard_object.setObjectName("dashboard_object")
        dashboard_object.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dashboard_object.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(dashboard_object)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_layout_top = QtWidgets.QGridLayout()
        self.grid_layout_top.setObjectName("grid_layout_top")
        self.button_logout = QtWidgets.QPushButton(dashboard_object)
        self.button_logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_logout.setIcon(icon1)
        self.button_logout.setIconSize(QtCore.QSize(32, 32))
        self.button_logout.setFlat(True)
        self.button_logout.setObjectName("button_logout")
        self.grid_layout_top.addWidget(self.button_logout, 0, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.grid_layout_top)
        self.label_teacher_dashboard = QtWidgets.QLabel(dashboard_object)
        self.label_teacher_dashboard.setObjectName("label_teacher_dashboard")
        self.verticalLayout.addWidget(self.label_teacher_dashboard)
        self.label_greetings = QtWidgets.QLabel(dashboard_object)
        self.label_greetings.setAlignment(QtCore.Qt.AlignCenter)
        self.label_greetings.setObjectName("label_greetings")
        self.verticalLayout.addWidget(self.label_greetings, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_dashboard_icon = QtWidgets.QLabel(dashboard_object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dashboard_icon.sizePolicy().hasHeightForWidth())
        self.label_dashboard_icon.setSizePolicy(sizePolicy)
        self.label_dashboard_icon.setMinimumSize(QtCore.QSize(1, 1))
        self.label_dashboard_icon.setBaseSize(QtCore.QSize(0, 0))
        self.label_dashboard_icon.setText("")
        self.label_dashboard_icon.setPixmap(QtGui.QPixmap("assets/briefcase.png"))
        self.label_dashboard_icon.setObjectName("label_dashboard_icon")
        self.verticalLayout.addWidget(self.label_dashboard_icon, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_spacer_middle = QtWidgets.QLabel(dashboard_object)
        self.label_spacer_middle.setText("")
        self.label_spacer_middle.setObjectName("label_spacer_middle")
        self.verticalLayout.addWidget(self.label_spacer_middle)
        self.label_placeholder = QtWidgets.QLabel(dashboard_object)
        self.label_placeholder.setObjectName("label_placeholder")
        self.verticalLayout.addWidget(self.label_placeholder, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid_layout_1 = QtWidgets.QGridLayout()
        self.grid_layout_1.setObjectName("grid_layout_1")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.grid_layout_2 = QtWidgets.QGridLayout()
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.button_update = QtWidgets.QPushButton(dashboard_object)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon2)
        self.button_update.setIconSize(QtCore.QSize(64, 64))
        self.button_update.setFlat(False)
        self.button_update.setObjectName("button_update")
        self.grid_layout_2.addWidget(self.button_update, 1, 3, 1, 1, QtCore.Qt.AlignVCenter)
        self.button_register = QtWidgets.QPushButton(dashboard_object)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_register.setIcon(icon3)
        self.button_register.setIconSize(QtCore.QSize(64, 64))
        self.button_register.setFlat(False)
        self.button_register.setObjectName("button_register")
        self.grid_layout_2.addWidget(self.button_register, 1, 5, 1, 1, QtCore.Qt.AlignVCenter)
        self.button_record = QtWidgets.QPushButton(dashboard_object)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_record.setIcon(icon4)
        self.button_record.setIconSize(QtCore.QSize(64, 64))
        self.button_record.setFlat(False)
        self.button_record.setObjectName("button_record")
        self.grid_layout_2.addWidget(self.button_record, 1, 1, 1, 1, QtCore.Qt.AlignVCenter)
        self.label_spacer_2 = QtWidgets.QLabel(dashboard_object)
        self.label_spacer_2.setText("")
        self.label_spacer_2.setObjectName("label_spacer_2")
        self.grid_layout_2.addWidget(self.label_spacer_2, 1, 6, 1, 1)
        self.line = QtWidgets.QFrame(dashboard_object)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.grid_layout_2.addWidget(self.line, 1, 2, 1, 1)
        self.label_spacer_1 = QtWidgets.QLabel(dashboard_object)
        self.label_spacer_1.setText("")
        self.label_spacer_1.setObjectName("label_spacer_1")
        self.grid_layout_2.addWidget(self.label_spacer_1, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(dashboard_object)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.grid_layout_2.addWidget(self.line_2, 1, 4, 1, 1)
        self.horizontal_layout.addLayout(self.grid_layout_2)
        self.grid_layout_1.addLayout(self.horizontal_layout, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.grid_layout_1)
        self.label_spacer_bottom = QtWidgets.QLabel(dashboard_object)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.verticalLayout.addWidget(self.label_spacer_bottom)

        dashboard_object.setWindowTitle("Dashboard")
        self.button_logout.setToolTip("Terminate Session")
        self.label_teacher_dashboard.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; "
                                             "font-weight:600; color:#888a85;\">TEACHER "
                                             "DASHBOARD</span></p></body></html>")
        self.label_greetings.setText("Hello Teacher, hope you\'re having a good day!")
        self.label_placeholder.setText("Please choose any one of the operations to get started!")
        self.button_update.setToolTip("Update Attendance")
        self.button_update.setText("Update Attendance")
        self.button_register.setToolTip("Register Faces")
        self.button_register.setText("Register Faces")
        self.button_record.setToolTip("Record Attendance")
        self.button_record.setText("Record Attendance")

        QtCore.QMetaObject.connectSlotsByName(dashboard_object)
        dashboard_object.setTabOrder(self.button_record, self.button_update)
        dashboard_object.setTabOrder(self.button_update, self.button_register)
        dashboard_object.setTabOrder(self.button_register, self.button_logout)
        self.button_record.clicked.connect(self.record_attendance)
        self.button_logout.clicked.connect(lambda: self.logout(dashboard_object))
        self.button_update.clicked.connect(self.update_attendance)

    def record_attendance(self):
        self.win_record_attendance = QtWidgets.QWidget()
        self.ui = RecordAttendance(self.user_name)
        self.ui.setupUi(self.win_record_attendance)
        self.win_record_attendance.show()

    def update_attendance(self):
        self.win_apply_filters = QtWidgets.QWidget()
        self.ui = ApplyFilters(self.user_name)
        self.ui.setup_ui(self.win_apply_filters)
        self.win_apply_filters.show()

    def logout(self, form_dashboard):
        form_dashboard.close()
        self.form.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form_dashboard = QtWidgets.QWidget()
    ui = Dashboard()
    ui.setup_ui(form_dashboard)
    form_dashboard.show()
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
