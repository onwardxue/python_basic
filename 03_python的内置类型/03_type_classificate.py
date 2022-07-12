# -*- coding:utf-8 -*-
# @Time : 2022/7/12 8:51 下午
# @Author : Bin Bin Xue
# @File : 03_type_classificate
# @Project : python_basic

# 3.1 python的类型分类
# python一切都封装在类当中，没有像c中的int型（参考java中的integer类）
# python内置有10大类，26小类

# 3.2 简单类型（布尔、整数、浮点、复数、None）

# 1_布尔类型（只包含两个值 - True 和 False）
# 在python中，除了False表示假以外，[]、{}、()、' '、0、0.0、None都表示假，其他为真
# and 表达式中若前一个为假，则直接返回false，后一个不计算；or 表达式则相反

# 2_整数类型（python3 整合了python2中的int和long）
# 运算顺序 （）> ** > * / % > + -
# 八进制 0o13 十六进制 0x13

# 3_ 浮点数类型（带小数点的都是）

# 4_复数类型（2+3j）

# 5_None类型（相当于c中的Null）

# 3.3 简单类型的运算
# 1_位运算
# ～a 按位求补（取反补1）
# >> << 右位移，左位移
# ^按位取异或
# & 求和
# ｜ 位或

# 运算规则：数值运算时，当有浮点型参加则结果为浮点型，否则为整型

# 3.4 常量类型
# id() 查看对象在内存中的编号
a = 3
print(id(a))

# 3.5 序列类型（容器 - 序列容器（数组），关联容器（链表））

# 3.6 列表类型 - []
# 1_元素访问（下标或切片）
a = [1, 2, 3, 4, 5]
print(a[2:4])

# 2_列表运算
# help的python的自省功能之一，可以查看python对象的帮助信息
help(list)
# + 列表合并，in 判断存在，* 复制，>==< 比较大小
a = [1, 2, 3]
print(a + [4, 5, 6])
print(4 in a)
print(a == [4, 5, 6])
print(a > [4, 5, 6])

# 3_列表方法（9种）
# append,count,extend,index,insert,pop,remove,reverse,sort
# 例子1：用列表方法模拟堆栈和队列
# 模拟堆栈（先进后出）
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())

# 模拟队列（先进先出）
queue = ['Eric', 'labour', 'lisa']
queue.append('Terrible')
queue.append('laught')
print(queue.pop(0))
print(queue.pop(0))
print(queue)

# 4_列表的内置函数（4种）
# range、filter、map、reduce
# range：生成一个整型序列
print(list(range(10)))
print(list(range(1, 10, 2)))

# filter：对列表进行过滤，只保留filter要求的元素
def f(x): return x % 2 != 0 and x % 3 != 0
list(filter(f, range(2, 25)))

# map：同时处理多个列表，但要求不同列表的元素个数一致
def add(a,b): return a+b
print(list(map(add,[1,2,3],[4,5,6])))

# reduce：对序列中的项迭代用f函数，如果有starting_value还可以作为初始值求和（这里显示错误）
def add(x,y): return x+y
# reduce(add,range(1,11),20)

# 5_列表推导式 （使用过滤和映射方法生成特定要求的列表）
# [<expr]