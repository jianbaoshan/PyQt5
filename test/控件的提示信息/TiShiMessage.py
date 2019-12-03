import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QWidget,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon


class TiMessage(QMainWindow):
    def __init__(self):
        super(TiMessage, self).__init__()
        self.setUi()

    def setUi(self):
        # 设置主窗口的标题
        self.setWindowTitle("窗口的提示信息")

        # 设置窗口尺寸 工作区的大小 不包含标题栏的  因为标题栏不能放控件
        self.resize(350, 300)
        self.move(400, 150)  # 窗口放在屏幕的坐标
        self.setToolTip('这是一个主窗口')      #设置窗口提示信息的方法

        # 添加控件按键来控制窗口的退出
        self.button1 = QPushButton(self)
        self.button1.setText('输出窗口坐标系')
        self.button1.move(100, 100)  # 将按钮放在窗口的位置
        self.button1.setToolTip('这是一个按钮：按下会输出信息')

        # 将信号与槽关联起来
        self.button1.clicked.connect(self.PrintMessage)

    def PrintMessage(self):
        print('Hello World!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./2.jpg'))
    ui = TiMessage()
    ui.show()
    sys.exit(app.exec_())


