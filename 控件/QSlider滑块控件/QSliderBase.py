
'''
滑块控件(QSlider)

'''

import  sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QSliderDemon(QWidget):
    def __init__(self):
        super(QSliderDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QSlider滑块控件")
        self.resize(300,300)

        #使用垂直布局
        layout = QVBoxLayout()

        #初始化Label，
        self.label1 = QLabel("PyQt5 Hello World 你好 世界")
        self.label1.setAlignment(Qt.AlignCenter)                 #居中对齐

        self.label2 = QLabel("宇宙你好 哈哈哈哈哈哈哈")
        self.label2.setAlignment(Qt.AlignCenter)  # 居中对齐

        #初始化滑块对象
        self.slider1 = QSlider(Qt.Horizontal)                   #滑块水平滑动
        self.slider1.setObjectName('滑块1')                     #设置滑块的名称
        self.slider1.setMinimum(18)                             #设置最小值
        self.slider1.setMaximum(48)                             #设置最大值
        self.slider1.setSingleStep(2)                           #设置步长
        self.slider1.setValue(22)                               #设置当前值
        self.slider1.setTickPosition(QSlider.TicksBelow)        #设置刻度在下方
        self.slider1.setTickInterval(6)                         #设置刻度的间隔
        self.slider1.valueChanged.connect(self.valueChange)     #信号与槽

        # 初始化滑块对象
        self.slider2 = QSlider(Qt.Vertical)                     #滑块垂直滑动
        self.slider2.setObjectName("滑块2")                     #设置滑块的名称
        self.slider2.setMinimum(3)                              #设置最小值
        self.slider2.setMaximum(66)                             #设置最大值
        self.slider2.setSingleStep(3)                           #设置步长
        self.slider2.setValue(9)                                #设置当前值
        self.slider2.setTickPosition(QSlider.TicksRight)        #设置刻度在右侧
        self.slider2.setTickInterval(6)                         #设置刻度的间隔
        self.slider2.valueChanged.connect(self.valueChange)     #信号与槽

        #布局
        layout.addWidget(self.slider1)
        layout.addWidget(self.slider2)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)


    #设置信号与槽的方法
    def valueChange(self):
        print(self.sender().objectName() + "的当前值：%s " % self.sender().value())      # 打印当前值
        if self.sender().objectName() == "滑块1":
            size1 = self.slider1.value()                                                #获取当前值
            self.label1.setFont(QFont('Arial', size1))                                  # 将当前值设置为字体的大小
        else:
            size2 = self.slider2.value()                                                #获取当前值
            self.label2.setFont(QFont('Arial', size2))                                  #将当前值设置为字体的大小


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./14.jpg'))
    ui = QSliderDemon()
    ui.show()
    sys.exit(app.exec_())