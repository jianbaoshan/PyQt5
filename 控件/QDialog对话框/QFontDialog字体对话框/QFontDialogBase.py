'''
QFontDialgo字体对话框
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QFontDialogDemon(QWidget):
    def __init__(self):
        super(QFontDialogDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QFontDialog字体对话框")
        self.resize(500, 500)

        # 初始化字体选择按钮
        self.but1 = QPushButton('设置字体按钮')
        self.but1.clicked.connect(self.getCharFont)

        # 初始化测试字体
        self.fontLabel = QLabel("Hello World! 你好 世界！")

        # 使用垂直布局
        layout = QVBoxLayout()

        layout.addWidget(self.but1)
        layout.addWidget(self.fontLabel)

        self.setLayout(layout)

    # 信号与槽
    def getCharFont(self):
        font, ok = QFontDialog.getFont()  # 选择字体
        if ok:
            self.fontLabel.setFont(font)  # 设置字体为选择的字体


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./18.jpg'))
    ui = QFontDialogDemon()
    ui.show()
    sys.exit(app.exec_())
