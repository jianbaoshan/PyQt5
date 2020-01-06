'''
QMessage对话框

1、关于对话框
2、错误对话框
3、警告对话框
4、提问对话框
5、消息对话框

有2点差异
1、显示的对话框图标可能不同
2、显示的按钮是不一样的

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QMessageDemon(QWidget):
    def __init__(self):
        super(QMessageDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QMessage消息对话框")
        self.resize(500, 500)

        # 初始化按钮，将按钮与信号槽绑定
        self.but1 = QPushButton()
        self.but1.setText("这是一个关于对话框")
        self.but1.clicked.connect(self.showQmessage)

        self.but2 = QPushButton()
        self.but2.setText("这是一个错误对话框")
        self.but2.clicked.connect(self.showQmessage)

        self.but3 = QPushButton()
        self.but3.setText("这是一个警告对话框")
        self.but3.clicked.connect(self.showQmessage)

        self.but4 = QPushButton()
        self.but4.setText("这是一个提问对话框")
        self.but4.clicked.connect(self.showQmessage)

        self.but5 = QPushButton()
        self.but5.setText("这是一个消息对话框")
        self.but5.clicked.connect(self.showQmessage)

        # 垂直布局
        layout = QVBoxLayout()

        layout.addWidget(self.but1)
        layout.addWidget(self.but2)
        layout.addWidget(self.but3)
        layout.addWidget(self.but4)
        layout.addWidget(self.but5)

        self.setLayout(layout)

    # 信号与槽
    def showQmessage(self):
        text = self.sender().text()
        if text == '这是一个关于对话框':
            QMessageBox.about(self, '关于', "关于对话框1")  # 第二个参数是弹出的对话框的标题，第三个参数是弹出的对话框显示的内容
        elif text == '这是一个错误对话框':
            QMessageBox.critical(self, '错误', "错误对话框2")  # 第二个参数是弹出的对话框的标题，第三个参数是弹出的对话框显示的内容
        elif text == '这是一个警告对话框':
            QMessageBox.warning(self, '警告', "警告对话框3")  # 第二个参数是弹出的对话框的标题，第三个参数是弹出的对话框显示的内容
        elif text == '这是一个提问对话框':
            QMessageBox.question(self, '提问', "提问对话框4")  # 第二个参数是弹出的对话框的标题，第三个参数是弹出的对话框显示的内容
        elif text == '这是一个消息对话框':
            reply = QMessageBox.information(self, '消息', "消息对话框5", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) #最后一个是默认的消息，即按回车默认是选中yes的
            print(reply)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./17.jpg'))
    ui = QMessageDemon()
    ui.show()
    sys.exit(app.exec_())
