"""
绘图API：
使用像素点绘制正弦曲线
"""

import sys,math
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont,QIcon
from PyQt5.QtCore import Qt


class DrawSinDemon(QWidget):
    def __init__(self):
        super(DrawSinDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("绘制正弦曲线")
        self.resize(500, 500)

    def paintEvent(self, QPaintEvent):
        painter = QPainter()

        painter.begin(self)

        painter.setPen(Qt.red)                  # 设置绘笔的颜色
        size = self.size()                      # 获得窗口的尺寸

        for i in range(1000):
            my = 50                             # 正弦曲线的高度
            mx = 150                            # 正弦曲线的长度
            sizex = 2.0                         # 正弦曲线在窗口的x轴的位置：2代表在窗口的正中间
            sizey = 2.0                         # 正弦曲线在窗口的y轴的位置：2代表在窗口的正中间
            # 这里加上串口一半的宽度是为了将正弦曲线显示在串口的正中间
            x = mx * (-1 + 2 * i/1000) + size.width()/sizex
            y = -my * math.sin((x - size.width() / sizex) * math.pi / my) + size.height() / sizey
            painter.drawPoint(x, y)

        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./22.jpg'))
    ui = DrawSinDemon()
    ui.show()
    sys.exit(app.exec_())
