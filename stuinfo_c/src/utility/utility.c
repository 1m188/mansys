#include "utility.h"
#include "platform.h"
#include "stdio.h"

void initConsole()
{
    platformInitConsole();
}

void setConsoleTitle(const char *title)
{
    platformSetTitle(title);
}

void displayCursor(bool isDisplay)
{
    fputs(isDisplay ? "\x1b[?25h" : "\x1b[?25l", stdout);
    fflush(stdout);
}

void setCursorPos(int x, int y)
{
    printf("\x1b[%d;%dH", y + 1, x + 1);
    fflush(stdout);
}

int64_t getConsoleSize()
{
    int32_t width = 0, height = 0;
    platformGetConsoleSize(&width, &height);
    return ((int64_t)width << 32) + height;
}

void clearScreen()
{
    fputs("\x1b[2J\x1b[H", stdout);
    fflush(stdout);
}

void printSthAtSwh(bool isClsBefore, int x, int y, const char *data)
{
    if (isClsBefore)
    {
        clearScreen();
    }
    setCursorPos(x, y);
    fputs(data, stdout);
    fflush(stdout);
}

int getKey(const char *keyList, int len)
{
    // 如果keyList为空或者长度为0，则一旦有按键按下立刻返回
    if (!keyList || !len)
    {
        return platformGetch();
    }
    // 否则按下keyList中的按键才返回
    while (true)
    {
        int ch = platformGetch();
        // 标准输入结束时原样返回，避免死循环
        if (ch == EOF)
        {
            return EOF;
        }
        int i;
        for (i = 0; i < len; i++)
        {
            if (ch == keyList[i])
            {
                return ch;
            }
        }
    }
}
