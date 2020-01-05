'''
QInputDialog输入对话框

1、QInputDialog.getItem      输入列表中的内容
2、QInputDialog.getText      输入字符串
3、QInputDialog.getInt       输入数字


'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QInpuDialogDemon(QWidget):
    def __init__(self):
        super(QInpuDialogDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QInputDialog输入对话框")
        self.resize(500, 500)

        # 初始化按键等对象来获取输入内容
        self.but1 = QPushButton("获取列表中的按钮")
        self.but1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()

        self.but2 = QPushButton("获取字符串的按钮")
        self.but2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()

        self.but3 = QPushButton("获取数字的按钮")
        self.but3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()


        #使用表单布局
        layout = QFormLayout()

        layout.addRow(self.but1, self.lineEdit1)
        layout.addRow(self.but2, self.lineEdit2)
        layout.addRow(self.but3, self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = ('C', 'C++', 'Python', "C#", "Java", "Rubby")
        item, ok = QInputDialog.getItem(self, '请选择编程语言', "语言列表", items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, '文本输入框', "随便输入字符串")
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        int, ok = QInputDialog.getInt(self, '数字输入框', "随便输入数字")
        if ok and int:
            self.lineEdit3.setText(str(int))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./18.jpg'))
    ui = QInpuDialogDemon()
    ui.show()
    sys.exit(app.exec_())
