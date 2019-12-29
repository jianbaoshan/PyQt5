"""
下拉列表控件(QComboBox)
"""


import  sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QComboBoxDemon(QWidget):
    def __init__(self):
        super(QComboBoxDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QComboBox下拉列表控件")
        self.resize(300,300)

        #使用垂直布局
        layout = QVBoxLayout()

        #初始化Label，
        self.label = QLabel("请选择编程语言")

        #初始化下拉列表控件
        self.cb = QComboBox()
        self.cb.addItem("C")                                            #向下拉列表控件中添加一个元素
        self.cb.addItem("Python")                                       #向下拉列表控件中添加一个元素
        self.cb.addItems(['C++', 'C#', "Java", "VB", "Go"])             #向下拉列表控件中添加多个元素

        #绑定信号与槽,这个信号自动传入两个参数的
        self.cb.currentIndexChanged.connect(self.selectChange)


        #将控件加入到垂直布局中
        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectChange(self, i):
        self.label.setText(self.cb.currentText())                       #显示当前所选择元素的文本
        self.cb.adjustSize()                                            #调整大小

        #打印所以的下拉列表元素
        for j in range(self.cb.count()):
            print("Index" + str(j) + "=" + self.cb.itemText(j))

        #打印当前所选择的下拉元素
        print("current index is ", i, 'Current Text is', self.cb.currentText())






if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./13.jpg'))
    ui = QComboBoxDemon()
    ui.show()
    sys.exit(app.exec_())