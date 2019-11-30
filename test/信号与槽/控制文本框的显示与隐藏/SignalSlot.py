import sys
from PyQt5 import  QtWidgets
#导入由.ui文件编译成的.py文件
import ShowEnable

#在QtDesigner中点击Edit->Edit Signals/Slots，然后在点击按钮进行拖拽，会出现红色的箭头，松开就会
#出现关于按钮的所有信号的操作方法了：这里我们使用click()这个单击方法

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wind = QtWidgets.QMainWindow()
    #向主控件添加其他控件
    ui = ShowEnable.Ui_MainWindow()
    ui.setupUi(wind)
    wind.show()
    sys.exit(app.exec_())

