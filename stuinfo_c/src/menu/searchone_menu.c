#include "searchone_menu.h"
#include "stdio.h"
#include "stdint.h"
#include "stdbool.h"
#include "string.h"
#include "malloc.h"
#include "utility.h"

void searchoneMenu()
{
    int64_t size = getConsoleSize();
    int32_t height = size, width = (size >> 32);

    displayCursor(true);

    // 获取要查找的学生的信息
    printSthAtSwh(false, width / 2 - 34, height / 2 - 7, "Please enter the student's name or number or profession or class:");
    char info[20];
    memset(info, '\0', 20);
    scanf("%s", info);

    displayCursor(false);

    // 输出结果信息
    printSthAtSwh(false, width / 2 - 21, height / 2 - 5, "The search result:");
    char *result = (char *)searchone(info);
    int i;
    int x = width / 2 - 21, y = height / 2 - 5;
    int offsetY = 2, offset = 0;
    int len = strlen(result);
    for (i = 0; i < len; i++)
    {
        if (result[i] == '\n')
        {
            result[i] = '\0';
            printSthAtSwh(false, x, y + offsetY, result + offset);
            offsetY += 2;
            offset = i + 1;
        }
    }
    free(result);
    printSthAtSwh(false, x, y + offsetY, "Press any key to continue...");

    getKey(NULL, 0);
    system("cls");
}

const char *searchone(const char *info)
{
    // 这里读入每一条信息，如果其中有任一部分信息吻合则保留整条信息，
    // 否则转入下一条信息处理
    FILE *f = fopen(fileName, "r");
    int len = 1;
    char *result = (char *)malloc(len);
    memset(result, '\0', len);
    char stuInfo[40], cmpInfo[20];
    memset(stuInfo, '\0', 40);
    memset(cmpInfo, '\0', 20);
    int i = 0, j = 0, ch;
    bool flag = false;
    while ((ch = fgetc(f)) != EOF)
    {
        stuInfo[i] = ch;
        i++;
        if (ch != ' ' && ch != '\n' && !flag)
        {
            cmpInfo[j] = ch;
            j++;
        }
        else
        {
            if (!flag)
            {
                if (!strcmp(cmpInfo, info))
                {
                    flag = true;
                }
                memset(cmpInfo, '\0', 20);
                j = 0;
            }

            if (ch == '\n')
            {
                if (flag)
                {
                    len += strlen(stuInfo);
                    result = (char *)realloc(result, len);
                    strcat(result, stuInfo);
                    flag = false;
                }
                memset(stuInfo, '\0', 40);
                i = 0;
            }
        }
    }
    fclose(f);
    return result;
}