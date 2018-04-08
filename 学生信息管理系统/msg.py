#消息
class Msg:
    #传入参数有 目标界面，消息标题，消息内容
    def __init__(self,aim,title,msg):
        self.aim = aim
        self.title = title
        self.msg = msg
