from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMessageBox


class Ui_Info:

    def __init__(self,messg):
        self.messg = messg

    def setupUi(self, Dialog):
        self.Info()

    def Info(self):

        msg = QMessageBox()
        msg.resize(130,550)
        msg.setFixedSize(130,550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)

        msg.setText("Information")
        msg.setInformativeText(self.messg)
        msg.setWindowTitle("FaceAttend - Information")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        print("value of pressed message box button:", retval)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    messageBox = QtWidgets.QMessageBox()
    ui = Ui_Info()
    ui.setupUi(messageBox)
    sys.exit(app.exec_())
