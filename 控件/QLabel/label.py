import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QWidget,QVBoxLayout,QPushButton,QLabel
from PyQt5.QtGui import QIcon,QPalette,QPixmap
from PyQt5.QtCore import Qt

#QLabel的主要操作方法：
#1、setAligment()    设置文本的对齐方式
#2、setIndent()      设置文本缩进
#3、text()           获取文本内容
#4、setBuddy()       设置伙伴关系
#5、setText()        设置文本内容
#6、selectedText()   返回所选择的字符
#7、setWordWrap()    设置是否允许换行

#QLabel常用的信号：
#1、当鼠标滑过QLabel控件时触发：linkHovered
#2、当鼠标单击QLabel控件时触发，linkActivated

class QlabelDemon(QLabel):
    def __init__(self):
        super(QlabelDemon, self).__init__()
        self.setUi()

    def setUi(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签。</font>")   #设置文本内容，颜色选择黄色
        #设置标签的背景色
        label1.setAutoFillBackground(True)          #这是标签背景色的开关：True代表打开标签背景色
        patette = QPalette()
        patette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(patette)
        #设置标签居中对齐
        label1.setAlignment(Qt.AlignCenter)

        #这也是一个超链接，只是使用默认配置：激活事件，没有打开超链接，和label4相对应
        label2.setText("<a href='www.baidu.com'>百度官网</a>")

        label3.setAlignment(Qt.AlignCenter)         #照片居中对齐
        label3.setToolTip("这是一个图片文件")
        label3.setPixmap(QPixmap("./3.jpg"))

        label4.setOpenExternalLinks(True)       #True打开超链接，False代表激活一个事件，执行对应的注册事件.事件和超链接二者只能选其一
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《PyThon从菜鸟到高手》")
        label4.setAlignment(Qt.AlignRight)          #右对齐
        label4.setToolTip('这是一个超链接')

        #垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)      #将标签放到垂直布局里面
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.MouseSlid)

        label4.linkActivated.connect(self.MousePut)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')


    def MouseSlid(self):
        print('当鼠标滑过标签时，触发事件')

    def MousePut(self):
        print('当标签被鼠标点击时，触发事件')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./3.jpg'))
    ui = QlabelDemon()
    ui.show()
    sys.exit(app.exec_())


