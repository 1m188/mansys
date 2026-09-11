#include "platform.h"
#include "Windows.h"
#include "conio.h"
#include "stdio.h"

#ifndef ENABLE_VIRTUAL_TERMINAL_PROCESSING
#define ENABLE_VIRTUAL_TERMINAL_PROCESSING 0x0004
#endif

void platformInitConsole()
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD mode = 0;
    // 启用虚拟终端处理让ANSI转义序列生效（Windows 10及以上支持）
    if (GetConsoleMode(hOut, &mode))
    {
        SetConsoleMode(hOut, mode | ENABLE_VIRTUAL_TERMINAL_PROCESSING);
    }

    // 输入输出代码页都设为UTF-8以支持中文
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
}

void platformGetConsoleSize(int32_t *width, int32_t *height)
{
    CONSOLE_SCREEN_BUFFER_INFO info;
    if (GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info))
    {
        *width = info.srWindow.Right - info.srWindow.Left + 1;
        *height = info.srWindow.Bottom - info.srWindow.Top + 1;
    }
    else
    {
        *width = 80;
        *height = 25;
    }
}

void platformSetTitle(const char *title)
{
    SetConsoleTitleA(title);
}

int platformGetch()
{
    return _getch();
}
