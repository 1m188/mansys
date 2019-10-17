'''
一个帮助界面
'''

from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class HelpGui(QDialog):
    def __init__(self):
        super().__init__()

        # 界面基本设置
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setAttribute(Qt.WA_QuitOnClose, False)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 界面标题和大小
        self.setWindowTitle("帮助")
        self.setFixedSize(600, 300)

        # 移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        self.initUI()  # UI启动

    def initUI(self):
        # 控件+布局
        infoLabel = QLabel(self)
        infoLabel.setFont(QFont("微软雅黑", 15))
        infoLabel.setText("学生信息管理系统\n\t——相信你一定会用")
        infoLabel.resize(infoLabel.sizeHint())
        infoLabel.move(self.width() / 2 - infoLabel.width() / 2, self.height() / 5)

        okButton = QPushButton(self)
        okButton.setDefault(True)
        okButton.setText("确定")
        okButton.resize(okButton.sizeHint())
        okButton.move(self.width() - okButton.width() - 20, self.height() - okButton.height() - 20)
        okButton.clicked.connect(self.close)
