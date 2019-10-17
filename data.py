'''
后台数据处理类，所有可能需要耗时且和界面无关的请求将以信号的形式发到这里进行处理，完毕之后如果需要反馈再反馈
'''

from PyQt5.QtCore import QObject,QThread,pyqtSignal
from pymysql import *
from Gui.loginGui import LoginGui
from Gui.registerGui import RegisterGui
from Gui.mainGui import MainGui
from Gui.enterGui import EnterGui
from Gui.delGui import DelGui
from msg import Msg


class Data(QObject):
    loginSignal = pyqtSignal() #登陆信号
    queryResultSignal = pyqtSignal(list) #查询数据库信号
    msgSignal = pyqtSignal(Msg) #给界面发送消息的信号

    def __init__(self):
        super().__init__()

        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.init) #线程初始化
        #资源管理
        self.destroyed.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start() #启动线程

    def init(self):
        #数据库操作
        self.connection = connect(host="localhost",port=3306,user="root",password="123456",db="stuinfosystem",charset="utf8",cursorclass=cursors.DictCursor)
        self.cursor = self.connection.cursor()

    #添加与各个界面的信号交互
    def addClass(self,cl):
        #如果是登陆界面
        if type(cl) == LoginGui:
            cl.loginSignal.connect(self.loginSlot) #登陆请求
            cl.registerSignal.connect(self.registerSlot) #注册请求
            self.loginSignal.connect(cl.accept) #登陆成功
            self.msgSignal.connect(cl.msgSlot) #发送消息
        #如果是主界面
        elif type(cl) == MainGui:
            cl.querySignal.connect(self.querySlot) #数据库操作
            self.queryResultSignal.connect(cl.queryResultSlot) #数据库操作结果
            cl.enterSignal.connect(self.enterSlot) #导入请求
            cl.delSignal.connect(self.delSlot) #删除请求
            self.msgSignal.connect(cl.msgSlot) #发送消息

    #登陆信号槽
    def loginSlot(self,acountInfo):
        self.cursor.execute("select * from acount where username='%s'" % acountInfo.split(' ')[0])
        result = self.cursor.fetchone()
        #如果能够查询到这个用户的话
        if result:
            #如果密码对的话，则登陆
            if result["password"] == acountInfo.split(' ')[1]:
                self.loginSignal.emit()
            else:
                self.msgSignal.emit(Msg(LoginGui,"错误","密码错误！"))
        #否则则说明没有这个用户
        else:
            self.msgSignal.emit(Msg(LoginGui,"错误","没有此用户！"))

    #注册信号槽
    def registerSlot(self,acountInfo):
        self.cursor.execute("select * from acount where username='%s'" % acountInfo.split(' ')[0])
        result = self.cursor.fetchone()
        #判定注册的用户账号是否已经存在
        if result:
            self.msgSignal.emit(Msg(RegisterGui,"警告","该用户已存在！"))
        else:
            #往表中插入相关用户数据
            self.cursor.execute("insert into acount values('%s','%s')" % (acountInfo.split(' ')[0],acountInfo.split(' ')[1]))
            self.connection.commit() #提交数据库更改
            self.msgSignal.emit(Msg(RegisterGui,"成功","注册成功！"))

    #查询信号槽
    def querySlot(self,stuInfo):
        #查询所有
        if stuInfo.split(' ')[0] == "" and stuInfo.split(' ')[1] == "":
            self.cursor.execute("select * from stuinfo")
        #按照姓名和学号查询
        elif stuInfo.split(' ')[0] != "" and stuInfo.split(' ')[1] != "":
            self.cursor.execute("select * from stuinfo where name='%s' and num='%s'" % (stuInfo.split(' ')[0],stuInfo.split(' ')[1]))
        #否则按照姓名或学号查询
        else:
            self.cursor.execute("select * from stuinfo where name='%s' or num='%s'" % (stuInfo.split(' ')[0],stuInfo.split(' ')[1]))
        result = self.cursor.fetchall()
        self.queryResultSignal.emit(list(result))

    #导入信息信号槽
    def enterSlot(self,stuInfo):
        stuInfoList = stuInfo.split(' ')
        #首先查询一波，看看这个学生的信息是否已经被导入
        self.cursor.execute("select * from stuinfo where name='%s' and age='%s' and num='%s' and profession='%s'" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
        result = list(self.cursor.fetchall())
        if len(result) > 0:
            self.msgSignal.emit(Msg(EnterGui,"错误","该学生信息已经导入！"))
        else:
            #否则就导入
            self.cursor.execute("insert into stuinfo values('%s','%s','%s','%s')" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
            self.connection.commit() #提交数据库更改
            self.msgSignal.emit(Msg(EnterGui,"成功","导入学生信息成功！"))

    #删除信息信号槽
    def delSlot(self,stuInfo):
        stuInfoList = stuInfo.split(' ')
        #查询是否有这个学生的信息
        self.cursor.execute("select * from stuinfo where name='%s' and age='%s' and num='%s' and profession='%s'" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
        result = list(self.cursor.fetchall())
        #如果有的话则删除
        if len(result) > 0:
            self.cursor.execute("delete from stuinfo where name='%s' and age='%s' and num='%s' and profession='%s'" % (stuInfoList[0],stuInfoList[1],stuInfoList[2],stuInfoList[3]))
            self.connection.commit()
            self.msgSignal.emit(Msg(DelGui,"成功","删除学生信息成功！"))
        else:
            self.msgSignal.emit(Msg(DelGui,"错误","没有该学生信息！"))
