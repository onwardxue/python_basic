# -*- coding:utf-8 -*-
# @Time : 2022/7/11 9:31 下午
# @Author : Bin Bin Xue
# @File : 02_python_basic
# @Project : python_basic

# 2.2 九九乘法表

# 先将所有表达式放到列表中
def getall():
    list = []
    for i in range(1, 10):
        for j in range(1, i + 1):
            list.append(str(j) + '*' + str(i) + '=' + str(i * j))
    return list


# 将表达式按顺序打印
def printTab(lis, order='A'):
    cpLis = lis[:]
    cpLis.reverse()
    if order == 'A':
        for i in range(1, 10):
            while i > 0:
                print('%s \t' % cpLis.pop(), end=' ')
                i = i - 1
            print()
    else:
        for i in range(1, 10):
            while (10 - i > 0):
                print('%s \t' % cpLis.pop(), end=' ')
                i = i + 1
            print()


if __name__ == '__main__':

    # 2.2 编写九九乘法表
    lis = getall()
    printTab(lis,'A')
    print('\n' *2)
    printTab(lis,'B')