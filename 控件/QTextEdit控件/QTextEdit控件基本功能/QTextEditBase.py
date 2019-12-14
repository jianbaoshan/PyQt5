"""
QTextEdit控件的基本功能
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys

class QTextEditBaseFunction(QWidget):
    def __init__(self):
        super(QTextEditBaseFunction, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle('QTextEdit控件')        #窗口标题
        self.resize(300,300)                        #窗口大小

        #初始化文本框
        self.text = QTextEdit()
        self.ButtonShowText = QPushButton('显示文本')
        self.ButtonGetText = QPushButton('获取文本')
        self.ButtonShowHtml = QPushButton('显示HTML')
        self.ButtonGetHtml = QPushButton('获取HTML')

        #将信号与槽绑定起来
        self.ButtonShowText.clicked.connect(self.ClickShowText)
        self.ButtonGetText.clicked.connect(self.ClickGetText)
        self.ButtonShowHtml.clicked.connect(self.ClickShowHTML)
        self.ButtonGetHtml.clicked.connect(self.ClickGetHTML)

        #垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.ButtonShowText)
        layout.addWidget(self.ButtonGetText)
        layout.addWidget(self.ButtonShowHtml)
        layout.addWidget(self.ButtonGetHtml)

        self.setLayout(layout)

    #信号槽
    def ClickShowText(self):
        self.text.setPlainText('Hello World! 世界你好吗？')       #在文本框中显示普通文本

    # 信号槽
    def ClickGetText(self):
        print(self.text.toPlainText())

    # 信号槽
    def ClickShowHTML(self):
        self.text.setHtml('<font color="red" size="50"> 哈哈！又是美好的一天</font>')  # 在文本框中显示普通文本

    # 信号槽
    def ClickGetHTML(self):
        print(self.text.toHtml())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./8.jpg'))
    ui = QTextEditBaseFunction()
    ui.show()
    sys.exit(app.exec_())