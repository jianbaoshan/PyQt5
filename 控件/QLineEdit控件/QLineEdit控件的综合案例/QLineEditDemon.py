'''
QLineEdit控件的综合案例
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys

class QLineEditDmon(QWidget):
    def __init__(self):
        super(QLineEditDmon, self).__init__()
        self.setUi()

    def setUi(self):
        #校验器
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())     #只能输入数字
        edit1.setMaxLength(6)                   #数字的最大长度为4
        edit1.setAlignment(Qt.AlignRight)       #右对齐
        edit1.setFont(QFont('Arial', 50))       #设置字体大小

        #浮点校验
        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.999, 99.999, 3))  #精度为3
        edit2.setMaxLength(8)                                   # 数字的最大长度为8,包含小数点
        edit2.setAlignment(Qt.AlignLeft)                        # 左对齐
        edit2.setFont(QFont('Arial', 30))                       # 设置字体大小

        #使用掩码
        edit3 = QLineEdit()
        edit3.setInputMask('99-999-9999;_')
        edit3.setAlignment(Qt.AlignCenter)                      # 居中对齐对齐
        edit3.setFont(QFont('Arial', 60))                       # 设置字体大小

        #信号和QLineEdit控件
        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textChange)
        edit4.setMaxLength(3)                           # 数字的最大长度为3
        edit4.setAlignment(Qt.AlignLeft)                # 左对齐
        edit4.setFont(QFont('Arial', 10))               # 设置字体大小

        #密码回显模式
        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)  #绑定槽
        edit5.setMaxLength(6)                           # 数字的最大长度为3
        edit5.setAlignment(Qt.AlignCenter)              # 居中对齐
        edit5.setFont(QFont('Arial', 50))               # 设置字体大小

        #只读
        edit6 = QLineEdit("Hell World!")
        edit6.setReadOnly(True)                         #只读属性为真
        edit6.setAlignment(Qt.AlignCenter)  # 居中对齐
        edit6.setFont(QFont('Arial', 50))  # 设置字体大小

        #使用表格布局
        layout = QFormLayout()
        layout.addRow('整数校验', edit1)
        layout.addRow('浮点校验', edit2)
        layout.addRow('掩码', edit3)
        layout.addRow('文本变化', edit4)
        layout.addRow('密码', edit5)
        layout.addRow('只读', edit6)


        #将表单布局设置到窗口上
        self.setLayout(layout)
        #设置窗口名称
        self.setWindowTitle('QLineEdit控件的综合案例')

    #信号槽
    def textChange(self, text):
        print('输入的内容' + text)

    def enterPress(self):
        print('已输入值')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./7.jpg'))
    ui = QLineEditDmon()
    ui.show()
    sys.exit(app.exec_())

