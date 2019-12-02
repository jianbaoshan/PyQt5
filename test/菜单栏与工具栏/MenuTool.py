import sys
from PyQt5 import  QtWidgets
#导入由.ui文件编译成的.py文件
import SimpleMenuToolBar


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wind = QtWidgets.QMainWindow()
    #向主控件添加其他控件
    ui = SimpleMenuToolBar.Ui_MainWindow()
    ui.setupUi(wind)
    wind.show()
    sys.exit(app.exec_())

