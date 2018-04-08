from PyQt5.Qt import *


class EnterGui(QWidget):
    enterSignal = pyqtSignal(str)
    closeSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_QuitOnClose,False)
        self.setAttribute(Qt.WA_DeleteOnClose,True)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("导入学生信息")
        self.resize(500,200)

        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        infoLabel = QLabel(self)
        infoLabel.setAlignment(Qt.AlignCenter)
        infoLabel.setFont(QFont("微软雅黑",15))
        infoLabel.setText("请输入你要导入的学生的信息")

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

        enterButton = QPushButton(self)
        enterButton.setText("导入")
        enterButton.clicked.connect(self.enterButtonClicked)

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
        layout.addWidget(enterButton,4,11,1,1)

    def enterButtonClicked(self):
        if self.nameLineEdit.text() == "" or self.ageLineEdit.text() == "" or self.numLineEdit.text() == "" or self.professLineEdit.text() == "":
            print("学生信息不可为空！")
        else:
            self.enterSignal.emit(self.nameLineEdit.text() + ' ' + self.ageLineEdit.text() + ' ' + self.numLineEdit.text() + ' ' + self.professLineEdit.text())

    def closeEvent(self, QCloseEvent):
        self.closeSignal.emit()
        return super().closeEvent(QCloseEvent)
