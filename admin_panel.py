from performance_analysis import Ui_performance_analysis
from PyQt5 import QtCore, QtGui, QtWidgets
from subject_allotment import Ui_subject_allotment


class AdminPanel(object):

    def __init__(self, form):
        self.form = form

    def setup_ui(self, admin_panel_object):
        admin_panel_object.setObjectName("admin_panel_object")
        admin_panel_object.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_panel_object.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(admin_panel_object)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.button_logout = QtWidgets.QPushButton(admin_panel_object)
        self.button_logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_logout.setIcon(icon1)
        self.button_logout.setIconSize(QtCore.QSize(32, 32))
        self.button_logout.setFlat(True)
        self.button_logout.setObjectName("button_logout")
        self.grid_layout.addWidget(self.button_logout, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.grid_layout)
        self.label_admin_panel = QtWidgets.QLabel(admin_panel_object)
        self.label_admin_panel.setObjectName("label_admin_panel")
        self.verticalLayout.addWidget(self.label_admin_panel)
        self.label_admin_icon = QtWidgets.QLabel(admin_panel_object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_admin_icon.sizePolicy().hasHeightForWidth())
        self.label_admin_icon.setSizePolicy(sizePolicy)
        self.label_admin_icon.setMinimumSize(QtCore.QSize(1, 1))
        self.label_admin_icon.setBaseSize(QtCore.QSize(0, 0))
        self.label_admin_icon.setText("")
        self.label_admin_icon.setPixmap(QtGui.QPixmap("assets/admin.png"))
        self.label_admin_icon.setObjectName("label_admin_icon")
        self.verticalLayout.addWidget(self.label_admin_icon, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_designation = QtWidgets.QLabel(admin_panel_object)
        self.label_designation.setObjectName("label_designation")
        self.verticalLayout.addWidget(self.label_designation, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_spacer_middle = QtWidgets.QLabel(admin_panel_object)
        self.label_spacer_middle.setText("")
        self.label_spacer_middle.setObjectName("label_spacer_middle")
        self.verticalLayout.addWidget(self.label_spacer_middle)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.button_subject_allotment = QtWidgets.QPushButton(admin_panel_object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_subject_allotment.sizePolicy().hasHeightForWidth())
        self.button_subject_allotment.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/teachers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_subject_allotment.setIcon(icon2)
        self.button_subject_allotment.setIconSize(QtCore.QSize(64, 64))
        self.button_subject_allotment.setObjectName("button_subject_allotment")
        self.horizontal_layout.addWidget(self.button_subject_allotment)
        self.divider_line = QtWidgets.QFrame(admin_panel_object)
        self.divider_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.divider_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_line.setObjectName("divider_line")
        self.horizontal_layout.addWidget(self.divider_line)
        self.button_performance_analysis = QtWidgets.QPushButton(admin_panel_object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_performance_analysis.sizePolicy().hasHeightForWidth())
        self.button_performance_analysis.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/line_chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_performance_analysis.setIcon(icon3)
        self.button_performance_analysis.setIconSize(QtCore.QSize(64, 64))
        self.button_performance_analysis.setFlat(False)
        self.button_performance_analysis.setObjectName("button_performance_analysis")
        self.horizontal_layout.addWidget(self.button_performance_analysis)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.label_spacer_bottom = QtWidgets.QLabel(admin_panel_object)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.verticalLayout.addWidget(self.label_spacer_bottom)

        admin_panel_object("Admin Panel")
        self.button_logout.setToolTip("Terminate Session")
        self.label_admin_panel.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                       "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                       "type=\"text/css\">\n "
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'Google Sans\'; font-size:11pt; "
                                       "font-weight:400; font-style:normal;\">\n "
                                       "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                       "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                       "text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; "
                                       "color:#888a85;\">ADMIN PANEL</span></p></body></html>")
        self.label_designation.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Head "
                                       "of Department</span></p><p align=\"center\"><span style=\" "
                                       "font-size:12pt;\">Department of Computer Science</span></p><p "
                                       "align=\"center\"><span style=\" font-size:12pt;\">Mohanlal Sukhadia "
                                       "University</span></p></body></html>")
        self.button_subject_allotment.setToolTip("Subject Allotment")
        self.button_subject_allotment.setText("Subject Allotment")
        self.button_performance_analysis.setToolTip("Performance Analysis")
        self.button_performance_analysis.setText("Performance Analysis")

        QtCore.QMetaObject.connectSlotsByName(admin_panel_object)
        admin_panel_object.setTabOrder(self.button_subject_allotment, self.button_performance_analysis)
        admin_panel_object.setTabOrder(self.button_performance_analysis, self.button_logout)
        self.button_logout.clicked.connect(lambda: self.logout(admin_panel_object))
        self.button_subject_allotment.clicked.connect(self.subject_allocation)
        self.button_performance_analysis.clicked.connect(self.performance_analysis)

    def logout(self, form_admin_panel):
        form_admin_panel.close()
        self.form.show()
        # self.WinLogin = QtWidgets.QMainWindow()
        # self.ui = form_login()
        # self.ui.setup_ui(self.WinLogin)
        # self.WinLogin.show()

    def subject_allocation(self):
        self.win_subject_allotment = QtWidgets.QWidget()
        self.ui = Ui_subject_allotment()
        self.ui.setupUi(self.win_subject_allotment)
        self.win_subject_allotment.show()

    def performance_analysis(self):
        self.win_performance = QtWidgets.QWidget()
        self.ui = Ui_performance_analysis()
        self.ui.setupUi(self.win_performance)
        self.win_performance.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    admin_panel = QtWidgets.QWidget()
    ui = AdminPanel()
    ui.setup_ui(admin_panel)
    admin_panel.show()
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
