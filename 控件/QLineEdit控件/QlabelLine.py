from PyQt5.Qt import *
import sys


#QLineEdit控件与回显模式
#基本功能：输入单行的文本
#EchoMode回显模式：
#1、Normal           输入内容正常显示
#2、NoEcho           输入内容不显示
#3、Passwd           输入内容以'.'显示
#4、PasswdEchoEdit   正在输入内容时，正常显示；输入完成之后以'.'显示

#QLineEdit控件限制输入的内容：


class QlabelEcho(QWidget):
    def __init__(self):
        super(QlabelEcho, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle('表单回显和校验器')

        Normal = QLineEdit()
        NoEcho = QLineEdit()
        Passwd = QLineEdit()
        PasswdEchoEdit = QLineEdit()

        #使用表单布局
        form = QFormLayout()            #初始化表单布局对象

        form.addRow("Normale", Normal)                  #设置名字
        form.addRow("NoEcho", NoEcho)
        form.addRow("Passwd", Passwd)
        form.addRow("PasswdEchoEdit", PasswdEchoEdit)

        Normal.setEchoMode(QLineEdit.Normal)                                #设置回显模式：Normal
        NoEcho.setEchoMode(QLineEdit.NoEcho)                                #设置回显模式：Normal
        Passwd.setEchoMode(QLineEdit.Password)                              #设置回显模式：Normal
        PasswdEchoEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)            #设置回显模式：Normal

        #QLineEdit控件的输入条件
        intLine = QLineEdit()
        floatLine = QLineEdit()
        charLine = QLineEdit()

        form.addRow("整数类型", intLine)             # 设置名字
        form.addRow("浮点数", floatLine)             # 设置名字
        form.addRow("数字和字母", charLine)          # 设置名字

        intLine.setPlaceholderText("整数")            #设置提示文本：即在文本显示提示信息
        floatLine.setPlaceholderText("浮点数")
        charLine.setPlaceholderText("字母和数字")

        #初始化整数校验器
        intValid = QIntValidator(self)
        intValid.setRange(1, 99)                     #设置范围

        #初始化浮点校验器
        floatValid = QDoubleValidator(self)
        floatValid.setRange(-360, 360)                                   #设置范围
        floatValid.setNotation(QDoubleValidator.StandardNotation)
        floatValid.setDecimals(2)                                        #设置精度，小数点2位

        #初始化字符和数字校验器
        reg = QRegExp("[a-zA-Z0-9]+$")
        charValid = QRegExpValidator(self)
        charValid.setRegExp(reg)

        #设置校验器
        intLine.setValidator(intValid)
        floatLine.setValidator(floatValid)
        charLine.setValidator(charValid)

        self.setLayout(form)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./5.jpg'))
    ui = QlabelEcho()
    ui.show()
    sys.exit(app.exec_())