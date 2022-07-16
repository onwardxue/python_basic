# -*- coding:utf-8 -*-
# @Time : 2022/7/16 4:48 下午
# @Author : Bin Bin Xue
# @File : 06_guessNumber
# @Project : python_basic

'''
    计算机猜数（不仅要实现该功能，因为涉及到与用户的交互操作，还要用异常处理方法保证健壮性）

    问题描述：自己先确定一个4位数（不能重复且为0），让计算机猜这个4位数字是多少。
                    每次计算机给出结果后，给出两个提示：1)4位数字中有几位猜对；2)对的数
                    字中有几个位置也是正确的，将这两个数字输入到程序中给计算机以提示，
                    让计算机再猜，直到猜对为止

    需求分析：具体来说，就是列出所有可能的范围，根据提示信息不断缩小范围
            计算机猜测的步骤为：
                    （1）按要求创建一个符合要求的数字列表（4位数共有4536种可能）
                    （2）初始随机给一个四位数给用户做比较（几个数字正确，几个数字和位置都正确）
                    （3）根据提示，将可能性列表与随机列表比较相同的数字，去除不符合条件的，缩小可能性列表范围
                    （4）根据第二个提示，将可能性列表与随机列表比较相同位置的个数，继续缩小范围
                    （5）重复步骤（2）-（4），只能可能性列表的长度为1或者用户输入True为止

    问题：这里还是存在一些问题，异常处理部分还是不够完整
'''

import random


class TComputer(object):
    def __init__(self):
        self.possibleList = []
        for num in range(1000, 10000):
            if len(set(list(str(num)))) == 4:
                self.possibleList.append(num)
                self.randomNum = random.choice(self.possibleList)

    def getUserInput(self, hasNum, posNum):
        self.hasNum = hasNum
        self.posNum = posNum
        self.reduceList()

    def reduceList(self):
        self.reduceByHasNum()
        self.reduceByLocation()
        self.randomNum = random.choice(self.possibleList)

    def reduceByLocation(self):
        subList = []
        for possibleNum in self.possibleList:
            randomNumList = list(str(self.randomNum))
            possibleNumList = list(str(possibleNum))
            samePostion = 0
            for i in range(4):
                if randomNumList[i] == possibleNumList[i]:
                    samePostion += 1
            if samePostion == self.posNum:
                subList.append(possibleNum)
        self.possibleList = subList[:]

    def reduceByHasNum(self):
        subList = []
        for possibleNum in self.possibleList:
            randomNumList = list(str(self.randomNum))
            possibleNumList = list(str(possibleNum))
            if len(set(randomNumList) & set(possibleNumList)) == self.hasNum:
                subList.append(possibleNum)
        self.possibleList = subList[:]


# 定义异常类
class BusiError(Exception):
    pass


class UserInputError(BusiError):
    def __init__(self, err_input, out_info):
        self.errInput = err_input
        self.errInput = out_info


class UserDataError(BusiError):
    pass


if __name__ == '__main__':
    computer = TComputer()
    print('计算机：准备猜数？')
    while 1:
        print('计算机：%s' % computer.randomNum)
        value = input('人：')
        if value == 'yes':
            print('计算机：bingo')
            break
        elif len(value.split()) > 2:
            raise UserInputError(value,'应该输入OK或者是2个数字')
        elif (not value.split()[0].isdigit())|(not value.split()[1].isdigit()):
            raise UserInputError(value,'输入的必须是2个数字')
        elif(int(value.split()[0]) <= int(value.split()[1]))&int(value.split()[0])>4:
            raise UserInputError(value,'输入的数字必须在[0,4]之间，并且第一个数字要大于第二个数字')
        else:
            hasNum = int(value.split()[0])
            posNum = int(value.split()[1])
            computer.getUserInput(hasNum,posNum)

