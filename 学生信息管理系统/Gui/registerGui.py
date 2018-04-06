from PyQt5.Qt import *


class RegisterGui(QDialog):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_DeleteOnClose)

        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowTitle("注册")
        self.setFixedSize(600,300)
        
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

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
        self.passwordLineEdit.resize(self.passwordLineEdit.sizeHint())
        self.passwordLineEdit.move(self.nameLineEdit.x(),passwordLabel.y())

        registerButton = QPushButton(self)
        registerButton.setText("注册")
        registerButton.resize(registerButton.sizeHint())
        registerButton.move(self.width() - registerButton.width() - 10,self.height() - registerButton.height() - 10)
        registerButton.clicked.connect(self.registerButtonClicked)

    def registerButtonClicked(self):
        if self.nameLineEdit.text() == "" or self.passwordLineEdit.text() == "":
            QMessageBox.warning(self,"警告","用户名或密码不可为空！")
        else:
            pass
