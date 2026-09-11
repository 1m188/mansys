#pragma once

#include "stdint.h"

// 平台相关的控制台底层实现，由console_win.c和console_posix.c分别提供

// 控制台初始化（Windows下启用ANSI转义序列支持和UTF-8代码页）
void platformInitConsole();

// 获取控制台的宽度和高度（单位为字符）
void platformGetConsoleSize(int32_t *width, int32_t *height);

// 设置控制台标题
void platformSetTitle(const char *title);

// 阻塞读取一个按键，不回显
int platformGetch();
