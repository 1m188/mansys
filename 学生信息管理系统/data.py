from PyQt5.Qt import *
from pymysql import *
from Gui.loginGui import LoginGui
from Gui.mainGui import MainGui


class Data(QObject):
    loginSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.init)
        self.thread.start()

    def init(self):
        self.connection = connect(host="localhost",port=3306,user="root",password="123456",db="stuinfosystem",charset="utf8",cursorclass=cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def addClass(self,cl):
        if type(cl) == LoginGui:
            cl.loginSignal.connect(self.loginSlot)
            cl.registerSignal.connect(self.registerSlot)
            self.loginSignal.connect(cl.accept)
        elif type(cl) == MainGui:
            pass

    def loginSlot(self,acountInfo):
        self.cursor.execute("select * from acount where username=%s" % acountInfo.split(' ')[0])
        result = self.cursor.fetchone()
        if result:
            if result["password"] == acountInfo.split(' ')[1]:
                self.loginSignal.emit()
            else:
                print("密码错误！")
        else:
            print("没有此用户！")

    def registerSlot(self,acountInfo):
        self.cursor.execute("select * from acount where username=%s" % acountInfo.split(' ')[0])
        result = self.cursor.fetchone()
        if result:
            print("该用户已存在！")
        else:
            self.cursor.execute("insert into acount values(%s,%s)" % (acountInfo.split(' ')[0],acountInfo.split(' ')[1]))
            self.connection.commit()
            print("注册成功！")
