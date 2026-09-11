#include "searchone_menu.h"
#include "stdio.h"
#include "stdint.h"
#include "stdbool.h"
#include "utility.h"
#include "db.h"

// 打印一条查询结果
static void printStuInfo(const char *name, const char *num, const char *profession, const char *class)
{
    printf("%s\t%s\t%s\t%s\n", name, num, profession, class);
}

void searchoneMenu()
{
    int64_t size = getConsoleSize();
    int32_t height = size, width = (size >> 32);

    displayCursor(true);

    // 获取要查找的学生的信息
    printSthAtSwh(false, width / 2 - 30, height / 2 - 7, "请输入要查找学生的姓名或学号或专业或班级（输入all查询全部）：");
    char info[100] = "";
    scanf("%99s", info);

    displayCursor(false);

    // 输出结果信息
    printSthAtSwh(false, width / 2 - 16, height / 2 - 5, "查询结果（姓名/学号/专业/班级）：");
    setCursorPos(width / 2 - 16, height / 2 - 4);
    int count = dbSearch(info, printStuInfo);
    fflush(stdout);
    if (count == 0)
    {
        printSthAtSwh(false, width / 2 - 16, height / 2 - 3, "没有找到匹配的学生信息！");
    }

    getKey(NULL, 0);
    clearScreen();
}
