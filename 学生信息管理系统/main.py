from PyQt5.QtWidgets import QApplication,QWidget
import sys
from Gui.loginGui import LoginGui


app = QApplication(sys.argv)

loginGui = LoginGui()
loginGui.show()

app.exec()