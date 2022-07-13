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

print('-----------------3.6 列表-----------------')
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
def add(a, b): return a + b


print(list(map(add, [1, 2, 3], [4, 5, 6])))


# reduce：对序列中的项迭代用f函数，如果有starting_value还可以作为初始值求和（这里显示错误）
def add(x, y): return x + y


# reduce(add,range(1,11),20)

# 5_列表推导式 （使用过滤和映射方法生成特定要求的列表）
# [<expr1> for k in L if <expr2>]
a = [1, 2, 3, 4, 5]
print([k * 5 for k in a if k != 3])

print('-----------------3.7 元组-----------------')
# 3.7 元组（于list的不同点在于不能更改元素，不能用list9种方法，只支持比较运算和加乘运算
a = (1,2,3,4,5,6)
print(a[0])
b = a+(7,8)
print(b)
b = a*2
print(b)

print('-----------------3.8 字符串-----------------')
# 3.8 字符串（单引号、双引号-单行；三引号-多行）
# 1_大小写转换
str1 = 'this Is a test'
# 句子首字母大写，其他小写：capitalize
print(str1.capitalize())
# 全部转小/大：lower/upper
print(str1.lower())
print(str1.upper())
# 大小写互换：swapcase
print(str1.swapcase())
# 各单词首字母大写其他小写：title
print(str1.title())

# 2_字符串搜索
# find,rfind分别从左向右和从右向左查找，找不到时返回-1
# index找不到时返回异常
print(str1.find('this'))
print(str1.rfind('this'))
print(str1.find('ok'))
# print(str1.index('ok'))

# 3_字符串替换
# replace(替换)、strip(去掉头尾指定的字符)、rstrip(从右边开始)、lstrip(左边开始)、expandtabs(用空格取代tab键)
a = 'as12367    678'
print(a.replace('as','ddbb'))
print(a.strip('as'))
print(a.rstrip('78'))
print(a.lstrip('78'))
print(a.expandtabs(1))

# 4_字符的分割
# split根据指定的字符把一个字符串截断成列表
# splitlines()将一个字符串根据换行符'\n'截断成列表
a = '1,2,3,4'
b = '123\n456\n789'
print(a.split(','))
print(b.splitlines())

# 5_字符串判断功能
# startwith，判断一个字符串是否以某个字符串为开头
# endwith，判断一个字符串是否以某个字符串为结尾
# isalnum，判断是否由数字和字符组成
# isdigit，判断是否全由数字组成
# isalpha，判断是否全由字母组成
# isspace，判断是否由空格符组成
# islower，判断是否全是小写
# isupper，判断是否全是大写
# istitle，判断是否首字母是大写

print('-----------------3.9 字典-----------------')
# 3.9 字典类型 - {key:value}
# 要点：key的类型只能是常量（数值、元组、字符串）；key的值唯一
# 1_字典创建
# 直接通过映射创建
fruit = {1:'apple', 2:'orange', 3:'pear'}
# 使用dict类
# 空字典
fruit = dict()
print(fruit)
# 映射类型组生成dict
a = {1:'one',2:'two',3:'three'}
b = dict(a)
print(b)
# 通过序列容器生成队列
t = dict([(1,'one'),(2,'two')])
print(t)
# 通过输入方法的参数（name=value）（这种创建方法有些限制，不是很好）
r = dict(one=1,two=2,three=3,four=4)
print(r)

# 2_字典操作
# key值作为下标访问value
print(a[2])
# dict只支持等于和非，不支持比较大小
print(a == b)
print(a != b)
# 清空字典
print(a.clear())
# 删除字典某一项（从尾删除，返回被删除的键值）
print(b.pop(1))
print(b.popitem())
# 迭代器访问
for k in b.items(): print(k)
for k in b.keys(): print(k)
for k in b.values(): print(k)

print('-----------------3.10 集合-----------------')
# 3.10 集合类型（无序存放且不能重复，分为可变集合和不可变集合）
# 1_创建集合
# 可变集合
a = set([1,2,3])
# 不可变集合
b = frozenset([1,3,2])
print(a,b)

# 2_集合方法和运算
# 并(union或|)、交(intersection或&)、差(difference或-)、补(symmetric_difference或^)、判断子集(issubset()或<=)
a = {1,2,3,4}
b = {4,5,6,7}
print(a.difference(b),a-b,a|b,a&b,a^b,a>=b)




