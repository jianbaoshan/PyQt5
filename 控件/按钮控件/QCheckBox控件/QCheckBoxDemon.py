
"""
复选框控件(QCheckBox)
未选中：0
半选中：1
选中：2
"""


import  sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#很多常量都是在Qt类里面
from PyQt5.QtCore import Qt


class QCheckBoxBase(QWidget):
    def __init__(self):
        super(QCheckBoxBase, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QCheckBox按钮")
        self.resize(300,300)

        #使用垂直布局
        layout = QVBoxLayout()

        #初始化复选框控件
        self.box1 = QCheckBox("复选框控件1")
        self.box1.setChecked(True)                  #设置复选框为选中状态
        self.box1.stateChanged.connect(lambda:self.CheckBoxState(self.box1))    #将信号复选框选中状态绑定到槽上

        self.box2 = QCheckBox("复选框控件2")
        self.box2.setChecked(False)                  # 设置复选框为选中状态
        self.box2.stateChanged.connect(lambda: self.CheckBoxState(self.box2))  # 将信号复选框选中状态绑定到槽上

        self.box3 = QCheckBox("复选框控件3:半选")
        self.box3.setTristate(True)                     #这两行是设置半选状态
        self.box3.setCheckState(Qt.PartiallyChecked)
        self.box3.stateChanged.connect(lambda: self.CheckBoxState(self.box3))  # 将信号复选框选中状态绑定到槽上

        #将复选框控件放入垂直布局中
        layout.addWidget(self.box1)
        layout.addWidget(self.box2)
        layout.addWidget(self.box3)

        self.setLayout(layout)
    #
    def CheckBoxState(self, state):
        box1state = self.box1.text() + ", isChecked" + str(self.box1.isChecked()) + ',checkState=' + str(self.box1.checkState()) + "\n"
        box2state = self.box2.text() + ", isChecked" + str(self.box2.isChecked()) + ',checkState=' + str(self.box2.checkState()) + "\n"
        box3state = self.box3.text() + ", isChecked" + str(self.box3.isChecked()) + ',checkState=' + str(self.box3.checkState()) + "\n"
        print(box1state + box2state + box3state)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./12.jpg'))
    ui = QCheckBoxBase()
    ui.show()
    sys.exit(app.exec_())