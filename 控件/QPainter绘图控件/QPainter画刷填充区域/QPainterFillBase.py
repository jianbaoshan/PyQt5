"""
绘图API：
使用画刷填充区域
"""

import sys, math
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QIcon, QPen, QPolygon, QImage, QBrush
from PyQt5.QtCore import Qt, QRect, QPoint


class FillRectDemon(QWidget):
    def __init__(self):
        super(FillRectDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("使用画刷填充区域")
        self.resize(500, 500)

    def paintEvent(self, QPaintEvent):
        painter = QPainter()

        painter.begin(self)

        # 初始化画刷
        brush0 = QBrush(Qt.SolidPattern)
        brush1 = QBrush(Qt.Dense1Pattern)
        brush2 = QBrush(Qt.Dense2Pattern)
        brush3 = QBrush(Qt.Dense3Pattern)
        brush4 = QBrush(Qt.Dense4Pattern)
        brush5 = QBrush(Qt.Dense5Pattern)
        brush6 = QBrush(Qt.Dense6Pattern)
        brush7 = QBrush(Qt.Dense7Pattern)

        # 选择画刷，设置填充区域
        painter.setBrush(brush0)
        painter.drawRect(0, 0, 100, 100)

        painter.setBrush(brush1)
        painter.drawRect(110, 0, 100, 100)

        painter.setBrush(brush2)
        painter.drawRect(220, 0, 100, 100)

        painter.setBrush(brush3)
        painter.drawRect(330, 0, 100, 100)

        painter.setBrush(brush4)
        painter.drawRect(0, 110, 100, 100)

        painter.setBrush(brush5)
        painter.drawRect(110, 110, 100, 100)

        painter.setBrush(brush6)
        painter.drawRect(220, 110, 100, 100)

        painter.setBrush(brush7)
        painter.drawRect(330, 110, 100, 100)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./26.jpg'))
    ui = FillRectDemon()
    ui.show()
    sys.exit(app.exec_())
