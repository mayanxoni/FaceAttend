import hashlib
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from error_message import ErrorMessage


class Signup(object):

    def __init__(self, signup_object):
        self.signup_object = signup_object

    def setup_ui(self, signup_object):
        signup_object.setObjectName("signup_object")
        signup_object.resize(380, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        signup_object.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(signup_object)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_signup = QtWidgets.QPushButton(signup_object)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_signup.setIcon(icon1)
        self.button_signup.setObjectName("button_signup")
        self.verticalLayout_2.addWidget(self.button_signup)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 9, 0, 1, 1)
        self.label_faceattend_icon = QtWidgets.QLabel(signup_object)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_faceattend_icon.sizePolicy().hasHeightForWidth())
        self.label_faceattend_icon.setSizePolicy(sizePolicy)
        self.label_faceattend_icon.setMinimumSize(QtCore.QSize(1, 1))
        self.label_faceattend_icon.setBaseSize(QtCore.QSize(0, 0))
        self.label_faceattend_icon.setText("")
        self.label_faceattend_icon.setPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"))
        self.label_faceattend_icon.setObjectName("label_faceattend_icon")
        self.gridLayout_3.addWidget(self.label_faceattend_icon, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(signup_object)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.gridLayout_3.addWidget(self.label_spacer_bottom, 2, 0, 1, 1)
        self.line_edit_password = QtWidgets.QLineEdit(signup_object)
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_password.setClearButtonEnabled(True)
        self.line_edit_password.setObjectName("line_edit_password")
        self.gridLayout_3.addWidget(self.line_edit_password, 6, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_spacer_top = QtWidgets.QLabel(signup_object)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.gridLayout.addWidget(self.label_spacer_top, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.line_edit_cpassword = QtWidgets.QLineEdit(signup_object)
        self.line_edit_cpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_cpassword.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_cpassword.setClearButtonEnabled(True)
        self.line_edit_cpassword.setObjectName("line_edit_cpassword")
        self.gridLayout_3.addWidget(self.line_edit_cpassword, 7, 0, 1, 1)
        self.line_edit_username = QtWidgets.QLineEdit(signup_object)
        self.line_edit_username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_edit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_username.setClearButtonEnabled(True)
        self.line_edit_username.setObjectName("line_edit_username")
        self.gridLayout_3.addWidget(self.line_edit_username, 5, 0, 1, 1)
        self.line_edit_contact_number = QtWidgets.QLineEdit(signup_object)
        self.line_edit_contact_number.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_contact_number.setClearButtonEnabled(True)
        self.line_edit_contact_number.setObjectName("line_edit_contact_number")
        self.gridLayout_3.addWidget(self.line_edit_contact_number, 4, 0, 1, 1)
        self.line_edit_fullname = QtWidgets.QLineEdit(signup_object)
        self.line_edit_fullname.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_fullname.setClearButtonEnabled(True)
        self.line_edit_fullname.setObjectName("line_edit_fullname")
        self.gridLayout_3.addWidget(self.line_edit_fullname, 3, 0, 1, 1)

        signup_object.setWindowTitle("Signup")
        self.button_signup.setText("Signup")
        self.line_edit_password.setPlaceholderText("Password")
        self.line_edit_cpassword.setPlaceholderText("Confirm Password")
        self.line_edit_username.setPlaceholderText("Username")
        self.line_edit_contact_number.setPlaceholderText("Contact Number")
        self.line_edit_fullname.setPlaceholderText("Full Name")

        QtCore.QMetaObject.connectSlotsByName(signup_object)
        signup_object.setTabOrder(self.line_edit_fullname, self.line_edit_contact_number)
        signup_object.setTabOrder(self.line_edit_contact_number, self.line_edit_username)
        signup_object.setTabOrder(self.line_edit_username, self.line_edit_password)
        signup_object.setTabOrder(self.line_edit_password, self.line_edit_cpassword)
        signup_object.setTabOrder(self.line_edit_cpassword, self.button_signup)
        self.button_signup.clicked.connect(self.signup_details)

    def close_event(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def signup_details(self):
        if self.line_edit_fullname.text() != "" and self.line_edit_password.text() != "" and \
                self.line_edit_cpassword.text() != "" and self.line_edit_username.text() != "" and \
                self.line_edit_contact_number.text() != "":
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                db_cursor = connection.cursor()
                user_id_query = "SELECT userid FROM userdatabase WHERE userid = " + self.line_edit_username.text()
                db_cursor.execute(user_id_query)
                user_id_result = db_cursor.fetchone()
                if user_id_result is None:
                    password = hashlib.sha1(str(self.line_edit_password.text()).encode())
                    cpassword = hashlib.sha1(str(self.line_edit_cpassword.text()).encode())
                    if password.hexdigest() == cpassword.hexdigest():
                        secure_password = password.hexdigest()
                        signup_query = "INSERT INTO userdatabase VALUES( " + self.line_edit_username.text() + \
                                       ", " + secure_password + ", " + self.line_edit_fullname.text() + \
                                       ", " + self.line_edit_contact_number.text() + ")"
                        try:
                            db_cursor.execute(signup_query)
                            connection.commit()
                            signup_object.close()
                            self.signup_object.show()
                            # app = QtWidgets.QApplication(sys.argv)
                            # super.WinLogin = QtWidgets.QMainWindow()
                            # self.ui =  Login()
                            # self.ui.setup_ui(self.WinLogin)
                            # form_signup.close()
                            # self.WinLogin.show()
                        except mysql.connector.Error as error:
                            self.error_report(format(error))
                    else:
                        self.error_report(str("Passwords don't match!"))
                        self.line_edit_password.clear()
                        self.line_edit_cpassword.clear()
                else:
                    self.error_report(str("Username already exists!"))
                    self.line_edit_username.clear()
            except Exception as e:
                self.error_report(format(e))
        else:
            self.error_report(str("Please fill all the details!"))

    def error_report(self, message):
        message_box = QtWidgets.QMessageBox()
        ui = ErrorMessage(message)
        ui.setup_ui(message_box)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    signup_object = QtWidgets.QWidget()
    signup = Signup()
    signup.setup_ui(signup_object)
    signup_object.show()
    sys.exit(app.exec_())
