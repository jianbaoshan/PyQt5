'''
QDialog对话框

QMessageBox         消息对话框
QColorDailog        颜色对话框
QFileDailog         文件对话框
QInputDailog        输入对话框

'''


import  sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QDialogDemon(QMainWindow):
    def __init__(self):
        super(QDialogDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QDialog对话框")
        self.resize(500,500)

        #初始化按钮
        self.but = QPushButton(self)                #直接把按钮放在主窗口上
        self.but.setText('弹出对话框')               #设置按钮的名称
        self.but.move(50, 30)                       #移动按钮的位置
        self.but.clicked.connect(self.showDialog)   #绑定信号与槽


    #信号槽
    def showDialog(self):
        myDailog = QDialog()
        myDailog.setWindowTitle('QDialog对话框1')
        myDailog.resize(300, 300)
        myDailog.setWindowModality(Qt.ApplicationModal)     #设置对话框模式：除非关闭该对话框否则主窗口无法操作

        but1 = QPushButton('确定',myDailog)
        #but1.setText('确定')
        but1.move(40, 50)
        but1.clicked.connect(myDailog.close)                #将按钮与对话框关闭绑定起来

        #显示对话框
        myDailog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./16.jpg'))
    ui = QDialogDemon()
    ui.show()
    sys.exit(app.exec_())