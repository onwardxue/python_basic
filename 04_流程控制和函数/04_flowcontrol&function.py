# -*- coding:utf-8 -*-
# @Time : 2022/7/14 9:06 下午
# @Author : Bin Bin Xue
# @File : 04_flowcontrol&function
# @Project : python_basic

'''
4.1 流程控制（if选择，for循环，while循环）

    4.1.1 选择结构
    if condition1:
        exper1
    elif condition2:
        exper2
    else:
        pass

    4.1.2 for循环结构
    for x in list:
        exper
    for i in rand():
        exper

        注意：当b = a[:]时，表示b是对a的复制。b=a中，b和a是同一对象

    4.1.3 while循环结构
    while condition1：
        exper1
        if condition2:
        continue/break

4.2 函数（定义、参数、调用和返回、lambda、嵌套、作用域）
    4.2.1 定义
    def <function_name> (<parameters_list>):
        <code block>

    4.2.2 参数
    特点：
    （1）参数可设置默认值
    （2）调用时可不按顺序赋值，用参数名定位
    （3）支持不定个数的参数（元组型：*arg，字典型：**argv）
    （4）python3.8新加参数：'/'
        注意：可变参数要放在最后

    设默认值：def getvolumn(len=0,width=0,height=0):
    使用参数名赋值：getvolumn(height=1,len=2)
    不定参数（元组型）：def getvloumn(*arg):   print(arg)
                                        getvloumn(1,2,3) -（结果是：（1，2，3））
    不定参数（字典型）：def getvolumn(**argv)（必须使用参数）
                                        getall(1,2,3) - （{1,2,3}）
                                        getall(one=1) - （'one' : 1）

    参数'/'：def getvolumn(len=2,width=3,/,height=4)
                当参数中有'/'时，其前面的参数必须使用默认值，不能赋值，后面的可以

    4.2.3 函数调用和返回
        使用函数名进行调用，也可以将函数名作为参数传给另一个函数做调用，如：
        def test2(fun,a,b): return fun(a,b)

        函数需要有返回值时，使用return
        def test():
            return exper1

    4.2.4 lambda函数
        理解：函数式编程，可以简单地理解为一种匿名函数，如：
        b = lambda a,b : a+b
        b(1,2)  (结果为3)

        化简：使用 and 和 or 替代 if 语句，如：
        f = lambda a:(a and 3 or 2)
        => def judge(a): if a: b=3 else: b=2 return b

        4.2.5 嵌套函数（在函数的内部定义函数）
        def getfun(x,y):
            def fun2(a,b):
                return a*b
            return fun2(x,y)
        print(getfun(2,3))  （结果是6）

        注意：如果内部函数与外部函数存在同名变量，该变量绑定的还是外部函数的值

        4.2.6 函数的作用域
        （LGB原则：对于一个变量名称，先查找局部命名空间，再查找全局命名空间，最后查找内在命令空间）

'''