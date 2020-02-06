#pragma once

#include "stdbool.h"
#include "stdint.h"

// 数据文件名
extern const char *fileName;

// 显示/隐藏光标
void displayCursor(bool isDisplay);

// 定位光标
void setCursorPos(int x, int y);

// 获取控制台大小
// 返回的64位整数中，高4位是宽度，低4位是高度
int64_t getConsoleSize();

// 初始化控制台屏幕缓冲区大小（去掉右边的滑条）
void initConsoleScreenBufferSize();

// 设置控制台标题
void setConsoleTitle(const char *title);

// 在指定的坐标输出指定的内容
// 传入参数  输出之前是否要清空控制台，xy坐标，输出数据
void printSthAtSwh(bool isClsBefore, int x, int y, const char *data);

// 阻塞检测按键，当按键为keyList中的值时返回相应的按键，len为keyList的长度
// （因此keyList最后一个元素不一定要为'\0'）
int getKey(const char *keyList, int len);