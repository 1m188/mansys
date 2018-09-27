# StudentsInformationSystem_PyQt
一个用pyqt5写的学生信息管理系统，能够访问本地MySQL数据库
1. 使用 vs2015，python 3.6.2 32bit，pymysql 0.8.0，pyqt5 5.11.2，MySQL Server version: 5.7.19-log MySQL Community Server (GPL) 开发。
2. 由于连接的是本地的MySQL数据库，所以如果要修改连接数据库的方式以及某些参数的话，需要在data.py的init函数中进行修改。
3. 连接的是一个叫做stuinfosystem的数据库，里面有两张表，分别叫做acount和stuinfo。其中acount主要储存的是用户的登陆账号和密码，有两个字段，分别是username和password，类型都是char（100） not null。stuinfo的表中主要储存的是学生的信息，有四个字段，分别是name，age，num和profession，分别储存学生的姓名，年龄，学号和专业，类型分别是char(10) not null，char(10) not null,char(20) not null,char(50) not null。
