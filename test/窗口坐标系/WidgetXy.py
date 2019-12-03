import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QWidget,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon

#窗口的坐标系
class WidgetXY(QWidget):
    def __init__(self):
        super(WidgetXY, self).__init__()

        #设置主窗口的标题
        self.setWindowTitle("窗口的坐标系")

        #设置窗口尺寸 工作区的大小 不包含标题栏的  因为标题栏不能放控件
        self.resize(350, 300)
        self.move(400, 150)         #窗口放在屏幕的坐标

        #添加控件按键来控制窗口的退出
        self.button1 = QPushButton(self)
        self.button1.setText('输出窗口坐标系')
        self.button1.move(100, 100)                 #将按钮放在窗口的位置

        #将信号与槽关联起来
        self.button1.clicked.connect(self.PrintXY)

    def PrintXY(self):
        print('-----------------------1------------------------------------')
        print(self.x())                         #窗口所在屏幕的X坐标     400     这个包含标题栏的
        print(self.y())                         #窗口所在屏幕的Y坐标     150
        print(self.width())                     #窗口的宽                350    工作区
        print(self.height())                    #窗口的高                300

        print('-----------------------2------------------------------------')
        print(self.geometry().x())              #工作区的横坐标       408                 这个边框
        print(self.geometry().y())              #工作区的纵坐标       180
        print(self.geometry().width())          #工作区的宽度       350
        print(self.geometry().height())         #工作区的高度       300

        print('-----------------------3------------------------------------')
        print(self.frameGeometry().x())         #窗口的坐标       400
        print(self.frameGeometry().y())         #窗口的坐标       150
        print(self.frameGeometry().width())     #窗口的宽度       366
        print(self.frameGeometry().height())    #窗口的高度       338
        print('-----------------------4------------------------------------')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #设置主窗口的图标
    app.setWindowIcon(QIcon('./1.jpg'))
    ui = WidgetXY()
    ui.show()
    sys.exit(app.exec_())