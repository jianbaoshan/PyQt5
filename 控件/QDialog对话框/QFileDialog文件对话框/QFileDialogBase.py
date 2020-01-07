''''
QFileDialgo文件对话框
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QFileDialogDemon(QWidget):
    def __init__(self):
        super(QFileDialogDemon, self).__init__()
        self.setUi()

    def setUi(self):
        self.setWindowTitle("QFileDialog文件对话框")
        self.resize(500, 500)

        # 初始化按钮
        self.but1 = QPushButton('加载图片')
        self.but1.clicked.connect(self.loadPicture)

        # 初始化label，将打开的图片在label中显示
        self.imageLabel = QLabel()

        self.but2 = QPushButton('加载文件')
        self.but2.clicked.connect(self.loadFiles)

        # 初始化文本输入框,将打开的文件内容显示在文本输入框中
        self.fileContents = QTextEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.but1)
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.but2)
        layout.addWidget(self.fileContents)

        self.setLayout(layout)

    # 加载图片
    def loadPicture(self):
        # 一次只能打开一个文件 第三个参数代表打开当前路径，最后一个表示限制打开文件的类型为jpg或png
        # 返回要打开文件的名字，_代表不取消
        file_name,_ = QFileDialog.getOpenFileName(self, '打开文件', '.', "图像文件(*.jpg *.png)")
        self.imageLabel.setPixmap(QPixmap(file_name))       # 显示打开的图片

    # 加载文件
    def loadFiles(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)             # 打开所有文件
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()              # 可以选择多个文件
            # 以只读模式打开第一个文件,使用utf-8显示
            f = open(filenames[0], encoding="utf-8", mode='r')
            with f:                                         # 使用with是为了当关闭对话框时，自动的调用f.close方法来关闭打开的文件
                data = f.read()                             # 读取文件内容
                self.fileContents.setText(data)             # 将读取的文件内容显示到文本输入框中


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置主窗口的图标和应用程序的图标
    app.setWindowIcon(QIcon('./20.jpg'))
    ui = QFileDialogDemon()
    ui.show()
    sys.exit(app.exec_())
