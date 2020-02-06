#include "start.h"
#include "stdbool.h"
#include "stdint.h"
#include "../utility.h"

int startMenu()
{
    int64_t size = getConsoleSize();
    int32_t height = size, width = (size >> 32);

    // 这里打印菜单
    printSthAtSwh(false, width / 2 - 20, height / 2 - 10, "Students Information Management System");
    printSthAtSwh(false, width / 2 - 20, height / 2 - 8, "1. add someone student's information.");
    printSthAtSwh(false, width / 2 - 20, height / 2 - 6, "2. delete someone student's information.");
    printSthAtSwh(false, width / 2 - 20, height / 2 - 4, "3. change someone student's information.");
    printSthAtSwh(false, width / 2 - 20, height / 2 - 2, "4. search someone student's information.");
    printSthAtSwh(false, width / 2 - 20, height / 2, "5. exit.");

    // 这里检测按键，如果有相应的按键按下则返回相应的数字，
    // 之后进入到其他的流程之中
    const char keyList[] = {'1', '2', '3', '4', '5'};
    int ch = getKey(keyList, 5);
    system("cls");
    return ch;
}