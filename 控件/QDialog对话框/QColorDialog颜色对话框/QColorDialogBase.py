'''
QColorDialgo颜色对话框
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QColorDialogDemon(QWidget):
    def __init__(self):
        super(QColorDialogDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QColorDialog颜色对话框")
        self.resize(500, 500)

        # 初始化字体选择按钮
        self.but1 = QPushButton('设置颜色按钮')
        self.but1.clicked.connect(self.getColorFont)

        self.but2 = QPushButton('设置背景颜色按钮')
        self.but2.clicked.connect(self.getBackGroundFont)

        # 初始化测试字体
        self.colorLabel = QLabel("Hello World! 你好 世界！")

        # 使用垂直布局
        layout = QVBoxLayout()

        layout.addWidget(self.but1)
        layout.addWidget(self.but2)
        layout.addWidget(self.colorLabel)

        self.setLayout(layout)

    # 信号与槽
    def getColorFont(self):
        color = QColorDialog.getColor()                 # 选择颜色
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(p)                   # 设置字体为选择的字体

    def getBackGroundFont(self):
        color = QColorDialog.getColor()                 # 选择颜色
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.colorLabel.setAutoFillBackground(True)     # 使能背景色设置
        self.colorLabel.setPalette(p)                   # 设置字体为选择的字体


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./19.jpg'))
    ui = QColorDialogDemon()
    ui.show()
    sys.exit(app.exec_())
