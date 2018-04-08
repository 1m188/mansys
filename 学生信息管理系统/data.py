from PyQt5.Qt import *
from pymysql import *
from Gui.loginGui import LoginGui
from Gui.mainGui import MainGui


class Data(QObject):
    loginSignal = pyqtSignal()
    queryResultSignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.init)
        self.thread.start()

    def init(self):
        self.connection = connect(host="localhost",port=3306,user="root",password="123456",db="stuinfosystem",charset="utf8",cursorclass=cursors.DictCursor)
        self.cursor = self.connection.cursor()

    #添加与各个界面的信号交互
    def addClass(self,cl):
        if type(cl) == LoginGui:
            cl.loginSignal.connect(self.loginSlot)
            cl.registerSignal.connect(self.registerSlot)
            self.loginSignal.connect(cl.accept)
        elif type(cl) == MainGui:
            cl.querySignal.connect(self.querySlot)
            self.queryResultSignal.connect(cl.queryResultSlot)
            cl.enterSignal.connect(self.enterSlot)
            cl.delSignal.connect(self.delSlot)

    #登陆信号槽
    def loginSlot(self,acountInfo):
        self.cursor.execute("select * from acount where username='%s'" % acountInfo.split(' ')[0])
        result = self.cursor.fetchone()
        if result:
            if result["password"] == acountInfo.split(' ')[1]:
                self.loginSignal.emit()
            else:
                print("密码错误！")
        else:
            print("没有此用户！")

    #注册信号槽
    def registerSlot(self,acountInfo):
        self.cursor.execute("select * from acount where username='%s'" % acountInfo.split(' ')[0])
        result = self.cursor.fetchone()
        if result:
            print("该用户已存在！")
        else:
            self.cursor.execute("insert into acount values('%s','%s')" % (acountInfo.split(' ')[0],acountInfo.split(' ')[1]))
            self.connection.commit()
            print("注册成功！")

    #查询信号槽
    def querySlot(self,stuInfo):
        if stuInfo.split(' ')[0] == "" and stuInfo.split(' ')[1] == "":
            self.cursor.execute("select * from stuinfo")
        elif stuInfo.split(' ')[0] != "" and stuInfo.split(' ')[1] != "":
            self.cursor.execute("select * from stuinfo where name='%s' and num='%s'" % (stuInfo.split(' ')[0],stuInfo.split(' ')[1]))
        else:
            self.cursor.execute("select * from stuinfo where name='%s' or num='%s'" % (stuInfo.split(' ')[0],stuInfo.split(' ')[1]))
        result = self.cursor.fetchall()
        self.queryResultSignal.emit(list(result))

    #导入信息信号槽
    def enterSlot(self,stuInfo):
        stuInfoList = stuInfo.split(' ')
        self.cursor.execute("select * from stuinfo where name='%s' and age='%s' and num='%s' and profession='%s'" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
        result = list(self.cursor.fetchall())
        if len(result) > 0:
            pass
        else:
            self.cursor.execute("insert into stuinfo values('%s','%s','%s','%s')" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
            self.connection.commit()

    #删除信息信号槽
    def delSlot(self,stuInfo):
        stuInfoList = stuInfo.split(' ')
        self.cursor.execute("select * from stuinfo where name='%s' and age='%s' and num='%s' and profession='%s'" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
        result = list(self.cursor.fetchall())
        if len(result) > 0:
            self.cursor.execute("delete from stuinfo where name='%s' and age='%s' and num='%s' and profession='%s'" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
            self.connection.commit()
        else:
            pass
