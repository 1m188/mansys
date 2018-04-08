from PyQt5.Qt import *
from msg import Msg


class BaseGui:
    msgSignal = pyqtSignal(Msg)

    def msgSlot(self,msg):
        if msg.aim == type(self):
            QMessageBox.about(self,msg.title,msg.msg)
        else:
            self.msgSignal.emit(msg)
