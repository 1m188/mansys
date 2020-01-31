#include "utility.h"
#include "Windows.h"
#include "stdio.h"

const char *fileName = "data.txt";

void displayCursor(bool isDisplay)
{
    CONSOLE_CURSOR_INFO info;
    info.bVisible = isDisplay;
    info.dwSize = sizeof(info);
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
}

void setCursorPos(int x, int y)
{
    COORD c;
    c.X = x;
    c.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), c);
}

int64_t getConsoleSize()
{
    CONSOLE_SCREEN_BUFFER_INFO info;
    GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &info);
    int32_t width = info.srWindow.Right;
    int32_t height = info.srWindow.Bottom;
    return ((int64_t)width << 32) + height;
}

void initConsoleScreenBufferSize()
{
    HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);
    CONSOLE_SCREEN_BUFFER_INFO info;
    GetConsoleScreenBufferInfo(h, &info);
    COORD c = {info.srWindow.Right + 1, info.srWindow.Bottom + 1};
    SetConsoleScreenBufferSize(h, c);
}

void setConsoleTitle(const char *title)
{
    SetConsoleTitle(title);
}

void printSthAtSwh(bool isClsBefore, int x, int y, const char *data)
{
    if (isClsBefore)
    {
        system("cls");
    }
    setCursorPos(x, y);
    printf("%s", data);
}

int getKey(const char *keyList, int len)
{
    // 如果keyList为空或者长度为0，则一旦有按键按下立刻返回
    if (!keyList || !len)
    {
        while (true)
        {
            if (kbhit())
            {
                return getch();
            }
        }
    }
    // 否则按下keyList中的按键才返回
    else
    {
        while (true)
        {
            if (kbhit())
            {
                int ch = getch();
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
    }
}