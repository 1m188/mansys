'''
用来删除学生信息的界面
'''

from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton,QGridLayout,QMessageBox
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QFont
from Gui.baseGui import BaseGui


class DelGui(QWidget,BaseGui):
    delSignal = pyqtSignal(str) #删除请求
    closeSignal = pyqtSignal() #界面关闭信号

    def __init__(self):
        super().__init__()

        #界面基本设置
        self.setAttribute(Qt.WA_QuitOnClose,False)
        self.setAttribute(Qt.WA_DeleteOnClose,True)

        #设置界面标题和大小
        self.setWindowTitle("删除学生信息")
        self.resize(500,200)

        #移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        self.initUI() #UI设置

    def initUI(self):
        #控件
        infoLabel = QLabel(self)
        infoLabel.setAlignment(Qt.AlignCenter)
        infoLabel.setFont(QFont("微软雅黑",15))
        infoLabel.setText("请输入你要删除的学生的信息")

        nameLabel = QLabel(self)
        nameLabel.setAlignment(Qt.AlignCenter)
        nameLabel.setFont(QFont("微软雅黑",10))
        nameLabel.setText("学生姓名")

        ageLabel = QLabel(self)
        ageLabel.setAlignment(Qt.AlignCenter)
        ageLabel.setFont(QFont("微软雅黑",10))
        ageLabel.setText("学生年龄")

        numLabel = QLabel(self)
        numLabel.setAlignment(Qt.AlignCenter)
        numLabel.setFont(QFont("微软雅黑",10))
        numLabel.setText("学生学号")

        professLabel = QLabel(self)
        professLabel.setAlignment(Qt.AlignCenter)
        professLabel.setFont(QFont("微软雅黑",10))
        professLabel.setText("学生专业")

        self.nameLineEdit = QLineEdit(self)

        self.ageLineEdit = QLineEdit(self)

        self.numLineEdit = QLineEdit(self)

        self.professLineEdit = QLineEdit(self)

        delButton = QPushButton(self)
        delButton.setText("删除")
        delButton.clicked.connect(self.delButtonClicked)

        #布局
        layout = QGridLayout(self)
        layout.addWidget(infoLabel,0,0,2,12)
        layout.addWidget(nameLabel,2,0,1,3)
        layout.addWidget(ageLabel,2,3,1,3)
        layout.addWidget(numLabel,2,6,1,3)
        layout.addWidget(professLabel,2,9,1,3)
        layout.addWidget(self.nameLineEdit,3,0,1,3)
        layout.addWidget(self.ageLineEdit,3,3,1,3)
        layout.addWidget(self.numLineEdit,3,6,1,3)
        layout.addWidget(self.professLineEdit,3,9,1,3)
        layout.addWidget(delButton,4,11,1,1)

    #单击删除按钮
    def delButtonClicked(self):
        if self.nameLineEdit.text() == "" or self.ageLineEdit.text() == "" or self.numLineEdit.text() == "" or self.professLineEdit.text() == "":
            QMessageBox.critical(self,"错误","学生信息不可为空！",QMessageBox.Ok)
        else:
            self.delSignal.emit(self.nameLineEdit.text() + ' ' + self.ageLineEdit.text() + ' ' + self.numLineEdit.text() + ' ' + self.professLineEdit.text())

    #关闭的时候发出这个信号，表示界面已经关闭
    def closeEvent(self, QCloseEvent):
        self.closeSignal.emit()
        return super().closeEvent(QCloseEvent)
