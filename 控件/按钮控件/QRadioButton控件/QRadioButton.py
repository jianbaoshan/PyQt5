



import  sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



class QRadioButtonBase(QWidget):
    def __init__(self):
        super(QRadioButtonBase, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QRadioButton按钮")
        self.resize(300,300)

        #初始化单选按钮
        self.but1 = QRadioButton("按钮1")
        self.but1.setChecked(True)                      #将该按钮设置为选中状态,同一个容器中的多个单选按钮都可以设置为Trye或False
        self.but1.toggled.connect(self.buttonState)     # 将按钮信号绑定到槽上


        self.but2 = QRadioButton("按钮2")
        self.but2.setChecked(False)                      # 将该按钮设置为未选中状态
        self.but2.toggled.connect(self.buttonState)     #将按钮信号绑定到槽上

        self.but3 = QRadioButton("按钮3")
        self.but3.setChecked(False)  # 将该按钮设置为未选中状态
        self.but3.toggled.connect(self.buttonState)  # 将按钮信号绑定到槽上

        self.but4 = QRadioButton("按钮4")
        self.but4.setChecked(False)  # 将该按钮设置为未选中状态
        self.but4.toggled.connect(self.buttonState)  # 将按钮信号绑定到槽上

        #使用水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.but1)                 #将按钮1加入到水平布局的容器中
        layout.addWidget(self.but2)                 #将按钮2加入到水平布局的容器中
        layout.addWidget(self.but3)                 #将按钮2加入到水平布局的容器中
        layout.addWidget(self.but4)                 #将按钮2加入到水平布局的容器中


        self.setLayout(layout)

    #信号槽
    def buttonState(self):
        radio = self.sender()                       #获取当前被点击按钮
        if radio.isChecked() == True:
            print("<" + radio.text() + '> 被选中')
        else:
            print("<" + radio.text() + '> 未被选中')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./11.jpg'))
    ui = QRadioButtonBase()
    ui.show()
    sys.exit(app.exec_())