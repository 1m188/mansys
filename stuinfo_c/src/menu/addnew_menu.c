#include "addnew_menu.h"
#include "stdio.h"
#include "stdbool.h"
#include "stdint.h"
#include "utility.h"
#include "db.h"

void addnewMenu()
{
    int64_t size = getConsoleSize();
    int32_t height = size, width = (size >> 32);

    displayCursor(true);

    char name[64] = "", num[64] = "", profession[64] = "", class[64] = "";

    // 姓名
    printSthAtSwh(false, width / 2 - 15, height / 2 - 7, "请输入新学生的姓名：");
    scanf("%63s", name);

    // 学号
    printSthAtSwh(false, width / 2 - 15, height / 2 - 5, "请输入新学生的学号：");
    scanf("%63s", num);

    // 专业
    printSthAtSwh(false, width / 2 - 15, height / 2 - 3, "请输入新学生的专业：");
    scanf("%63s", profession);

    // 班级
    printSthAtSwh(false, width / 2 - 15, height / 2 - 1, "请输入新学生的班级：");
    scanf("%63s", class);

    displayCursor(false);

    // 写入数据库
    dbAdd(name, num, profession, class);

    // 给出结束信息
    printSthAtSwh(true, width / 2 - 22, height / 2 - 7, "信息添加成功！按任意键返回主菜单...");

    getKey(NULL, 0);
    clearScreen();
}
