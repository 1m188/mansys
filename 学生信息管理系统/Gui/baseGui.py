'''
一个基本的界面类，包含了消息信号和消息信号槽，这样其他的界面只需继承这个类即可获得相应的信号和信号槽
'''

from PyQt5.Qt import *
from msg import Msg


class BaseGui:
    msgSignal = pyqtSignal(Msg)

    def msgSlot(self,msg):
        if msg.aim == type(self):
            QMessageBox.about(self,msg.title,msg.msg)
        else:
            self.msgSignal.emit(msg)
