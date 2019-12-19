import datetime

from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(165, 125, 61, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Form")
        self.label.setText("Form")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    def update_label():
        current_time = str(datetime.datetime.now().time().second)
        ui.label.setText(current_time)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(100)  # every 100 milliseconds (0.01 seconds)

    sys.exit(app.exec_())
