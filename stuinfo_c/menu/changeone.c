#include "changeone.h"
#include "stdint.h"
#include "string.h"
#include "../utility.h"
#include "deleteone.h"
#include "addnew.h"

void changeoneMenu()
{
    int64_t size = getConsoleSize();
    int32_t height = size, width = (size >> 32);

    displayCursor(true);

    // 源信息
    char sourceInfo[100];
    memset(sourceInfo, '\0', 100);

    // 姓名
    printSthAtSwh(false, width / 2 - 21, height / 2 - 7, "Please enter the student's origin name:");
    scanf("%s", sourceInfo);
    sourceInfo[strlen(sourceInfo)] = ' ';

    // 学号
    printSthAtSwh(false, width / 2 - 21, height / 2 - 5, "Please enter the student's origin number:");
    scanf("%s", sourceInfo + strlen(sourceInfo));
    sourceInfo[strlen(sourceInfo)] = ' ';

    // 专业
    printSthAtSwh(false, width / 2 - 21, height / 2 - 3, "Please enter the student's origin profession:");
    scanf("%s", sourceInfo + strlen(sourceInfo));
    sourceInfo[strlen(sourceInfo)] = ' ';

    // 班级
    printSthAtSwh(false, width / 2 - 21, height / 2 - 1, "Please enter the student's origin class:");
    scanf("%s", sourceInfo + strlen(sourceInfo));
    sourceInfo[strlen(sourceInfo)] = '\n';

    system("cls");

    // 目标信息
    char dstInfo[100];
    memset(dstInfo, '\0', 100);

    // 姓名
    printSthAtSwh(false, width / 2 - 21, height / 2 - 7, "Please enter the student's new name:");
    scanf("%s", dstInfo);
    dstInfo[strlen(dstInfo)] = ' ';

    // 学号
    printSthAtSwh(false, width / 2 - 21, height / 2 - 5, "Please enter the student's new number:");
    scanf("%s", dstInfo + strlen(dstInfo));
    dstInfo[strlen(dstInfo)] = ' ';

    // 专业
    printSthAtSwh(false, width / 2 - 21, height / 2 - 3, "Please enter the student's new profession:");
    scanf("%s", dstInfo + strlen(dstInfo));
    dstInfo[strlen(dstInfo)] = ' ';

    // 班级
    printSthAtSwh(false, width / 2 - 21, height / 2 - 1, "Please enter the student's new class:");
    scanf("%s", dstInfo + strlen(dstInfo));
    dstInfo[strlen(dstInfo)] = '\n';

    displayCursor(false);

    // 修改
    changeone(sourceInfo, dstInfo);

    // 给出结束信息
    printSthAtSwh(true, width / 2 - 27, height / 2 - 7, "information changed! press any key to come back start menu...");

    getKey(NULL, 0);
    system("cls");
}

void changeone(const char *src, const char *dst)
{
    // 删除掉原来的，将修改过后的信息作为新的添加进去
    deleteone(src);
    addnew(dst);
}