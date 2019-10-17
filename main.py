'''
整个应用的主流程，启动文件，主要是最开始实例化数据处理类，然后登陆，成功了就进入主界面，addClass函数是用来连接信号和信号槽的
'''

from PyQt5.QtWidgets import QApplication, QDialog
import sys
from data import Data
from Gui.loginGui import LoginGui
from Gui.mainGui import MainGui

app = QApplication(sys.argv)

data = Data()

loginGui = LoginGui()
data.addClass(loginGui)
loginGui.show()
if loginGui.exec() == QDialog.Accepted:
    mainGui = MainGui()
    data.addClass(mainGui)
    mainGui.show()
    app.exec()
