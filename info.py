from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMessageBox


class Info:

    def __init__(self, message):
        self.message = message

    def setup_ui(self, info_object):
        self.information()

    def information(self):
        message_box = QMessageBox()
        message_box.resize(130, 550)
        message_box.setFixedSize(130, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        message_box.setWindowIcon(icon)
        message_box.setIcon(QMessageBox.Information)

        message_box.setText("Information")
        message_box.setInformativeText(self.message)
        message_box.setWindowTitle("FaceAttend - Information")
        message_box.setStandardButtons(QMessageBox.Ok)
        retval = message_box.exec_()
        print("Value of pressed message box button:", retval)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    info_object = QtWidgets.QMessageBox()
    info = Info()
    info.setup_ui(info_object)
    sys.exit(app.exec_())
