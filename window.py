from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np


class Ui_MainWindow(object):
    # Setting up all the elements of the Main Window
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 407)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameImage = QtWidgets.QLabel(self.centralwidget)
        self.frameImage.setGeometry(QtCore.QRect(130, 10, 421, 301))
        self.frameImage.setFrameShape(QtWidgets.QFrame.Box)
        self.frameImage.setText("")
        self.frameImage.setObjectName("frameImage")
        self.buttonSelectImage = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSelectImage.setGeometry(QtCore.QRect(420, 320, 131, 41))
        self.buttonSelectImage.setObjectName("buttonSelectImage")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 111, 351))
        self.groupBox.setObjectName("groupBox")
        self.buttonHue = QtWidgets.QPushButton(self.groupBox)
        self.buttonHue.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.buttonHue.setObjectName("buttonHue")
        self.buttonSaturation = QtWidgets.QPushButton(self.groupBox)
        self.buttonSaturation.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.buttonSaturation.setObjectName("buttonSaturation")
        self.buttonValue = QtWidgets.QPushButton(self.groupBox)
        self.buttonValue.setGeometry(QtCore.QRect(20, 110, 75, 23))
        self.buttonValue.setObjectName("buttonValue")
        self.buttonBinary = QtWidgets.QPushButton(self.groupBox)
        self.buttonBinary.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.buttonBinary.setObjectName("buttonBinary")
        self.buttonGrayscale = QtWidgets.QPushButton(self.groupBox)
        self.buttonGrayscale.setGeometry(QtCore.QRect(20, 170, 75, 23))
        self.buttonGrayscale.setObjectName("buttonGrayscale")
        self.buttonRed = QtWidgets.QPushButton(self.groupBox)
        self.buttonRed.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.buttonRed.setObjectName("buttonRed")
        self.buttonBlue = QtWidgets.QPushButton(self.groupBox)
        self.buttonBlue.setGeometry(QtCore.QRect(20, 200, 75, 23))
        self.buttonBlue.setObjectName("buttonBlue")
        self.buttonGreen = QtWidgets.QPushButton(self.groupBox)
        self.buttonGreen.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.buttonGreen.setObjectName("buttonGreen")
        self.buttonHSV = QtWidgets.QPushButton(self.groupBox)
        self.buttonHSV.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.buttonHSV.setObjectName("buttonHSV")
        self.buttonTranslate = QtWidgets.QPushButton(self.groupBox)
        self.buttonTranslate.setGeometry(QtCore.QRect(20, 290, 75, 23))
        self.buttonTranslate.setObjectName("buttonTranslate")
        self.buttonScale = QtWidgets.QPushButton(self.groupBox)
        self.buttonScale.setGeometry(QtCore.QRect(20, 320, 75, 23))
        self.buttonScale.setObjectName("buttonScale")
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
        self.buttonSelectImage.clicked.connect(self.set_image)
        self.buttonHSV.clicked.connect(self.hsv_image)
        self.buttonHue.clicked.connect(self.hue_image)
        self.buttonSaturation.clicked.connect(self.saturation_image)
        self.buttonValue.clicked.connect(self.value_image)
        self.buttonBinary.clicked.connect(self.binary_image)
        self.buttonGrayscale.clicked.connect(self.grayscale_image)
        self.buttonBlue.clicked.connect(self.blue_image)
        self.buttonGreen.clicked.connect(self.green_image)
        self.buttonRed.clicked.connect(self.red_image)
        self.buttonTranslate.clicked.connect(self.translate_Image)
        self.buttonScale.clicked.connect(self.scale_Image)

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
        self.buttonHSV.setText(_translate("MainWindow", "HSV"))
        self.buttonTranslate.setText(_translate("MainWindow", "Translate"))
        self.buttonScale.setText(_translate("MainWindow", "Scale"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    # Function for selecting an image from file explorer
    def set_image(self):
        self.file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select an image", "",
                                                                 "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.file_name:
            pixmap = QtGui.QPixmap(self.file_name)
            pixmap = pixmap.scaled(self.frameImage.width(), self.frameImage.height(), QtCore.Qt.KeepAspectRatio)
            self.frameImage.setPixmap(pixmap)
            self.frameImage.setAlignment(QtCore.Qt.AlignCenter)

    # Function for converting selected image into binary
    def binary_image(self):
        img = cv2.imread(self.file_name)
        returnValue, blackAndWhite = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow("Black & White", blackAndWhite)

    # Function for converting selected image into binary
    def hsv_image(self):
        img = cv2.imread(self.file_name)
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV Image", img_HSV)

    # Function for converting selected image into hue
    def hue_image(self):
        img = cv2.imread(self.file_name)
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("Hue Image", img_HSV[:, :, 0])

    # Function for converting selected image into saturation
    def saturation_image(self):
        img = cv2.imread(self.file_name)
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("Saturation Image", img_HSV[:, :, 1])

    # Function for converting selected image into value
    def value_image(self):
        img = cv2.imread(self.file_name)
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow("Value Image", img_HSV[:, :, 2])

    # Function for converting selected image into grayscale
    def grayscale_image(self):
        img = cv2.imread(self.file_name)
        grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale Image", grayscale_img)

    # Function for converting selected image into blue
    def blue_image(self):
        img = cv2.imread(self.file_name)
        B, G, R = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype="uint8")
        cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

    # Function for converting selected image into green
    def green_image(self):
        img = cv2.imread(self.file_name)
        B, G, R = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype="uint8")
        cv2.imshow("Blue", cv2.merge([zeros, G, zeros]))

    # Function for converting selected image into red
    def red_image(self):
        img = cv2.imread(self.file_name)
        B, G, R = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype="uint8")
        cv2.imshow("Blue", cv2.merge([zeros, zeros, R]))

    def translate_Image(self):
        img = cv2.imread(self.file_name)

    def scale_Image(self):
        img = cv2.imread(self.file_name)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
