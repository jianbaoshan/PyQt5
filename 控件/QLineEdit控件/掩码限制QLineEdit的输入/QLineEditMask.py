'''
        用掩码限制QLineEdit控件的输入
A   ASCII字母字符是必需输入的（A-Z a-z）
a   ASCII字母字符是允许输入的，但不是必需的（A-Z a-z）
N   ASCII字母字符是必需输入的（A-Z a-z 0-9）
n   ASCII字母字符是允许输入的，但是不是必需的（A-Z a-z 0-9）
X   任何字符都是必须输入的
x   任何字符都是允许输入的，但是不是必需的
9   ASCII数字字符是必需输入的（0-9）
0   ASCII数字字符是允许输入的，但是不是必需的（0-9）
D   ASCII数字字符是必需输入的（1-9）
d   ASCII数字字符或加减符号是允许输入的，但不是必需的（1-9）
#   ASCI数字字符是允许输入的，但不是必需的
H   十六进制格式字符是必需输入的（A-F,a-f,0-9）
h   十六进制格式字符是允许输入的，但是不是必需的（A-F,a-f,0-9）
B   二进制格式字符是必需输入的（0-1）
b   二进制格式字符是允许输入的，但不是必需的（0-1）
>   所有的字母字符都是大写
<   所有的字母字符都是小写
!   关闭大小写转换
\   转义上面列出的字符
'''

from PyQt5.Qt import *
import sys

class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')      #设置窗口标题

        #使用表格布局
        layout = QFormLayout()

        #使用四个行输入
        ip = QLineEdit()            #ip地址：192.168.21.11
        mac = QLineEdit()           #mac地址：ac:bc:ed:fc:de:cd:ad
        date = QLineEdit()          #日期：2019-12-14
        license = QLineEdit()       #许可证：ASDW:WEQE:WQEQ:DSDA:DQWE:DSAA

        #使用掩码来限制QLineEdit的输入字符
        ip.setInputMask('000.000.000.000;_')        #0代表允许输入数字字符，.是直接显示在文本框中的，;_代表没有输入时使用_代替
        mac.setInputMask('HH:HH:HH:HH:HH:HH;_')     #H代表允许输入十六进制格式字符，:是直接显示在文本框中的，;_代表没有输入时使用_代替
        date.setInputMask('0000-00-00 00：00:00;_') #0代表允许输入数字字符，.是直接显示在文本框中的，;_代表没有输入时使用_代替
        #>代表输入字符是大写，A是必需输入ASCII字母字符，-是直接显示在行输入框中的，;#是没有输入显示#
        license.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        #将行输入框放入表格布局中
        layout.addRow('ip地址掩码',ip)
        layout.addRow('mac地址掩码',mac)
        layout.addRow('日期掩码',date)
        layout.addRow('许可证掩码',license)

        #设置布局为表格布局
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./6.jpg'))
    ui = QLineEditMask()
    ui.show()
    sys.exit(app.exec_())