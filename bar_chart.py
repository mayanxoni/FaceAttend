# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chart.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import (QApplication, QMainWindow)
from  PyQt5.Qt import  Qt
from PyQt5.QtChart import QChart, QBarCategoryAxis, QStackedBarSeries, QBarSet, QChartView
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_Chart(object):

    def __init__(self,per,sub):
        self.percentage = []
        self.Subjects = []
        self.percentage.extend(per)
        self.Subjects.extend(sub)
    #     super().__init__()

    def setupUi(self, Form):
        Form.resize(800, 600)


        # low = QBarSet("Short")
        high = QBarSet("Clear")

        # low << 40.0 << 75.0 << 45.3 << 37.0 << 25.6 << 8.0 << 6.0
        # high << value[0] << value[1] << value[2] << value[3] << value[4] << value[5] << value[6]
        # high <<40 << -50 << -45.3 << -37.0 << -25.6 << -8.0 << -6.0
        high << self.percentage[0] << self.percentage[1] << self.percentage[2] << self.percentage[3] << self.percentage[4] << self.percentage[5] << self.percentage[6]

        series = QStackedBarSeries()
        # series.append(low)
        series.append(high)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Attendance Graph")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = [self.Subjects[0],self.Subjects[1],self.Subjects[2],self.Subjects[3],self.Subjects[4],self.Subjects[5],self.Subjects[6]]

        axis = QBarCategoryAxis()
        axis.append(categories)
        axis.setTitleText("Month")
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.axisY(series).setRange(0, 100)
        chart.axisY(series).setTitleText("Percentage (%)")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        Form.setCentralWidget(chartView)





    # def CharTShow(self):
    #
    #     print("enter to the form")
    #     print(len(self.percentage))
    #     for i in range(len(self.percentage)):
    #         print(self.percentage[i])
    #
    #     low = QBarSet("Short")
    #     high = QBarSet("Clear")
    #     low << 40 << -50 << -45.3 << -37.0 << -25.6 << -8.0 << -6.0
    #     high << self.percentage[0] << self.percentage[1] << self.percentage[2] << self.percentage[3] << self.percentage[4] << self.percentage[5] << self.percentage[6]
    #     self.seseries.append(low)
    #     self.series.append(high)
    #
    #
    #
    #     self.chart.legend()
    #
    #     chartView = QChartView(self.chart)
    #     chartView.setRenderHint(QPainter.Antialiasing)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Chart()
    ui.setupUi(Form)
    Form.show()
    sys._excepthook = sys.excepthook
    def my_exception_hook(exctype, value, traceback):
        # Print the error and traceback
        print(exctype, value, traceback)
        # Call the normal Exception hook after
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)
    # Set the exception hook to our wrapping function
    sys.excepthook = my_exception_hook
    sys.exit(app.exec_())
