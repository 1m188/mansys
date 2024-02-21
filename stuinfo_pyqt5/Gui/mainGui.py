'''
整个应用的主界面
'''

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QAbstractItemView, QHeaderView, QPushButton, QMenuBar, QMenu, QAction, QGridLayout, QApplication
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont
from Gui.helpGui import HelpGui
from Gui.enterGui import EnterGui
from Gui.delGui import DelGui
from Gui.baseGui import BaseGui


class MainGui(QWidget, BaseGui):
    querySignal = pyqtSignal(str)  # 查询请求
    enterSignal = pyqtSignal(str)  # 导入请求
    delSignal = pyqtSignal(str)  # 删除请求

    def __init__(self):
        super().__init__()

        self.isEnterGuiOpen = False  # 导入界面是否打开
        self.isDelGuiOpen = False  # 删除界面是否打开

        # 界面基本设置
        self.setAttribute(Qt.WA_QuitOnClose, True)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        # 设置标题和大小
        self.setWindowTitle("学生信息管理系统")
        self.resize(900, 600)

        # 移动到屏幕中央
        rect = self.frameGeometry()
        rect.moveCenter(QApplication.desktop().availableGeometry().center())
        self.move(rect.topLeft())

        self.initUI()  # UI设置

    def initUI(self):
        # 控件
        infoLabel = QLabel(self)
        infoLabel.setAlignment(Qt.AlignCenter)
        infoLabel.setFont(QFont("微软雅黑", 20))
        infoLabel.setText("学生信息管理系统")

        nameLabel = QLabel(self)
        nameLabel.setAlignment(Qt.AlignCenter)
        nameLabel.setFont(QFont("微软雅黑", 10))
        nameLabel.setText("学生姓名")

        numLabel = QLabel(self)
        numLabel.setAlignment(Qt.AlignCenter)
        numLabel.setFont(QFont("微软雅黑", 10))
        numLabel.setText("学生学号")

        self.nameLineEdit = QLineEdit(self)

        self.numLineEdit = QLineEdit(self)

        self.stuInfoList = QTableWidget(self)
        # 选中项目编辑动作为不编辑
        self.stuInfoList.setEditTriggers(self.stuInfoList.NoEditTriggers)
        # 取消掉每次新增条目的序号id显示
        self.stuInfoList.verticalHeader().setHidden(True)
        self.stuInfoList.setColumnCount(4)
        self.stuInfoList.setHorizontalHeaderLabels(["姓名", "年龄", "学号", "专业"])
        # 选中条目的动作为选中那一行
        self.stuInfoList.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 将每个条目扩展到充满容器
        self.stuInfoList.horizontalHeader().setStretchLastSection(True)
        # 将容器宽度平均分给所有条目
        self.stuInfoList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        queryButton = QPushButton(self)
        queryButton.setText("查询")
        queryButton.setDefault(True)
        queryButton.clicked.connect(self.queryButtonClicked)

        # 菜单
        menuBar = QMenuBar(self)
        menuBar.setStyleSheet("QMenuBar{background-color:rgb(240,240,240)}")

        menu = QMenu(menuBar)
        menu.setTitle("菜单")
        menuBar.addMenu(menu)

        enterAction = QAction(menu)
        enterAction.setText("导入")
        enterAction.triggered.connect(self.enterActionTriggered)
        menu.addAction(enterAction)

        delAction = QAction(menu)
        delAction.setText("删除")
        delAction.triggered.connect(self.delActionTriggered)
        menu.addAction(delAction)

        quitAction = QAction(menu)
        quitAction.setText("退出")
        quitAction.triggered.connect(self.close)
        menu.addAction(quitAction)

        helpAction = QAction(menuBar)
        helpAction.setText("帮助")
        helpAction.triggered.connect(self.helpActionTriggered)
        menuBar.addAction(helpAction)

        # 布局
        layout = QGridLayout(self)
        layout.addWidget(infoLabel, 0, 0, 1, 10)
        layout.addWidget(nameLabel, 1, 0, 1, 6)
        layout.addWidget(self.nameLineEdit, 1, 6, 1, 3)
        layout.addWidget(numLabel, 2, 0, 1, 6)
        layout.addWidget(self.numLineEdit, 2, 6, 1, 3)
        layout.addWidget(self.stuInfoList, 3, 0, 5, -1)
        layout.addWidget(queryButton, 8, 9, 1, 1)
        layout.setMenuBar(menuBar)

    # 单击查询按钮
    def queryButtonClicked(self):
        self.querySignal.emit(self.nameLineEdit.text() + ' ' + self.numLineEdit.text())

    # 返回来的查询结果显示到界面上
    def queryResultSlot(self, result):
        self.stuInfoList.setRowCount(len(result))
        for i in range(len(result)):
            self.stuInfoList.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            self.stuInfoList.setItem(i, 1, QTableWidgetItem(str(result[i][1])))
            self.stuInfoList.setItem(i, 2, QTableWidgetItem(str(result[i][2])))
            self.stuInfoList.setItem(i, 3, QTableWidgetItem(str(result[i][3])))

    # 导入信息界面
    def enterActionTriggered(self):
        if not self.isEnterGuiOpen:
            self.enterGui = EnterGui()
            self.enterGui.enterSignal.connect(self.enterSignal)
            self.enterGui.closeSignal.connect(self.enterGuiCloseSlot)
            self.msgSignal.connect(self.enterGui.msgSlot)
            self.isEnterGuiOpen = True
            self.enterGui.show()

    # 导入界面关闭
    def enterGuiCloseSlot(self):
        self.isEnterGuiOpen = False
        del self.enterGui

    # 删除信息界面
    def delActionTriggered(self):
        if not self.isDelGuiOpen:
            self.delGui = DelGui()
            self.delGui.delSignal.connect(self.delSignal)
            self.delGui.closeSignal.connect(self.delGuiCloseSlot)
            self.msgSignal.connect(self.delGui.msgSlot)
            self.isDelGuiOpen = True
            self.delGui.show()

    # 删除界面关闭
    def delGuiCloseSlot(self):
        self.isDelGuiOpen = False
        del self.delGui

    # 帮助界面
    def helpActionTriggered(self):
        helpGui = HelpGui()
        helpGui.exec()
