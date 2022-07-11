# -*- coding:utf-8 -*-
# @Time : 2022/7/11 9:31 下午
# @Author : Bin Bin Xue
# @File : 02_python_basic
# @Project : python_basic

# 2.1.1 启动python解释器
# pycharm中的python控制台有'>>>'符号就表示已经启动解释器

if __name__ == '__main__':
    # 2.1.2 数值类型（整型、浮点型、复数）
    a = 3
    b = 3.246
    c = 5 + 1j
    print(a,b,c)
    # 1.分别赋值
    a,b,c = 3,3.246,6+1j
    print(a,b,c)
    # 2.连续复制
    a=b=c=4.2
    print(a,b,c)

    print('————————————————————')
    # 2.1.3 字符串
    bb = 'china'
    print(bb)
    # 1.分行（在行结尾加反斜杠标识延续到下一行，\n标识换行）
    hello = '    这是第1行\n\
    这是第2行\n\
    这是第3行\
    结束。'
    print(hello)
    # 2.三引号字符串注释多行
    hello = '''欢迎来到我的github，
    努力学习，赚更多钱！
    '''
    print(hello)
    # 3.用upper/lower转换字符串大小写
    str = 'Money'
    print(str.upper()+'\n',str.lower())

    # 4.下标索引字符串（配合切片）
    word = 'Arrested'
    print(word[3],word[2:6],word[2:])

    # 5.注意：字符串不可改变
    # word[3] = 'p' 会报错

    # 6.字符串合并
    word1 = 'h'+word[1:]
    print(word1)

    print('————————————————————')
    # 2.1.4 列表
    # python为容器，中括号之间用逗号分割的一系列值
    aa = ['china', 2, 3, 4, 2*2, ]
    print(aa)

    # 1.列表可以改变元素值
    aa[2] = aa[2] + 23
    print(aa[2])

    # 2.列表可以切片和改变大小
    aa[0:2] = [1,12]
    print(aa)
    aa[:0] = aa
    print(aa)

    