from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMessageBox


class ErrorMessage:

    def __init__(self, message):
        self.message = message

    def setup_ui(self, error_message_object):
        self.get_error_code()

    def get_error_code(self):
        message_box = QMessageBox()
        message_box.resize(130, 550)
        message_box.setFixedSize(130, 550)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttendLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        message_box.setWindowIcon(icon)
        message_box.setIcon(QMessageBox.Critical)

        message_box.setText("ERROR!")
        message_box.setInformativeText(self.message)
        message_box.setWindowTitle("FaceAttend - Error")
        message_box.setStandardButtons(QMessageBox.Ok)
        return_value = message_box.exec_()
        print("Value of pressed message box button: ", return_value)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    error_message_object = QtWidgets.QMessageBox()
    error_message = ErrorMessage()
    error_message.setup_ui(error_message_object)
    sys.exit(app.exec_())
