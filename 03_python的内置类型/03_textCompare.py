# -*- coding:utf-8 -*-
# @Time : 2022/7/13 10:04 下午
# @Author : Bin Bin Xue
# @File : 03_textCompare
# @Project : python_basic

'''
实现功能：对两个英文文档进行统计，得到两个英文文档使用了多少单词，每个单词的
                  使用频率，并对两个文档进行比较，返回有差异的行号和内容

需求分析：
    统计功能：统计总词汇数和每个词汇的词频（使用字典的键存放单词，值存放词频）
    比较功能：比较两个文本的差异，忽略空格和空行的影响（将文本分成一行一行的按行处理，将字符串里的有效字符转成列表）
'''


# 单词统计
def wordcount(readtext):
    dict = {}
    readlist = readtext.split()
    for every_word in readlist:
        if every_word in dict:
            dict[every_word] += 1
        else:
            dict[every_word] = 1
    return dict

# 文本比较功能
def testcmp(sText,dText):
    cmpList = []
    sLineList = []
