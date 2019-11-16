# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameImage = QtWidgets.QLabel(self.centralwidget)
        self.frameImage.setGeometry(QtCore.QRect(130, 10, 421, 271))
        self.frameImage.setFrameShape(QtWidgets.QFrame.Box)
        self.frameImage.setText("")
        self.frameImage.setObjectName("frameImage")
        self.buttonSelectImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSelectImage.setGeometry(QtCore.QRect(240, 290, 81, 31))
        self.buttonSelectImage.setObjectName("buttonSelectImage")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 111, 271))
        self.groupBox.setObjectName("groupBox")
        self.buttonHue = QtWidgets.QPushButton(self.groupBox)
        self.buttonHue.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.buttonHue.setObjectName("buttonHue")
        self.buttonSaturation = QtWidgets.QPushButton(self.groupBox)
        self.buttonSaturation.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.buttonSaturation.setObjectName("buttonSaturation")
        self.buttonValue = QtWidgets.QPushButton(self.groupBox)
        self.buttonValue.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.buttonValue.setObjectName("buttonValue")
        self.buttonBinary = QtWidgets.QPushButton(self.groupBox)
        self.buttonBinary.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.buttonBinary.setObjectName("buttonBinary")
        self.buttonGrayscale = QtWidgets.QPushButton(self.groupBox)
        self.buttonGrayscale.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.buttonGrayscale.setObjectName("buttonGrayscale")
        self.buttonRed = QtWidgets.QPushButton(self.groupBox)
        self.buttonRed.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.buttonRed.setObjectName("buttonRed")
        self.buttonBlue = QtWidgets.QPushButton(self.groupBox)
        self.buttonBlue.setGeometry(QtCore.QRect(20, 170, 75, 23))
        self.buttonBlue.setObjectName("buttonBlue")
        self.buttonGreen = QtWidgets.QPushButton(self.groupBox)
        self.buttonGreen.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.buttonGreen.setObjectName("buttonGreen")
        self.groupBox.raise_()
        self.frameImage.raise_()
        self.buttonSelectImage.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # For connecting button with a function
        self.buttonSelectImage.clicked.connect(self.setImage)

    # Setting text on widgets
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FaceAttend"))
        self.buttonSelectImage.setText(_translate("MainWindow", "Select Image"))
        self.groupBox.setTitle(_translate("MainWindow", "Presets"))
        self.buttonHue.setText(_translate("MainWindow", "Hue"))
        self.buttonSaturation.setText(_translate("MainWindow", "Saturation"))
        self.buttonValue.setText(_translate("MainWindow", "Value"))
        self.buttonBinary.setText(_translate("MainWindow", "Binary"))
        self.buttonGrayscale.setText(_translate("MainWindow", "Grayscale"))
        self.buttonRed.setText(_translate("MainWindow", "Red"))
        self.buttonBlue.setText(_translate("MainWindow", "Blue"))
        self.buttonGreen.setText(_translate("MainWindow", "Green"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    # Function for selecting an image from file explorer
    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select an image", "",
                                                            "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.frameImage.width(), self.frameImage.height(), QtCore.Qt.KeepAspectRatio)
            self.frameImage.setPixmap(pixmap)
            self.frameImage.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
