#include "platform.h"
#include "stdio.h"
#include "termios.h"
#include "unistd.h"
#include "sys/ioctl.h"

void platformInitConsole()
{
    // POSIX终端天然支持ANSI转义序列，无需额外初始化
}

void platformGetConsoleSize(int32_t *width, int32_t *height)
{
    struct winsize ws;
    // 标准输出不是终端（比如被重定向）时退回默认大小
    if (ioctl(STDOUT_FILENO, TIOCGWINSZ, &ws) != 0 || ws.ws_col == 0 || ws.ws_row == 0)
    {
        *width = 80;
        *height = 24;
        return;
    }
    *width = ws.ws_col;
    *height = ws.ws_row;
}

void platformSetTitle(const char *title)
{
    // 用OSC转义序列设置终端标题
    printf("\x1b]0;%s\x07", title);
    fflush(stdout);
}

int platformGetch()
{
    // 标准输入不是终端（比如被重定向）时直接读
    if (!isatty(STDIN_FILENO))
    {
        return getchar();
    }

    // 临时关闭行缓冲和回显来读取单个按键，读完之后恢复原设置
    struct termios oldt, newt;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    int ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    return ch;
}
