from PyQt5.Qt import *


class MainGui(QWidget):
    querySignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WA_QuitOnClose,True)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("学生信息管理系统")
        self.resize(900,600)

        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        infoLabel = QLabel(self)
        infoLabel.setAlignment(Qt.AlignCenter)
        infoLabel.setFont(QFont("微软雅黑",20))
        infoLabel.setText("学生信息管理系统")

        nameLabel = QLabel(self)
        nameLabel.setAlignment(Qt.AlignCenter)
        nameLabel.setFont(QFont("微软雅黑",10))
        nameLabel.setText("学生姓名")
        
        numLabel = QLabel(self)
        numLabel.setAlignment(Qt.AlignCenter)
        numLabel.setFont(QFont("微软雅黑",10))
        numLabel.setText("学生学号")

        self.nameLineEdit = QLineEdit(self)

        self.numLineEdit = QLineEdit(self)

        self.stuInfoList = QTableWidget(self)
        #禁止编辑表格内的查询内容
        self.stuInfoList.setEditTriggers(self.stuInfoList.NoEditTriggers)
        self.stuInfoList.setColumnCount(4)
        self.stuInfoList.setHorizontalHeaderLabels(["姓名","年龄","学号","专业"])
        #让表格头标签横向充满容器
        self.stuInfoList.horizontalHeader().setStretchLastSection(True)
        #让每个表格头标签长度相等，即均分容器长度分给每个标签
        self.stuInfoList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        queryButton = QPushButton(self)
        queryButton.setText("查询")
        queryButton.setDefault(True)
        queryButton.clicked.connect(self.queryButtonClicked)

        #菜单
        menuBar = QMenuBar(self)
        menuBar.setStyleSheet("QMenuBar{background-color:rgb(240,240,240)}")

        menu = QMenu(menuBar)
        menu.setTitle("菜单")
        menuBar.addMenu(menu)

        enterAction = QAction(menu)
        enterAction.setText("导入")
        menu.addAction(enterAction)

        delAction = QAction(menu)
        delAction.setText("删除")
        menu.addAction(delAction)

        quitAction = QAction(menu)
        quitAction.setText("退出")
        menu.addAction(quitAction)

        helpAction = QAction(menuBar)
        helpAction.setText("帮助")
        menuBar.addAction(helpAction)

        layout = QGridLayout(self)
        layout.addWidget(infoLabel,0,0,1,10)
        layout.addWidget(nameLabel,1,0,1,6)
        layout.addWidget(self.nameLineEdit,1,6,1,3)
        layout.addWidget(numLabel,2,0,1,6)
        layout.addWidget(self.numLineEdit,2,6,1,3)
        layout.addWidget(self.stuInfoList,3,0,4,-1)
        layout.addWidget(queryButton,7,9,1,1)
        layout.setMenuBar(menuBar)

    def queryButtonClicked(self):
        pass
