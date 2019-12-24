# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'errordilog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMessageBox


class Ui_Dialog:

    def __init__(self,messg):
        self.messg = messg

    def setupUi(self, Dialog):
        self.get_error_code()

    def get_error_code(self):

        msg = QMessageBox()
        msg.resize(130,550)
        msg.setFixedSize(130,550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Critical)

        msg.setText("ERROR!")
        msg.setInformativeText(self.messg)
        msg.setWindowTitle("FaceAttend - Error")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        print("value of pressed message box button:", retval)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    messageBox = QtWidgets.QMessageBox()
    ui = Ui_Dialog()
    ui.setupUi(messageBox)
    sys.exit(app.exec_())
