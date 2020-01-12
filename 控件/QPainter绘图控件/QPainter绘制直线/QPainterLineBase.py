"""
绘图API：
使用像素点绘制不同的直线
"""

import sys, math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QIcon, QPen
from PyQt5.QtCore import Qt


class DrawLines(QWidget):
    def __init__(self):
        super(DrawLines, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("绘制不同的直线")
        self.resize(500, 500)

    def paintEvent(self, QPaintEvent):
        painter = QPainter()

        painter.begin(self)

        # 初始化画笔
        pen1 = QPen(Qt.red, 5, Qt.SolidLine)            # 红色, 粗细=5，直线
        pen2 = QPen(Qt.blue, 6, Qt.DashLine)            # 蓝色, 粗细=6，虚线
        pen3 = QPen(Qt.yellow, 7, Qt.DashDotDotLine)    # 黄色, 粗细=7，点点虚线
        pen4 = QPen(Qt.black, 8, Qt.DashDotLine)        # 黑色, 粗细=8，点虚线
        pen6 = QPen(Qt.cyan, 10, Qt.DotLine)            # 青色, 粗细=9，虚线

        painter.setPen(pen1)                            # 设置画线使用的画笔
        painter.drawLine(20, 40, 400, 40)               # 前两个参数是直线在窗口的起点坐标，后两个参数是直线在窗口的终点坐标

        painter.setPen(pen2)                            # 设置画线使用的画笔
        painter.drawLine(20, 60, 400, 60)               # 前两个参数是直线在窗口的起点坐标，后两个参数是直线在窗口的终点坐标

        painter.setPen(pen3)                            # 设置画线使用的画笔
        painter.drawLine(20, 80, 400, 80)               # 前两个参数是直线在窗口的起点坐标，后两个参数是直线在窗口的终点坐标

        painter.setPen(pen4)                            # 设置画线使用的画笔
        painter.drawLine(20, 100, 400, 100)             # 前两个参数是直线在窗口的起点坐标，后两个参数是直线在窗口的终点坐标

        painter.setPen(pen6)                            # 设置画线使用的画笔
        painter.drawLine(20, 140, 400, 140)             # 前两个参数是直线在窗口的起点坐标，后两个参数是直线在窗口的终点坐标

        # 可以通过setStyle来修改画笔的属性
        pen6.setStyle(Qt.CustomDashLine)                # 修改画笔的属性
        pen6.setDashPattern([1, 4, 10, 3])              # 自定义的线：线和空白按照数组给定的数据来走的  只能有四位
        painter.setPen(pen6)                            # 设置画线使用的画笔
        painter.drawLine(20, 120, 400, 120)             # 前两个参数是直线在窗口的起点坐标，后两个参数是直线在窗口的终点坐标

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./23.jpg'))
    ui = DrawLines()
    ui.show()
    sys.exit(app.exec_())
