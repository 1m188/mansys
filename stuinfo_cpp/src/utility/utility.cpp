#include "utility.h"
#include "Windows.h"

void displayCursor(bool isDisplay)
{
    HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_CURSOR_INFO info;
    info.bVisible = isDisplay;
    info.dwSize = sizeof(info);
    SetConsoleCursorInfo(h, &info);
}