from PyQt5.Qt import *
import sys

class QlabelBuddy(QDialog):
    def __init__(self):
        super(QlabelBuddy, self).__init__()
        self.setUi()

    def setUi(self):
        name = QLabel('&Name', self)            #初始化一个QLable对象，并设置文本内容为Name
        nameLine = QLineEdit(self)
        name.setBuddy(nameLine)                 #设置name和nameLine的伙伴关系

        passwd = QLabel('&Password', self)      #初始化一个QLable对象，并设置文本内容为Password
        passwdLine = QLineEdit(self)
        passwd.setBuddy(passwdLine)               # 设置passwd和passwdLine的伙伴关系

        btOK = QPushButton('&OK')               #初始化一个按键对象，并设置文本内容为OK
        btCancel = QPushButton('&Cance')        #初始化一个按键对象，并设置文本内容为Cance

        #网格布局
        mainLayout = QGridLayout(self)          #初始化网格对象

        mainLayout.addWidget(name,0,0)          #将对象name放到网格中的第一行第一列，大小为默认的1行，1列
        mainLayout.addWidget(nameLine,0,1,1,3)  #将对象nameLine放到网格的第一行第二列，大小为1行2列

        mainLayout.addWidget(passwd, 1, 0)              # 将对象name放到网格中的第二行第一列，大小为默认的1行，1列
        mainLayout.addWidget(passwdLine, 1, 1, 1, 3)    # 将对象nameLine放到网格的第二行第二列，大小为1行2列

        mainLayout.addWidget(btOK, 2, 0,1,2)  # 将对象name放到网格中的第三行第一列，大小为1行，2列
        mainLayout.addWidget(btCancel, 2, 2, 1, 2)  # 将对象nameLine放到网格的第二行第三列，大小为1行2列

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./4.jpg'))
    ui = QlabelBuddy()
    ui.show()
    sys.exit(app.exec_())