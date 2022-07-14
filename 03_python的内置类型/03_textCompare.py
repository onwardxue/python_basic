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

'''
    存在问题：这里调整了书中的代码，改用直接读取文件，改后有点问题，运行出来会显示多一个b
'''

# 文件读取操作（创建文件类，使用文件类方法进行读取）
# open_file=open(filename)
# file_txt=open_file.read()

# python标准库optparse模块用来读取命令行参数，并作解释
# optparse使用三个步骤：
# (1) import optparse
# (2) parser = optparse.OptionParser()
# (3) 添加参数选项：parser.add_option('-f','--file',action='store',type='string',dest='filename',default='./')
# (4) 解释命令行：(options,args) = parser.parse_args()
# 解释命令行参数解析后，就可以直接访问options来得到命令行的参数值
# print(options.filename)

# if __name__=='__main__'为python文件的主要入口，用来集成其他的模块，完成一个完整的程序
import optparse
import sys


# 单词统计（将句子划分成单词；字典的键为单词，值为词频）
def wordcount(readtext):
    dict = {}
    readlist = readtext.split()
    for every_word in readlist:
        if every_word in dict:
            dict[every_word] += 1
        else:
            dict[every_word] = 1
    return dict


# 文本比较功能（先将两个文本划分成行；逐行划分成单词进行比较）
def testcmp(sText, dText):
    cmpList = []
    sLineList = []
    # 文本按行划分，并去掉空格行或空值行
    for line in sText.splitlines():
        if not line.isspace() and line != '':
            sLineList.append(line)
    dLineList = []
    for line in dText.splitlines():
        if not line.isspace() and line != '':
            dLineList.append(line)
    # 获取行数
    sLen = len(sLineList)
    dLen = len(dLineList)
    # 逐行切分为单词列表进行比较（如果有文本到达末尾，则用''补充行内容）
    for step in range(max(dLen, sLen)):
        sWordList = dWordList = []
        try:
            sWordList = sLineList[step].split()
        except IndexError as e:
            print('sfile is  end')
            sLineList.append('')
        try:
            dWordList = dLineList[step].split()
        except IndexError as e:
            print('dfile is  end')
            dLineList.append('')
        # 若单词列表不同，则添加到列表cmp中（行号、文本1该行内容，文本2该行内容）
        if sWordList != dWordList:
            cmpList.append((step+1, sLineList[step], dLineList[step]))

    return cmpList


if __name__ == '__main__':
    # 通过命令行参数方法读取文件
    # parser = optparse.OptionParser()
    # parser.add_option('-s', '--sFile', action='store', type='string', dest='sFileName')
    # parser.add_option('-d', '--dFile', action='store', type='string', dest='dFileName')
    #
    # (options, args) = parser.parse_args()
    path_1 = 'a.txt'
    path_2 = 'b.txt'
    sFile = open('a.txt', 'rb')
    dFile = open('b.txt', 'rb')

    # with open(options.sFileName, 'r') as sFile, open(options.dFileName, 'r') as dFile:
    # 开始统计文件
    # sText = sFile.read()
    # dText = dFile.read()
    # print('文件 %s' % options.sFileName)
    # print('词汇总数：%d' % len(wordcount(sText)))
    # print('各词频统计：%d' % wordcount(sText))
    #
    # print('文件 %s' % options.dFileName)
    # print('词汇总数：%d' % len(wordcount(dText)))
    # print('各词频统计：%d' % wordcount(dText))
    #
    # # 文本比较
    # cmpList = testcmp(sText, dText)
    # for diff in cmpList:
    #     print('%s %s: %s' % (options.sFileName, diff[0], diff[1]))
    #     print('%s %s: %s' % (options.dFileName, diff[0], diff[2]))

    sText = sFile.read()
    dText = dFile.read()
    print('文件 %s' % path_1)
    print('词汇总数：%d' % len(wordcount(sText)))
    print('各词频统计：')
    mydict_1 = wordcount(sText)
    for x in mydict_1.items():
        print('%s : %d' % (x[0], x[1]))

    print('文件 %s' % path_2)
    print('词汇总数：%d' % len(wordcount(dText)))
    print('各词频统计：')
    mydict_1 = wordcount(dText)
    for x in mydict_1.items():
        print('%s : %d' % (x[0], x[1]))

    # 文本比较
    cmpList = testcmp(sText, dText)
    for diff in cmpList:
        print('文件名：%s 行号：%s: 该行内容：%s' % (path_1, diff[0], diff[1]))
        print('文件名：%s 行号：%s: 该行内容：%s' % (path_2, diff[0], diff[2]))
