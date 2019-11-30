import sys
from PyQt5 import  QtWidgets
#导入由.ui文件编译成的.py文件
import Ui_Tab

#在QtDesigner中使用Crtl+R可以预览设计的Qt的界面
#使用tab键可以切换输入的控件顺序，默认是从上到下的，这个顺序可以被修改的
#选择Edit->Edit Tab Order，然后就可以修改顺序了

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wind = QtWidgets.QMainWindow()
    #向主控件添加其他控件
    ui = Ui_Tab.Ui_MainWindow()
    ui.setupUi(wind)
    wind.show()
    sys.exit(app.exec_())

