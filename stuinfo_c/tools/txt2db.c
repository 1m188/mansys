/*
 * 一次性数据迁移工具：把旧版本的文本数据文件data.txt导入sqlite数据库。
 *
 * 用法: txt2db [data.txt] [stuinfo.db]
 *
 * 1. 逐行读取data.txt，每行按空白拆成姓名、学号、专业、班级四个字段后写入数据库；
 * 2. 字段数不为4的行视为坏行，跳过不导入；
 * 3. 全部行都成功导入后才删除data.txt，只要存在坏行就保留原文件并给出提示。
 */

#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdbool.h"
#include "sqlite3.h"

// 建表语句
static const char *createTableSql = "create table if not exists stuinfo ("
                                    "name        char(10) not null,"
                                    "num         char(20) not null,"
                                    "profession  char(50) not null,"
                                    "class       char(20) not null);";

// 从一行内容里拆出四个字段，字段数不为4时返回false
static bool splitStuInfo(char *line, char **name, char **num, char **profession, char **class)
{
    char *fields[4] = {NULL};
    int count = 0;
    char *token = strtok(line, " \t");
    while (token)
    {
        if (count < 4)
        {
            fields[count] = token;
        }
        count++;
        token = strtok(NULL, " \t");
    }
    if (count != 4)
    {
        return false;
    }
    *name = fields[0];
    *num = fields[1];
    *profession = fields[2];
    *class = fields[3];
    return true;
}

int main(int argc, char *argv[])
{
    const char *txtFile = argc > 1 ? argv[1] : "data.txt";
    const char *dbFile = argc > 2 ? argv[2] : "stuinfo.db";

    // 打开文本数据文件
    FILE *f = fopen(txtFile, "r");
    if (!f)
    {
        printf("无法打开数据文件%s！\n", txtFile);
        return 1;
    }

    // 打开数据库，不存在则创建并建表
    sqlite3 *db = NULL;
    if (sqlite3_open(dbFile, &db) != SQLITE_OK)
    {
        printf("无法打开数据库%s！\n", dbFile);
        fclose(f);
        return 1;
    }
    char *errMsg = NULL;
    if (sqlite3_exec(db, createTableSql, NULL, NULL, &errMsg) != SQLITE_OK)
    {
        printf("建表失败：%s\n", errMsg);
        sqlite3_free(errMsg);
        fclose(f);
        sqlite3_close(db);
        return 1;
    }

    // 逐行读取并导入
    char line[256];
    int lineNo = 0, okCount = 0, badCount = 0;
    while (fgets(line, sizeof(line), f))
    {
        lineNo++;
        // 去掉行尾的换行
        line[strcspn(line, "\r\n")] = '\0';
        // 空行直接跳过
        if (line[0] == '\0')
        {
            continue;
        }

        char *name, *num, *profession, *class;
        if (!splitStuInfo(line, &name, &num, &profession, &class))
        {
            printf("第%d行格式有误，已跳过：%s\n", lineNo, line);
            badCount++;
            continue;
        }

        sqlite3_stmt *stmt = NULL;
        sqlite3_prepare_v2(db, "insert into stuinfo values(?, ?, ?, ?);", -1, &stmt, NULL);
        if (stmt)
        {
            sqlite3_bind_text(stmt, 1, name, -1, SQLITE_STATIC);
            sqlite3_bind_text(stmt, 2, num, -1, SQLITE_STATIC);
            sqlite3_bind_text(stmt, 3, profession, -1, SQLITE_STATIC);
            sqlite3_bind_text(stmt, 4, class, -1, SQLITE_STATIC);
            if (sqlite3_step(stmt) == SQLITE_DONE)
            {
                okCount++;
            }
            else
            {
                printf("第%d行写入数据库失败：%s\n", lineNo, sqlite3_errmsg(db));
                badCount++;
            }
            sqlite3_finalize(stmt);
        }
        else
        {
            printf("第%d行写入数据库失败：%s\n", lineNo, sqlite3_errmsg(db));
            badCount++;
        }
    }
    fclose(f);
    sqlite3_close(db);

    printf("迁移完成：成功导入%d条，失败%d条。\n", okCount, badCount);
    if (badCount == 0)
    {
        remove(txtFile);
        printf("数据文件%s已删除。\n", txtFile);
    }
    else
    {
        printf("由于存在未导入的行，数据文件%s被保留。\n", txtFile);
    }
    return 0;
}
