import hashlib

import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


from ErrorMessg import Ui_Dialog


class Ui_form_signup(object):
    def __init__(self,form,signup):
        self.sigup = signup
        self.form = form

    def setupUi(self, form_signup):
        form_signup.setObjectName("form_signup")
        form_signup.resize(380, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_signup.setWindowIcon(icon)
        self.gridLayout_3 = QtWidgets.QGridLayout(form_signup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_signup = QtWidgets.QPushButton(form_signup)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_signup.setIcon(icon1)
        self.button_signup.setObjectName("button_signup")
        self.verticalLayout_2.addWidget(self.button_signup)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 9, 0, 1, 1)
        self.label_faceattend_icon = QtWidgets.QLabel(form_signup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_faceattend_icon.sizePolicy().hasHeightForWidth())
        self.label_faceattend_icon.setSizePolicy(sizePolicy)
        self.label_faceattend_icon.setMinimumSize(QtCore.QSize(1, 1))
        self.label_faceattend_icon.setBaseSize(QtCore.QSize(0, 0))
        self.label_faceattend_icon.setText("")
        self.label_faceattend_icon.setPixmap(QtGui.QPixmap("assets/FaceAttend2.png"))
        self.label_faceattend_icon.setObjectName("label_faceattend_icon")
        self.gridLayout_3.addWidget(self.label_faceattend_icon, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_spacer_bottom = QtWidgets.QLabel(form_signup)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.gridLayout_3.addWidget(self.label_spacer_bottom, 2, 0, 1, 1)
        self.line_edit_password = QtWidgets.QLineEdit(form_signup)
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_password.setClearButtonEnabled(True)
        self.line_edit_password.setObjectName("line_edit_password")
        self.gridLayout_3.addWidget(self.line_edit_password, 6, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_spacer_top = QtWidgets.QLabel(form_signup)
        self.label_spacer_top.setText("")
        self.label_spacer_top.setObjectName("label_spacer_top")
        self.gridLayout.addWidget(self.label_spacer_top, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.line_edit_cpassword = QtWidgets.QLineEdit(form_signup)
        self.line_edit_cpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_edit_cpassword.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_cpassword.setClearButtonEnabled(True)
        self.line_edit_cpassword.setObjectName("line_edit_cpassword")
        self.gridLayout_3.addWidget(self.line_edit_cpassword, 7, 0, 1, 1)
        self.line_edit_username = QtWidgets.QLineEdit(form_signup)
        self.line_edit_username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line_edit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_username.setClearButtonEnabled(True)
        self.line_edit_username.setObjectName("line_edit_username")
        self.gridLayout_3.addWidget(self.line_edit_username, 5, 0, 1, 1)
        self.line_edit_contact_number = QtWidgets.QLineEdit(form_signup)
        self.line_edit_contact_number.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_contact_number.setClearButtonEnabled(True)
        self.line_edit_contact_number.setObjectName("line_edit_contact_number")
        self.gridLayout_3.addWidget(self.line_edit_contact_number, 4, 0, 1, 1)
        self.line_edit_fullname = QtWidgets.QLineEdit(form_signup)
        self.line_edit_fullname.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit_fullname.setClearButtonEnabled(True)
        self.line_edit_fullname.setObjectName("line_edit_fullname")
        self.gridLayout_3.addWidget(self.line_edit_fullname, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(form_signup)
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1, QtCore.Qt.AlignLeft)




        self.retranslateUi(form_signup)
        QtCore.QMetaObject.connectSlotsByName(form_signup)
        form_signup.setTabOrder(self.line_edit_fullname, self.line_edit_contact_number)
        form_signup.setTabOrder(self.line_edit_contact_number, self.line_edit_username)
        form_signup.setTabOrder(self.line_edit_username, self.line_edit_password)
        form_signup.setTabOrder(self.line_edit_password, self.line_edit_cpassword)
        form_signup.setTabOrder(self.line_edit_cpassword, self.button_signup)
        self.button_signup.clicked.connect(self.SignUpDetails)
        self.pushButton.clicked.connect(self.BackButton)


    def retranslateUi(self, form_signup):
        _translate = QtCore.QCoreApplication.translate
        form_signup.setWindowTitle(_translate("form_signup", "Signup"))
        self.button_signup.setText(_translate("form_signup", "Signup"))
        self.line_edit_password.setPlaceholderText(_translate("form_signup", "Password"))
        self.line_edit_cpassword.setPlaceholderText(_translate("form_signup", "Confirm Password"))
        self.line_edit_username.setPlaceholderText(_translate("form_signup", "Username"))
        self.line_edit_contact_number.setPlaceholderText(_translate("form_signup", "Contact Number"))
        self.line_edit_fullname.setPlaceholderText(_translate("form_signup", "Full Name"))



    def SignUpDetails(self):

        if self.line_edit_fullname.text() != "" and self.line_edit_password.text() != "" and self.line_edit_cpassword.text() != "" and self.line_edit_username.text() != "" and self.line_edit_contact_number.text() != "":
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="collegeattend",
                    passwd=""
                )
                mycursor = mydb.cursor()
                mycursor.execute("SELECT userid FROM userdatabase where userid = %s ", (self.line_edit_username.text(),))
                myresult = mycursor.fetchone()
                if myresult is None:
                    pas = hashlib.sha1(str(self.line_edit_password.text()).encode())
                    cpas = hashlib.sha1(str(self.line_edit_cpassword.text()).encode())
                    if pas.hexdigest() == cpas.hexdigest():
                        spass = pas.hexdigest()
                        try:
                            mycursor.execute("insert into userdatabase values(%s ,%s ,%s ,%s)",
                                             (self.line_edit_username.text(), spass, self.line_edit_fullname.text(), self.line_edit_contact_number.text()))
                            mydb.commit()
                            self.sigup.close()
                            self.form.show()
                        except mysql.connector.Error as error:
                            self.ErrorReport(format(error))
                    else:
                        self.ErrorReport(str("password miss match"))
                        self.line_edit_password.clear()
                        self.line_edit_cpassword.clear()
                else:
                    self.ErrorReport(str("Username already exists"))
                    self.line_edit_username.clear()
            except Exception as e:
                self.ErrorReport(format(e))
        else:
            self.ErrorReport(str("please enter each detail"))

    def ErrorReport(self, message):
         messageBox = QtWidgets.QMessageBox()
         ui = Ui_Dialog(message)
         ui.setupUi(messageBox)

    def BackButton(self):
        self.sigup.close()
        self.form.show()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_signup = QtWidgets.QWidget()
    ui = Ui_form_signup()
    ui.setupUi(form_signup)
    form_signup.show()
    sys.exit(app.exec_())