#include "db.h"
#include "sqlite3.h"
#include "stdio.h"
#include "string.h"

// 建表语句
static const char *createTableSql = "create table if not exists stuinfo ("
                                    "name        char(10) not null,"
                                    "num         char(20) not null,"
                                    "profession  char(50) not null,"
                                    "class       char(20) not null);";

static sqlite3 *db = NULL;

// 执行绑定参数的SQL，vals为按顺序绑定的参数，count为参数个数
static bool execWithBind(const char *sql, const char *vals[], int count)
{
    sqlite3_stmt *stmt = NULL;
    if (sqlite3_prepare_v2(db, sql, -1, &stmt, NULL) != SQLITE_OK)
    {
        fprintf(stderr, "prepare error: %s\n", sqlite3_errmsg(db));
        return false;
    }
    int i;
    for (i = 0; i < count; i++)
    {
        sqlite3_bind_text(stmt, i + 1, vals[i], -1, SQLITE_STATIC);
    }
    bool ok = sqlite3_step(stmt) == SQLITE_DONE;
    if (!ok)
    {
        fprintf(stderr, "exec error: %s\n", sqlite3_errmsg(db));
    }
    sqlite3_finalize(stmt);
    return ok;
}

bool dbOpen()
{
    if (sqlite3_open(DB_FILE_NAME, &db) != SQLITE_OK)
    {
        fprintf(stderr, "open database error: %s\n", db ? sqlite3_errmsg(db) : "unknown");
        db = NULL;
        return false;
    }

    char *errMsg = NULL;
    if (sqlite3_exec(db, createTableSql, NULL, NULL, &errMsg) != SQLITE_OK)
    {
        fprintf(stderr, "create table error: %s\n", errMsg);
        sqlite3_free(errMsg);
        sqlite3_close(db);
        db = NULL;
        return false;
    }
    return true;
}

void dbClose()
{
    if (db)
    {
        sqlite3_close(db);
        db = NULL;
    }
}

void dbAdd(const char *name, const char *num, const char *profession, const char *class)
{
    const char *sql = "insert into stuinfo values(?, ?, ?, ?);";
    const char *vals[4] = {name, num, profession, class};
    execWithBind(sql, vals, 4);
}

void dbDelete(const char *name, const char *num, const char *profession, const char *class)
{
    const char *sql = "delete from stuinfo where name=? and num=? and profession=? and class=?;";
    const char *vals[4] = {name, num, profession, class};
    execWithBind(sql, vals, 4);
}

void dbChange(const char *srcName, const char *srcNum, const char *srcProfession, const char *srcClass,
              const char *dstName, const char *dstNum, const char *dstProfession, const char *dstClass)
{
    const char *sql = "update stuinfo set name=?, num=?, profession=?, class=? "
                      "where name=? and num=? and profession=? and class=?;";
    const char *vals[8] = {dstName, dstNum, dstProfession, dstClass, srcName, srcNum, srcProfession, srcClass};
    execWithBind(sql, vals, 8);
}

int dbSearch(const char *info, dbQueryCallback callback)
{
    if (!db)
    {
        return 0;
    }

    sqlite3_stmt *stmt = NULL;
    // "all"查询全部，否则查询任一字段吻合的记录（同一个参数复用于四个字段）
    if (strcmp(info, "all") == 0)
    {
        sqlite3_prepare_v2(db, "select name, num, profession, class from stuinfo;", -1, &stmt, NULL);
    }
    else
    {
        sqlite3_prepare_v2(db, "select name, num, profession, class from stuinfo "
                               "where name=?1 or num=?1 or profession=?1 or class=?1;",
                           -1, &stmt, NULL);
        sqlite3_bind_text(stmt, 1, info, -1, SQLITE_STATIC);
    }
    if (!stmt)
    {
        return 0;
    }

    int count = 0;
    while (sqlite3_step(stmt) == SQLITE_ROW)
    {
        callback((const char *)sqlite3_column_text(stmt, 0),
                 (const char *)sqlite3_column_text(stmt, 1),
                 (const char *)sqlite3_column_text(stmt, 2),
                 (const char *)sqlite3_column_text(stmt, 3));
        count++;
    }
    sqlite3_finalize(stmt);
    return count;
}
