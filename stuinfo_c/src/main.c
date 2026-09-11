#include "stdio.h"
#include "stdbool.h"
#include "utility.h"
#include "db.h"
#include "start_menu.h"
#include "addnew_menu.h"
#include "deleteone_menu.h"
#include "changeone_menu.h"
#include "searchone_menu.h"

int main()
{
    // 设置控制台（启用ANSI转义序列和UTF-8代码页）
    initConsole();

    // 打开数据库，不存在则创建并建表
    if (!dbOpen())
    {
        printf("打开数据库失败！\n");
        return 1;
    }

    setConsoleTitle("学生信息管理系统");
    displayCursor(false);

    // 进入主流程
    bool flag = true;
    while (flag)
    {
        int res = startMenu();
        // 标准输入结束时（比如Ctrl-D）退出
        if (res == EOF)
        {
            break;
        }
        switch (res)
        {
        // 添加新的学生信息
        case '1':
            addnewMenu();
            break;
        // 删除学生信息
        case '2':
            deleteoneMenu();
            break;
        // 修改学生信息
        case '3':
            changeoneMenu();
            break;
        // 查询学生信息
        case '4':
            searchoneMenu();
            break;
        // 退出
        case '5':
            flag = false;
            break;
        }
    }

    displayCursor(true);
    dbClose();
    return 0;
}
