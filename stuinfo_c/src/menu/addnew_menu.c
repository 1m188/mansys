#include "addnew_menu.h"
#include "stdio.h"
#include "stdbool.h"
#include "stdint.h"
#include "string.h"
#include "utility.h"

void addnewMenu()
{
    int64_t size = getConsoleSize();
    int32_t height = size, width = (size >> 32);

    displayCursor(true);

    // 整体信息
    char info[100];
    memset(info, '\0', 100);

    // 姓名
    printSthAtSwh(false, width / 2 - 21, height / 2 - 7, "Please enter the new student's name:");
    scanf("%s", info);
    info[strlen(info)] = ' ';

    // 学号
    printSthAtSwh(false, width / 2 - 21, height / 2 - 5, "Please enter the new student's number:");
    scanf("%s", info + strlen(info));
    info[strlen(info)] = ' ';

    // 专业
    printSthAtSwh(false, width / 2 - 21, height / 2 - 3, "Please enter the new student's profession:");
    scanf("%s", info + strlen(info));
    info[strlen(info)] = ' ';

    // 班级
    printSthAtSwh(false, width / 2 - 21, height / 2 - 1, "Please enter the new student's class:");
    scanf("%s", info + strlen(info));
    info[strlen(info)] = '\n';

    displayCursor(false);

    // 写入数据文件
    addnew(info);

    // 给出结束信息
    printSthAtSwh(true, width / 2 - 27, height / 2 - 7, "information get! press any key to come back start menu...");

    getKey(NULL, 0);
    system("cls");
}

void addnew(const char *info)
{
    FILE *f = fopen(fileName, "a"); // 追加信息
    fprintf(f, info);
    fclose(f);
}