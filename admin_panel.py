# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_admin_panel(object):
    def setupUi(self, form_admin_panel):
        form_admin_panel.setObjectName("form_admin_panel")
        form_admin_panel.resize(720, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/FaceAttend2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        form_admin_panel.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(form_admin_panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.button_logout = QtWidgets.QPushButton(form_admin_panel)
        self.button_logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_logout.setIcon(icon1)
        self.button_logout.setIconSize(QtCore.QSize(32, 32))
        self.button_logout.setFlat(True)
        self.button_logout.setObjectName("button_logout")
        self.grid_layout.addWidget(self.button_logout, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.grid_layout)
        self.label_admin_panel = QtWidgets.QLabel(form_admin_panel)
        self.label_admin_panel.setObjectName("label_admin_panel")
        self.verticalLayout.addWidget(self.label_admin_panel)
        self.label_admin_icon = QtWidgets.QLabel(form_admin_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_admin_icon.sizePolicy().hasHeightForWidth())
        self.label_admin_icon.setSizePolicy(sizePolicy)
        self.label_admin_icon.setMinimumSize(QtCore.QSize(1, 1))
        self.label_admin_icon.setBaseSize(QtCore.QSize(0, 0))
        self.label_admin_icon.setText("")
        self.label_admin_icon.setPixmap(QtGui.QPixmap("assets/user.png"))
        self.label_admin_icon.setObjectName("label_admin_icon")
        self.verticalLayout.addWidget(self.label_admin_icon, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_designation = QtWidgets.QLabel(form_admin_panel)
        self.label_designation.setObjectName("label_designation")
        self.verticalLayout.addWidget(self.label_designation, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_spacer_middle = QtWidgets.QLabel(form_admin_panel)
        self.label_spacer_middle.setText("")
        self.label_spacer_middle.setObjectName("label_spacer_middle")
        self.verticalLayout.addWidget(self.label_spacer_middle)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.button_subject_allotment = QtWidgets.QPushButton(form_admin_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_subject_allotment.sizePolicy().hasHeightForWidth())
        self.button_subject_allotment.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/teachers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_subject_allotment.setIcon(icon2)
        self.button_subject_allotment.setIconSize(QtCore.QSize(64, 64))
        self.button_subject_allotment.setObjectName("button_subject_allotment")
        self.horizontal_layout.addWidget(self.button_subject_allotment)
        self.divider_line = QtWidgets.QFrame(form_admin_panel)
        self.divider_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.divider_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_line.setObjectName("divider_line")
        self.horizontal_layout.addWidget(self.divider_line)
        self.button_performance_analysis = QtWidgets.QPushButton(form_admin_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_performance_analysis.sizePolicy().hasHeightForWidth())
        self.button_performance_analysis.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/line_chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_performance_analysis.setIcon(icon3)
        self.button_performance_analysis.setIconSize(QtCore.QSize(64, 64))
        self.button_performance_analysis.setFlat(False)
        self.button_performance_analysis.setObjectName("button_performance_analysis")
        self.horizontal_layout.addWidget(self.button_performance_analysis)
        self.verticalLayout.addLayout(self.horizontal_layout)
        self.label_spacer_bottom = QtWidgets.QLabel(form_admin_panel)
        self.label_spacer_bottom.setText("")
        self.label_spacer_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.label_spacer_bottom.setObjectName("label_spacer_bottom")
        self.verticalLayout.addWidget(self.label_spacer_bottom)

        self.retranslateUi(form_admin_panel)
        QtCore.QMetaObject.connectSlotsByName(form_admin_panel)
        form_admin_panel.setTabOrder(self.button_subject_allotment, self.button_performance_analysis)
        form_admin_panel.setTabOrder(self.button_performance_analysis, self.button_logout)

    def retranslateUi(self, form_admin_panel):
        _translate = QtCore.QCoreApplication.translate
        form_admin_panel.setWindowTitle(_translate("form_admin_panel", "Admin Panel"))
        self.button_logout.setToolTip(_translate("form_admin_panel", "Logout"))
        self.label_admin_panel.setText(_translate("form_admin_panel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Google Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#888a85;\">ADMIN PANEL</span></p></body></html>"))
        self.label_designation.setText(_translate("form_admin_panel", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Head of Department</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Department of Computer Science</span></p><p align=\"center\"><span style=\" font-size:12pt;\">Mohanlal Sukhadia University</span></p></body></html>"))
        self.button_subject_allotment.setToolTip(_translate("form_admin_panel", "Subject Allotment"))
        self.button_subject_allotment.setText(_translate("form_admin_panel", "Subject Allotment"))
        self.button_performance_analysis.setToolTip(_translate("form_admin_panel", "Performance Analysis"))
        self.button_performance_analysis.setText(_translate("form_admin_panel", "Performance Analysis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_admin_panel = QtWidgets.QWidget()
    ui = Ui_form_admin_panel()
    ui.setupUi(form_admin_panel)
    form_admin_panel.show()
    sys.exit(app.exec_())
