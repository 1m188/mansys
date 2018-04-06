from PyQt5.QtWidgets import QApplication,QDialog
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
