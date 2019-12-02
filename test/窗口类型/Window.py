import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QWidget,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon

#窗口类型有三种：Main Window、Widget、Dialg
#QMainWindow：有菜单栏、工具栏、状态栏
#Dialog:对话窗口的基类，没有菜单栏、工具栏、状态栏
#QWidget：不确定窗口的类型，就是要这个

#自己定义一个类，是从QMainWindow这个类继承来的
class FirstWindow(QMainWindow):
    def __init__(self, parent=None):
        super(FirstWindow, self).__init__(parent)

        #设置主窗口的标题
        self.setWindowTitle("窗口居中")

        #设置窗口尺寸
        self.resize(400, 300)

        #添加状态栏
        self.status = self.statusBar()

        #显示状态栏的消息：只存在5秒钟
        self.status.showMessage("只存在5秒的消息", 5000)

        #添加控件按键来控制窗口的退出
        self.button1 = QPushButton('退出窗口')
        #将信号与槽关联起来
        self.button1.clicked.connect(self.ButtonQuit)

        #水平布局，将按钮放到水平布局上
        layout = QHBoxLayout()
        layout.addWidget(self.button1)


        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    #按钮事件来退出窗口
    def ButtonQuit(self):
        sen = self.sender()
        #print(sen.text() + '按钮被按下')
        app = QApplication.instance()
        #退出窗口
        app.quit()

    # 让窗口居中显示，以窗口的左上角的顶点来确定
    def center(self):
        #获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标
        WindSize = self.geometry()

        #计算窗口居中时，左上角顶点的坐标点
        newleft = (screen.width() - WindSize.width()) / 2
        newright = (screen.height() - WindSize.height()) / 2
        #移动窗口的左上角的顶点
        self.move(newleft, newright)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #设置主窗口的图标
    app.setWindowIcon(QIcon('./bird.jpg'))
    ui = FirstWindow()
    ui.center()
    ui.show()
    sys.exit(app.exec_())