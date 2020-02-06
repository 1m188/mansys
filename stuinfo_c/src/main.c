#include "stdio.h"
#include "stdbool.h"
#include "utility.h"
#include "start_menu.h"
#include "addnew_menu.h"
#include "deleteone_menu.h"
#include "changeone_menu.h"
#include "searchone_menu.h"

int main(int argc, char *argv[])
{
    // 判断数据文件是否存在，不存在则创建一个
    FILE *f = fopen(fileName, "r");
    if (!f)
    {
        f = fopen(fileName, "w");
    }
    fclose(f);

    // 设置控制台
    initConsoleScreenBufferSize();
    setConsoleTitle("Students Information Management System");
    displayCursor(false);

    // 进入主流程
    bool flag = true;
    while (flag)
    {
        int res = startMenu();
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

    return 0;
}