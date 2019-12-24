from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.Qt import Qt
from PyQt5.QtChart import QChart, QBarCategoryAxis, QStackedBarSeries, QBarSet, QChartView
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets


class BarChart(object):

    def __init__(self, percentage, subject):
        self.percentage = []
        self.subjects = []
        self.percentage.extend(percentage)
        self.subjects.extend(subject)
    #     super().__init__()

    def setup_ui(self, bar_chart_object):
        bar_chart_object.resize(800, 600)
        self.calculate()
        chill = QBarSet("Clear")
        worry = QBarSet("Short")
        trouble = QBarSet("Very Short")

        worry << self.worry[0] << self.worry[1] << self.worry[2] << self.worry[3] << self.worry[4] << self.worry[5] << \
            self.worry[6]
        trouble << self.trouble[0] << self.trouble[1] << self.trouble[2] << self.trouble[3] << self.trouble[4] << \
            self.trouble[5] << self.trouble[6]
        # chill <<40 << -50 << -45.3 << -37.0 << -25.6 << -8.0 << -6.0
        chill << self.chill[0] << self.chill[1] << self.chill[2] << self.chill[3] << self.chill[4] << self.chill[5] << \
            self.chill[6]

        series = QStackedBarSeries()
        series.append(worry)
        series.append(chill)
        series.append(trouble)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Attendance Graph")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = [self.subjects[0], self.subjects[1], self.subjects[2], self.subjects[3], self.subjects[4],
                      self.subjects[5], self.subjects[6]]

        axis = QBarCategoryAxis()
        axis.append(categories)
        axis.setTitleText("Month")
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.axisY(series).setRange(0, 100)
        chart.axisY(series).setTitleText("Percentage (%)")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QChartView(chart)
        bar_chart_object.setCentralWidget(chart_view)

    def calculate(self):
        self.chill = []
        self.worry = []
        self.trouble = []

        for i in range(7):
            if (self.percentage[i] > 75):
                self.chill.append(self.percentage[i])
                self.worry.append(0)
                self.trouble.append(0)
            elif (self.percentage[i] < 40):
                self.chill.append(0)
                self.worry.append(self.percentage[i])
                self.trouble.append(0)
            elif (self.percentage[i] > 40 or self.percentage[i] < 75):
                self.chill.append(0)
                self.worry.append(0)
                self.trouble.append(self.percentage[i])
    # def CharTShow(self):
    #
    #     print("enter to the form")
    #     print(len(self.percentage))
    #     for i in range(len(self.percentage)):
    #         print(self.percentage[i])
    #
    # low = QBarSet("Short") high = QBarSet("Clear") low << 40 << -50 << -45.3 << -37.0 << -25.6 << -8.0 << -6.0 high
    # << self.percentage[0] << self.percentage[1] << self.percentage[2] << self.percentage[3] << self.percentage[4]
    # << self.percentage[5] << self.percentage[6] self.seseries.append(low) self.series.append(high)
    #
    #     self.chart.legend()
    #
    #     chartView = QChartView(self.chart)
    #     chartView.setRenderHint(QPainter.Antialiasing)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    bar_chart = QtWidgets.QMainWindow()
    ui = BarChart()
    ui.setup_ui(bar_chart)
    bar_chart.show()
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
