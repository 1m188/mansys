from PyQt5.Qt import *
from pymysql import *
from Gui.loginGui import LoginGui
from Gui.mainGui import MainGui


class Data(QObject):
    def __init__(self):
        super().__init__()

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.init)
        self.thread.start()

    def init(self):
        pass

    def addClass(self,cl):
        if type(cl) == LoginGui:
            pass
        elif type(cl) == MainGui:
            pass