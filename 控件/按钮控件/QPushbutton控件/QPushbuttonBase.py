"""
按钮控件（QPushbutton）

QAbstractButton         所有按钮的父类
子类：
QPushButton             普通按钮
QToolButton             工具条按钮
QRadioButton            单选按钮
QCheckBox               多选按钮
"""

import  sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QPushButtonBaseFunction(QDialog):
    def __init__(self):
        super(QPushButtonBaseFunction, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QPushButton按钮")
        self.resize(300,300)

        #测试按钮
        self.firstButton = QPushButton("第一个按钮")         #可以直接这样设置按钮的文本
        #这两步是将按钮设置成：按一次处于选中状态，再按一次就取消掉了
        self.firstButton.setCheckable(True)
        self.firstButton.toggle()
        #将按钮信号与槽绑定起来
        self.firstButton.clicked.connect(lambda:self.whichButton(self.firstButton))
        self.firstButton.clicked.connect(self.ButtonState)

        #图像按钮
        self.SecondButton = QPushButton()
        self.SecondButton.setText('图像按钮')  # 也可以使用这个方法来设置按钮的文本
        self.SecondButton.setIcon(QIcon(QPixmap("./9.jpg")))
        self.SecondButton.clicked.connect(lambda:self.whichButton(self.SecondButton))

        #不可用按钮
        self.ThirdButton = QPushButton("不可使用的按钮")
        self.ThirdButton.setEnabled(False)

        #默认按钮：按下回车键也会自动调用这个按键
        self.FourButton = QPushButton("&MyButton")      #按ALT+M键会自动调用这个按键
        self.FourButton.setDefault(True)
        self.FourButton.clicked.connect(lambda: self.whichButton(self.FourButton))


        #使用垂直布局
        layout = QVBoxLayout()

        layout.addWidget(self.firstButton)
        layout.addWidget(self.SecondButton)
        layout.addWidget(self.ThirdButton)
        layout.addWidget(self.FourButton)

        self.setLayout(layout)

    #槽：输出被单击按钮的文本，使用传参的方式，将按钮通过参数button传递给whichButton含税
    def whichButton(self, button):
        print('单击的按钮是<' + button.text() + '>')      #text函数是读取按钮的文本

    def ButtonState(self):
        if self.firstButton.isChecked():
            print('按钮1被选中')
        else:
            print('按钮1未被选中')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./10.jpg'))
    ui = QPushButtonBaseFunction()
    ui.show()
    sys.exit(app.exec_())