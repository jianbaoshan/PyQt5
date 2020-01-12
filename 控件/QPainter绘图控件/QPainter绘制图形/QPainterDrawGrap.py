"""
绘图API：
使用像素点绘制不同的图形
弧
扇形
圆
矩形
图片
"""

import sys, math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QIcon, QPen, QPolygon, QImage
from PyQt5.QtCore import Qt, QRect,QPoint


class DrawGraph(QWidget):
    def __init__(self):
        super(DrawGraph, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("绘制不同的直线")
        self.resize(500, 500)

    def paintEvent(self, QPaintEvent):
        painter = QPainter()

        painter.begin(self)

        # 绘制弧
        painter.setPen(Qt.red)
        rect = QRect(0, 0, 100, 100)                # 初始化一块矩形区域，前面两个是矩形所在的左上角坐标点，后面两个是矩形的长和宽
        # 绘图使用的单位是alen：1个alen等于1/16度
        painter.drawArc(rect, 0, 66 * 16)           # rect是弧形所在的区域，0是弧形的起始角度，60*16是弧形的终止角度

        # 使用绘制弧形函数来绘制圆
        painter.setPen(Qt.blue)
        painter.drawArc(200,0, 100,100, 0, 360 * 16)  # rect是弧形所在的区域，0是弧形的起始角度，60*16是弧形的终止角度

        # 绘制带弦的弧
        painter.setPen(Qt.yellow)
        painter.drawChord(300, 0, 100, 100, 0, 145 * 16)

        # 绘制扇形
        painter.setPen(Qt.cyan)
        painter.drawPie(0, 100, 100, 100, 0, 200 * 16)

        # 绘制椭圆
        painter.setPen(Qt.red)
        painter.drawEllipse(100, 100, 100, 150)

        # 绘制多边形：几变形就要指定几个点
        p1 = QPoint(10, 200)        #点的坐标
        p2 = QPoint(30, 200)        #点的坐标
        p3 = QPoint(200, 300)        #点的坐标
        p4 = QPoint(300, 300)       #点的坐标
        p5 = QPoint(100, 400)        #点的坐标

        po = QPolygon([p1, p2, p3, p4, p5])
        painter.drawPolygon(po)

        # 绘制图像
        image = QImage("./24.jpg")        # 加载图像
        rect1 = QRect(300, 300, image.width()/3, image.height()/3)
        painter.drawImage(rect1, image)


        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./25.jpg'))
    ui = DrawGraph()
    ui.show()
    sys.exit(app.exec_())
