'''
如果没有用户，可以通过这个注册界面进行注册
'''

from PyQt5.QtWidgets import QDialog,QApplication,QLabel,QLineEdit,QPushButton,QMessageBox
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QFont
from Gui.baseGui import BaseGui


class RegisterGui(QDialog,BaseGui):
    registerSignal = pyqtSignal(str) #注册请求

    def __init__(self):
        super().__init__()

        #界面基本设置
        self.setAttribute(Qt.WA_DeleteOnClose,True)
        self.setAttribute(Qt.WA_QuitOnClose,False)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        #界面标题和大小
        self.setWindowTitle("注册")
        self.setFixedSize(600,300)
        
        #移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        self.initUI() #UI设置

    def initUI(self):
        #控件+布局
        infoLabel = QLabel(self)
        infoLabel.setAlignment(Qt.AlignCenter)
        infoLabel.setFont(QFont("微软雅黑",12))
        infoLabel.setText("请输入要注册的用户名和密码")
        infoLabel.resize(infoLabel.sizeHint())
        infoLabel.move(self.width() / 2 - infoLabel.width() / 2,self.height() / 10)

        nameLabel = QLabel(self)
        nameLabel.setAlignment(Qt.AlignCenter)
        nameLabel.setText("用户名")
        nameLabel.resize(nameLabel.sizeHint())
        nameLabel.move(self.width() / 2 - nameLabel.width() - 100,infoLabel.y() + infoLabel.height() + 50)

        passwordLabel = QLabel(self)
        passwordLabel.setAlignment(Qt.AlignCenter)
        passwordLabel.setText("密码")
        passwordLabel.resize(passwordLabel.sizeHint())
        passwordLabel.move(nameLabel.x(),nameLabel.y() + nameLabel.height() + 50)

        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.resize(self.nameLineEdit.sizeHint())
        self.nameLineEdit.move(self.width() / 2 + 30,nameLabel.y())

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.resize(self.passwordLineEdit.sizeHint())
        self.passwordLineEdit.move(self.nameLineEdit.x(),passwordLabel.y())

        registerButton = QPushButton(self)
        registerButton.setDefault(True)
        registerButton.setText("注册")
        registerButton.resize(registerButton.sizeHint())
        registerButton.move(self.width() - registerButton.width() - 10,self.height() - registerButton.height() - 10)
        registerButton.clicked.connect(self.registerButtonClicked)

    #单击注册按钮
    def registerButtonClicked(self):
        if self.nameLineEdit.text() == "" or self.passwordLineEdit.text() == "":
            QMessageBox.warning(self,"警告","用户名或密码不可为空！")
        else:
            self.registerSignal.emit(self.nameLineEdit.text() + ' ' + self.passwordLineEdit.text())
