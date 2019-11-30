from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_camera_feed(object):
    def setupUi(self, form_camera_feed):
        form_camera_feed.setObjectName("form_camera_feed")
        form_camera_feed.resize(720, 480)
        form_camera_feed.setFixedSize(720, 480)
        self.horizontalLayout = QtWidgets.QHBoxLayout(form_camera_feed)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_vertical = QtWidgets.QVBoxLayout()
        self.layout_vertical.setObjectName("layout_vertical")
        self.label_image = QtWidgets.QLabel(form_camera_feed)
        self.label_image.setObjectName("label_image")
        self.layout_vertical.addWidget(self.label_image, 0, QtCore.Qt.AlignHCenter)
        self.button_capture = QtWidgets.QPushButton(form_camera_feed)
        self.button_capture.setObjectName("button_capture")
        self.layout_vertical.addWidget(self.button_capture)
        self.horizontalLayout.addLayout(self.layout_vertical)

        self.retranslateUi(form_camera_feed)
        QtCore.QMetaObject.connectSlotsByName(form_camera_feed)

    def retranslateUi(self, form_camera_feed):
        _translate = QtCore.QCoreApplication.translate
        form_camera_feed.setWindowTitle(_translate("form_camera_feed", "Camera Feed"))
        self.label_image.setText(_translate("form_camera_feed", "To start live camera feed, click \"Capture\" button."))
        self.button_capture.setText(_translate("form_camera_feed", "Capture"))
