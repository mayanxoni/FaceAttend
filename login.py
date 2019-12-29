import hashlib

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow 

from ErrorMessg import  Ui_Dialog
from signup import Ui_form_signup
from dashboard import Ui_form_dashboard
from admin_panel import  Ui_form_admin_panel
from  Information import  Ui_Info


class Ui_form_login(object):
    def setupUi(self, form_login):
        self.from_login = form_login
        form_login.setObjectName("form_login")
        form_login.setWindowModality(QtCore.Qt.ApplicationModal)
        form_login.setEnabled(True)
        form_login.resize(380, 420)
        form_login.setFixedSize(380, 420)
        form_login.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_login.setWindowIcon(icon)
        form_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        form_login.setAutoFillBackground(False)
        form_login.setTabShape(QtWidgets.QTabWidget.Rounded)
        form_login.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        form_login.setUnifiedTitleAndToolBarOnMac(False)
        self.central_widget = QtWidgets.QWidget(form_login)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.label_spacer_top = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.grid_layout.addWidget(self.label_spacer_top, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.grid_layout, 0, 0, 1, 1)
        self.button_signup = QtWidgets.QPushButton(self.central_widget)
        self.button_signup.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_signup.setIcon(icon1)
        self.button_signup.setObjectName("button_signup")
        self.gridLayout.addWidget(self.button_signup, 9, 0, 1, 1)
        self.line_edit_password = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_password.setClearButtonEnabled(True)
        self.line_edit_password.setObjectName("line_edit_password")
        self.gridLayout.addWidget(self.line_edit_password, 4, 0, 1, 1)
        self.label_placeholder = QtWidgets.QLabel(self.central_widget)
        self.label_placeholder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_placeholder.setAlignment(QtCore.Qt.AlignCenter)
        self.label_placeholder.setObjectName("label_placeholder")
        self.gridLayout.addWidget(self.label_placeholder, 8, 0, 1, 1)
        self.label_faceattend_icon = QtWidgets.QLabel(self.central_widget)
        self.label_faceattend_icon.setText("")
        self.label_faceattend_icon.setPixmap(QtGui.QPixmap("assets/FaceAttend2.png"))
        self.label_faceattend_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_faceattend_icon.setObjectName("label_faceattend_icon")
        self.gridLayout.addWidget(self.label_faceattend_icon, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.gridLayout.addWidget(self.label_spacer_bottom, 10, 0, 1, 1)
        self.label_spacer_middle_2 = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_middle_2.setText("")
        self.label_spacer_middle_2.setObjectName("label_spacer_middle_2")
        self.gridLayout.addWidget(self.label_spacer_middle_2, 7, 0, 1, 1)
        self.line_edit_username = QtWidgets.QLineEdit(self.central_widget)
        self.line_edit_username.setMouseTracking(True)
        self.line_edit_username.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.line_edit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_username.setClearButtonEnabled(True)
        self.line_edit_username.setObjectName("line_edit_username")
        self.gridLayout.addWidget(self.line_edit_username, 3, 0, 1, 1)
        self.button_login = QtWidgets.QPushButton(self.central_widget)
        self.button_login.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_login.setIcon(icon2)
        self.button_login.setObjectName("button_login")
        self.gridLayout.addWidget(self.button_login, 6, 0, 1, 1)
        self.label_spacer_middle_1 = QtWidgets.QLabel(self.central_widget)
        self.label_spacer_middle_1.setText("")
        self.label_spacer_middle_1.setObjectName("label_spacer_middle_1")
        self.gridLayout.addWidget(self.label_spacer_middle_1, 2, 0, 1, 1)
        form_login.setCentralWidget(self.central_widget)

        self.retranslateUi(form_login)
        QtCore.QMetaObject.connectSlotsByName(form_login)
        form_login.setTabOrder(self.line_edit_username, self.line_edit_password)
        form_login.setTabOrder(self.line_edit_password, self.button_login)
        form_login.setTabOrder(self.button_login, self.button_signup)
        self.button_login.clicked.connect(lambda :self.FunChecking(form_login))
        self.line_edit_password.returnPressed.connect(lambda :self.FunChecking(form_login))
        self.button_signup.clicked.connect(lambda :self.FuncSignup(form_login))

    def retranslateUi(self, form_login):
        _translate = QtCore.QCoreApplication.translate
        form_login.setWindowTitle(_translate("form_login", "Login"))
        self.button_signup.setToolTip(_translate("form_login", "Click to get yourself signed up!"))
        self.button_signup.setText(_translate("form_login", "Signup"))
        self.line_edit_password.setToolTip(_translate("form_login", "Enter your password."))
        self.line_edit_password.setPlaceholderText(_translate("form_login", "Password"))
        self.label_placeholder.setText(_translate("form_login", "Don\'t have access to username/password?\n""Contact Computer Centre or Signup to gain access."))
        self.line_edit_username.setToolTip(_translate("form_login", "Enter your username."))
        self.line_edit_username.setPlaceholderText(_translate("form_login", "Username"))
        self.button_login.setToolTip(_translate("form_login", "Click to Login!"))
        self.button_login.setText(_translate("form_login", "Login"))


    def FunChecking(self,form_login):
        UserName = self.line_edit_username.text()
        PassWD = self.line_edit_password.text()
        Pass2 = hashlib.sha1(str(PassWD).encode())
        PassWD = Pass2.hexdigest()
        if UserName == "" and  self.line_edit_password.text() == "":
            self.ErrorReport(str("Please Enter Your Username And Password."))
        elif UserName == "" :
            self.ErrorReport(str("Please Enter Your Useraname."))
        elif self.line_edit_password.text() == "" :
            self.ErrorReport(str("Please Enter Your Password. "))
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="collegeattend",
                passwd=""
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT userid FROM userdatabase where userid = %s and pass = %s",(UserName, PassWD,))
            myresult = mycursor.fetchone()
            if myresult is None:
                self.ErrorReport(str("Username or password don't match."))
            elif myresult[0] == "Admin":
                self.InfoReport(str("admin account"))
                self.WinAdmin = QtWidgets.QWidget()
                self.ui = Ui_form_admin_panel(form_login)
                self.ui.setupUi(self.WinAdmin)
                form_login.hide()
                self.line_edit_username.clear()
                self.line_edit_password.clear()
                self.WinAdmin.show()
            else:
                self.InfoReport(str("Teacher account"))
                self.WinDash = QtWidgets.QWidget()
                self.ui = Ui_form_dashboard(UserName,form_login)
                self.ui.setupUi(self.WinDash)
                form_login.hide()
                self.line_edit_username.clear()
                self.line_edit_password.clear()
                self.WinDash.show()

        except mysql.connector.Error as e:
            self.ErrorReport(str("Database server didn't respond please make sure college database server is working "))
            print(e.errno)
            print(e.sqlstate)
            print("Failed to insert into MySQL table {}".format(e))


    def FuncSignup(self,form_login):
        self.WinSignup = QtWidgets.QWidget()
        self.ui = Ui_form_signup(form_login)
        self.ui.setupUi(self.WinSignup)
        form_login.hide()
        self.WinSignup.show()



    def ErrorReport(self,message):
        messageBox = QtWidgets.QMessageBox()
        ui = Ui_Dialog(message)
        ui.setupUi(messageBox)

    def InfoReport(self,message):
        messageBox = QtWidgets.QMessageBox()
        ui = Ui_Info(message)
        ui.setupUi(messageBox)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_login = QtWidgets.QMainWindow()
    ui = Ui_form_login()
    ui.setupUi(form_login)
    form_login.show()
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
