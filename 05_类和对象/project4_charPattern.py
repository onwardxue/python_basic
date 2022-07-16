# -*- coding:utf-8 -*-
# @Time : 2022/7/15 7:30 下午
# @Author : Bin Bin Xue
# @File : 05_charPattern
# @Project : python_basic

'''
    自动打印字符图案
    -   实现一个小程序，实现将数字字符串的每一个字符在一个9*9的空间里用*来模拟出数字的样子（计算机中数字显示）

    需求分析：
        这个小功能实际上包含三个部分：将数字字符串拆分成字符，字符转成图案，将图案组合起来打印

    程序设计：
            这个程序一共有13个类，其中10个是数字类，继承于数字图案总类，工厂类负责根据数字串成数字类对象，
    而图案打印类负责接受输入，然后组合输出的数字类表进行打印

    实现出来还有点问题：打印格式不对
'''


# 1_数字图案总类
# 属性：图案列表
# 方法：添加*行列()、完成图案列表()、画行()、画竖()
class numpic(object):
    def __init__(self):
        self.pic_list = [[' ' for i in range(9)] for x in range(9)]

    def setpos(self, i, j):
        self.pic_list[i][j] = '*'

    def draw(self):
        return self.pic_list

    def drawline(self, line):
        for step in range(9):
            self.setpos(line, step)

    def drawrow(self, row, row_type):
        if row_type == 0:
            for step in range(9):
                self.setpos(step, row)
        elif row_type == 1:
            for step in range(5):
                self.setpos(step, row)
        else:
            for step in range(4, 9):
                self.setpos(step, row)


# 2_十个数字类
class onepic(numpic):
    def draw(self):
        self.drawrow(8, 0)
        return self.pic_list


class zeropic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 0)
        self.drawline(8)
        self.drawrow(8, 0)
        return self.pic_list


class twopic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(8, 1)
        self.drawline(4)
        self.drawrow(0, 2)
        self.drawline(8)
        return self.pic_list


class threepic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(8, 0)
        self.drawline(4)
        self.drawline(8)
        return self.pic_list


class fourpic(numpic):
    def draw(self):
        self.drawrow(0, 1)
        self.drawline(4)
        self.drawrow(8, 0)
        return self.pic_list


class fivepic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 1)
        self.drawline(4)
        self.drawrow(8, 2)
        self.drawline(8)
        return self.pic_list


class sixpic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 0)
        self.drawline(4)
        self.drawrow(8, 2)
        self.drawline(8)
        return self.pic_list


class sevenpic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(8, 0)
        return self.pic_list


class eightpic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 0)
        self.drawrow(8, 0)
        self.drawline(4)
        self.drawline(8)
        return self.pic_list


class ninepic(numpic):
    def draw(self):
        self.drawline(0)
        self.drawrow(0, 1)
        self.drawrow(8, 0)
        self.drawline(4)
        return self.pic_list

# 3_工厂类（生产对象的工厂：接收传进来的数字字符串，返回生成的对象）
class numfact(object):
    def factory(self,which):
        if int(which)==0:
            return zeropic()
        elif int(which)==1:
            return onepic()
        elif int(which)==2:
            return twopic()
        elif int(which)==3:
            return threepic()
        elif int(which)==4:
            return fourpic()
        elif int(which)==5:
            return fivepic()
        elif int(which) == 6:
            return sixpic()
        elif int(which)==7:
            return sevenpic()
        elif int(which)==8:
            return eightpic()
        elif int(which)==9:
            return ninepic()

# 4_图案打印类
class picprint(object):
    def __init__(self):
        self.list_total=[[] for x in range(9)]

    def getprinstr(self,string):
        self.num_str=string

    def __unionpic(self,prc_list):
        for step in range(9):
            self.list_total[step]+=[' ',' ']+prc_list[step]

    def printstr(self):
        num_fact=numfact()
        print_str=' '
        for eve_char in self.num_str:
            num_obj=num_fact.factory(eve_char)
            self.__unionpic(num_obj.draw())
            print_str=' '
            for sub_list in self.list_total:
                for every_char in sub_list:
                    print_str+=every_char
                print_str+='\n'
        print(print_str)


if __name__ == '__main__':
    string = input('请输入数字字符串(如98761)：')
    print_str = picprint()
    print_str.getprinstr(string)
    print_str.printstr()




