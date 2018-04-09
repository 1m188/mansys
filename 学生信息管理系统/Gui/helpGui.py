'''
一个帮助界面
'''

from PyQt5.Qt import *


class HelpGui(QDialog):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_DeleteOnClose,True)

        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle("帮助")
        self.setFixedSize(600,300)

        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        infoLabel = QLabel(self)
        infoLabel.setFont(QFont("微软雅黑",15))
        infoLabel.setText("学生信息管理系统\n\t——相信你一定会用")
        infoLabel.resize(infoLabel.sizeHint())
        infoLabel.move(self.width() / 2 - infoLabel.width() / 2,self.height() / 5)

        okButton = QPushButton(self)
        okButton.setDefault(True)
        okButton.setText("确定")
        okButton.resize(okButton.sizeHint())
        okButton.move(self.width() - okButton.width() - 20,self.height() - okButton.height() - 20)
        okButton.clicked.connect(self.close)
