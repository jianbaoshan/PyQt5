
'''
QSpinBox计数器控件
'''

import  sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QSpinBoxDemon(QWidget):
    def __init__(self):
        super(QSpinBoxDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QSpinBox计数器控件")
        self.resize(300,300)

        #初始化label
        self.label = QLabel('当前值：33')                            #设置label名称
        self.label.setAlignment(Qt.AlignCenter)                   #居中对齐

        #初始化计数器
        self.spin = QSpinBox()                                    #设置计数器的名称
        self.spin.setRange(1,99)                                  #设置计数器的范围
        self.spin.setSingleStep(7)                                #设置计数器的步长
        self.spin.setValue(33)                                    #设置默认值
        self.spin.valueChanged.connect(self.ValueChange)          #绑定信号与槽

        #使用垂直布局
        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.spin)

        self.setLayout(layout)

    #绑定信号与槽
    def ValueChange(self):
        self.label.setText('当前值：' + str(self.spin.value()))   #打印当前值

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./15.jpg'))
    ui = QSpinBoxDemon()
    ui.show()
    sys.exit(app.exec_())