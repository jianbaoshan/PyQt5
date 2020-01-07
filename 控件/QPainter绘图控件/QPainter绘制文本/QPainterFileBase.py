"""
绘图API：绘制文本

1、文本
2、各种图形(直线、点、椭圆、弧、扇形、多边形等)
3、图像

QPainter

painter = QPainter()

初始化一个画板
painter.begin()

在这里进行一些绘制
...

结束绘制
painter.end()

上面的四个绘制步骤必须在painEvent事件方法中执行的

"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont,QIcon
from PyQt5.QtCore import Qt


class DrawFile(QWidget):
    def __init__(self):
        super(DrawFile, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("绘制文本")
        self.resize(500, 500)
        self.text = "正在学习PyQt5中"

    def paintEvent(self, event):
        painter = QPainter(self)

        # 开始绘制
        painter.begin(self)

        painter.setPen(QColor(150,43,5))            # 设置画笔的颜色，即绘制出来的图像的颜色
        painter.setFont(QFont('SimSun', 30))        # 设置字体和大小

        # rect=绘制的区域、AlignCenter=居中绘制、self.text=绘制的文本内容
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)

        # 结束绘制
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./21.jpg'))
    ui = DrawFile()
    ui.show()
    sys.exit(app.exec_())
