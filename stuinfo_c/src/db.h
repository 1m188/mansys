#pragma once

#include "stdbool.h"

// 数据库文件名
#define DB_FILE_NAME "stuinfo.db"

// 打开数据库，不存在则创建并建表，成功返回true
bool dbOpen();

// 关闭数据库
void dbClose();

// 添加一条学生信息
void dbAdd(const char *name, const char *num, const char *profession, const char *class);

// 删除姓名、学号、专业、班级完全匹配的学生信息
void dbDelete(const char *name, const char *num, const char *profession, const char *class);

// 将源信息修改为目标信息
void dbChange(const char *srcName, const char *srcNum, const char *srcProfession, const char *srcClass,
              const char *dstName, const char *dstNum, const char *dstProfession, const char *dstClass);

// 查询学生信息：info为"all"时查询全部，否则查询姓名、学号、专业、班级任一字段吻合的记录
// 每查到一条记录就调用一次callback，返回查到的记录条数
typedef void (*dbQueryCallback)(const char *name, const char *num, const char *profession, const char *class);
int dbSearch(const char *info, dbQueryCallback callback);
