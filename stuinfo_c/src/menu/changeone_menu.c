#include "changeone_menu.h"
#include "stdio.h"
#include "stdint.h"
#include "utility.h"
#include "db.h"

void changeoneMenu()
{
    int64_t size = getConsoleSize();
    int32_t height = size, width = (size >> 32);

    displayCursor(true);

    // 源信息
    char srcName[64] = "", srcNum[64] = "", srcProfession[64] = "", srcClass[64] = "";

    // 姓名
    printSthAtSwh(false, width / 2 - 19, height / 2 - 7, "请输入该学生原来的姓名：");
    scanf("%63s", srcName);

    // 学号
    printSthAtSwh(false, width / 2 - 19, height / 2 - 5, "请输入该学生原来的学号：");
    scanf("%63s", srcNum);

    // 专业
    printSthAtSwh(false, width / 2 - 19, height / 2 - 3, "请输入该学生原来的专业：");
    scanf("%63s", srcProfession);

    // 班级
    printSthAtSwh(false, width / 2 - 19, height / 2 - 1, "请输入该学生原来的班级：");
    scanf("%63s", srcClass);

    clearScreen();

    // 目标信息
    char dstName[64] = "", dstNum[64] = "", dstProfession[64] = "", dstClass[64] = "";

    // 姓名
    printSthAtSwh(false, width / 2 - 19, height / 2 - 7, "请输入修改后的姓名：");
    scanf("%63s", dstName);

    // 学号
    printSthAtSwh(false, width / 2 - 19, height / 2 - 5, "请输入修改后的学号：");
    scanf("%63s", dstNum);

    // 专业
    printSthAtSwh(false, width / 2 - 19, height / 2 - 3, "请输入修改后的专业：");
    scanf("%63s", dstProfession);

    // 班级
    printSthAtSwh(false, width / 2 - 19, height / 2 - 1, "请输入修改后的班级：");
    scanf("%63s", dstClass);

    displayCursor(false);

    // 修改
    dbChange(srcName, srcNum, srcProfession, srcClass, dstName, dstNum, dstProfession, dstClass);

    // 给出结束信息
    printSthAtSwh(true, width / 2 - 22, height / 2 - 7, "信息修改成功！按任意键返回主菜单...");

    getKey(NULL, 0);
    clearScreen();
}
