# stuinfo_c

一个用C语言实现的控制台版本的学生信息管理系统。

1. 支持Windows、Linux、macOS三个平台，控制台操作（清屏、光标定位、按键读取等）基于ANSI转义序列和少量平台API实现，不依赖第三方库。
2. 使用内嵌的sqlite3源码（lib/sqlite_3310100）存储学生信息，数据库文件为程序运行目录下的stuinfo.db，其中stuinfo表包含姓名、学号、专业、班级四个字段。
3. 能够对学生信息进行增删改查等基础操作，查询时输入all可以查询所有信息。

## 使用方法

clone项目之后用cmake构建（要求cmake版本大于等于3.15），Windows下配合Visual Studio，Linux/macOS下用gcc或clang：

    cmake -B build
    cmake --build build

Windows下也可以用Visual Studio直接打开build目录里生成的工程文件来编译。构建成功后会在build目录（或其内部的子目录）里生成两个程序：

- stuinfo_c：学生信息管理系统主程序，直接运行即可。
- txt2db：一次性数据迁移工具。如果存在旧版本遗留的data.txt数据文件，运行一次`txt2db data.txt stuinfo.db`即可把旧数据导入数据库，全部导入成功后data.txt会被删除；存在格式有误无法导入的行时会保留原文件并给出提示。

## 说明

- 界面提示为中文（UTF-8）。Windows下需要Windows 10及以上版本，程序会自动启用终端的ANSI转义序列支持并设置UTF-8代码页。
- 数据库文件stuinfo.db在程序运行目录下自动创建，不需要手动准备。
