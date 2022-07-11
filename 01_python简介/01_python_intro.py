# -*- coding:utf-8 -*-
# @Time : 2022/7/11 8:26 下午
# @Author : Bin Bin Xue
# @File : 1.1_python历史
# @Project : python_basic

# 记录书中的一些关键信息

# 1.1 python历史

# python在1989年诞生，比java诞生还早，java在1991年诞生，在1995年才更名为java
# python = modula3 + unix + c

# 1.2 为什么使用python?
#  1- python开发效率高（python能作为原型开发工具，先用python作出一个小的demo，再用java或c++做成品或对其进行改造）

# 1.3 搭建python3.8开发环境
# 下载python
# 运行python
# 选择python IDE - pyCharm

# 1.4 pyCharm第一个程序 - hello world

# 1.5 python语言特性
# 1-python的缩进（四个空格或一个tab，不要混用这两个）
# 2-python序列（列表、元组、字典等，序列可做运算、切片、索引、复制等）
# 3-python支持各种编程模式（类、重载、对象等）
# 4-python动态性（根据语义确定数据类型。。）
# 5-支持匿名函数、嵌套函数
# 6-python自省（python显示方法）

# 1.6 python3.8新功能
# 1-海象运算符 n:=k 中的n不用提前定义
# 2-参数占位符：/，可以用'/'充当一个参数值（位置参数时使用）
# 3-支持f字符调试串调试：更便于输出表达式的值

if __name__ == '__main__':
    # 海象运算符
    a = '66666'
    if (n:=len(a)) < 8:
        print(n)

    # 参数占位符（这个不对）
    def f(a,b,c):
        print(a+c)
    f(1,'/',3)

    # f字符串调试
    x = 6
    print(f'{x + 2}')
    print(f'{x + 2=}')