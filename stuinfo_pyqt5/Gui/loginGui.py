'''
最开始的登陆用户的界面
'''

from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont
from Gui.registerGui import RegisterGui
from Gui.baseGui import BaseGui


class LoginGui(QDialog, BaseGui):
    loginSignal = pyqtSignal(str)  # 登陆请求
    registerSignal = pyqtSignal(str)  # 注册请求

    def __init__(self):
        super().__init__()

        # 界面基本设置
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setAttribute(Qt.WA_QuitOnClose, True)

        # 设置界面的标题和大小
        self.setWindowTitle("登录")
        self.setFixedSize(600, 300)

        # 移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        self.initUI()  # UI设置

    def initUI(self):
        # 控件+布局
        infoLabel = QLabel(self)
        infoLabel.setAlignment(Qt.AlignCenter)
        infoLabel.setFont(QFont("微软雅黑", 12))
        infoLabel.setText("请输入用户名和密码登录")
        infoLabel.resize(infoLabel.sizeHint())
        infoLabel.move(self.width() / 2 - infoLabel.width() / 2, self.height() / 10)

        nameLabel = QLabel(self)
        nameLabel.setAlignment(Qt.AlignCenter)
        nameLabel.setText("用户名")
        nameLabel.resize(nameLabel.sizeHint())
        nameLabel.move(self.width() / 2 - nameLabel.width() - 100, infoLabel.y() + infoLabel.height() + 50)

        passwordLabel = QLabel(self)
        passwordLabel.setAlignment(Qt.AlignCenter)
        passwordLabel.setText("密码")
        passwordLabel.resize(passwordLabel.sizeHint())
        passwordLabel.move(nameLabel.x(), nameLabel.y() + nameLabel.height() + 50)

        self.nameLineEdit = QLineEdit(self)
        self.nameLineEdit.resize(self.nameLineEdit.sizeHint())
        self.nameLineEdit.move(self.width() / 2 + 30, nameLabel.y())

        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.resize(self.passwordLineEdit.sizeHint())
        self.passwordLineEdit.move(self.nameLineEdit.x(), passwordLabel.y())

        quitButton = QPushButton(self)
        quitButton.setText("退出")
        quitButton.resize(quitButton.sizeHint())
        quitButton.move(self.width() - quitButton.width() - 10, self.height() - quitButton.height() - 10)
        quitButton.clicked.connect(self.close)

        loginButton = QPushButton(self)
        loginButton.setDefault(True)
        loginButton.setText("登录")
        loginButton.resize(loginButton.sizeHint())
        loginButton.move(quitButton.x() - loginButton.width() - 10, quitButton.y())
        loginButton.clicked.connect(self.loginButtonClicked)

        registerButton = QPushButton(self)
        registerButton.setText("注册")
        registerButton.resize(registerButton.sizeHint())
        registerButton.move(self.width() - quitButton.x() - quitButton.width(), quitButton.y())
        registerButton.clicked.connect(self.registerButtonClicked)

    # 单击登陆按钮
    def loginButtonClicked(self):
        if self.nameLineEdit.text() == "" or self.passwordLineEdit.text() == "":
            QMessageBox.warning(self, "警告", "用户名或密码不可为空！")
        else:
            self.loginSignal.emit(self.nameLineEdit.text() + ' ' + self.passwordLineEdit.text())

    # 单击注册按钮
    def registerButtonClicked(self):
        registerGui = RegisterGui()
        registerGui.registerSignal.connect(self.registerSignal)  # 注册请求
        self.msgSignal.connect(registerGui.msgSlot)  # 消息发送
        registerGui.exec()
