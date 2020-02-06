#include "deleteone_menu.h"
#include "stdio.h"
#include "stdint.h"
#include "stdbool.h"
#include "string.h"
#include "utility.h"

void deleteoneMenu()
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

    // 从数据文件中删除信息
    deleteone(info);

    // 给出结束信息
    printSthAtSwh(true, width / 2 - 27, height / 2 - 7, "information deleted! press any key to come back start menu...");

    getKey(NULL, 0);
    system("cls");
}

void deleteone(const char *info)
{
    // 新建一个新的文件，从原来的文件里不断地读数据写到新文件，如果
    // 有相同的数据的话则不写到新文件中，最后把原来的文件删除并重命
    // 名新的文件
    FILE *f = fopen(fileName, "r");
    FILE *tempF = fopen("temp", "w");
    char stuInfo[40];
    memset(stuInfo, '\0', 40);
    int i = 0, ch;
    while ((ch = fgetc(f)) != EOF)
    {
        stuInfo[i] = ch;
        i++;
        if (ch == '\n')
        {
            if (strcmp(stuInfo, info))
            {
                fprintf(tempF, stuInfo);
            }
            memset(stuInfo, '\0', 40);
            i = 0;
        }
    }
    fclose(f);
    fclose(tempF);
    remove(fileName);
    rename("temp", fileName);
}