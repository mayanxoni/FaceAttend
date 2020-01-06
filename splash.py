import os
import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from login import Ui_form_login

FROM_SPLASH, _ = loadUiType(os.path.join(os.path.dirname(__file__), "splash.ui"))

class ThreadProgress(QThread):
    thread_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def run(self):
        i = 0
        while i < 101:
            time.sleep(0.1)
            self.thread_signal.emit(i)
            i += 10

class SplashScreen(QMainWindow, FROM_SPLASH):
    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        progress = ThreadProgress(self)
        progress.thread_signal.connect(self.progress)
        progress.start()

    @pyqtSlot(int)
    def progress(self, i):
        self.progress_bar.setValue(i)
        if i == 100:
            self.hide()
            form_login = QtWidgets.QMainWindow()
            login_object = Ui_form_login()
            login_object.setupUi(form_login)
            form_login.show()

def main():
    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except Exception as why:
        print(why)