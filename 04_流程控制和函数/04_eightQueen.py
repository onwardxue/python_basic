# -*- coding:utf-8 -*-
# @Time : 2022/7/14 10:16 下午
# @Author : Bin Bin Xue
# @File : 04_eightQueen
# @Project : python_basic

'''
    八皇后算法（回溯法实现：逐步尝试各种可能，失败就返回上一步，直到条件达成）

    注意：八皇后问题共有92种解法，书中的方法并不能给出所有解法

    - 思路：(1)从第一列开始，为皇后找到安全位置，然后跳到下一列
                (2)如果在第n列出现死胡同，并且列为第一列，那么棋局失败，否则后退到上一列，再进行回溯
                (3)如果在第8列上找到了安全位置，那么棋局成功

'''

def setdanger(chess,x,y):
    for col in range(len(chess)):
        for row in range(len(chess[0])):
            if col==x:
                chess[col][row] += 1
            elif row == y:
                chess[col][row]+=1
            elif col+row==x+y:
                chess[col][row]+=1
            elif col-row==x-y:
                chess[col][row]+=1
            else:
                pass

def erasedanger(chess,x,y):
    for col in range(len(chess)):
        for row in range(len(chess[0])):
            if col == x:
                chess[col][row]-=1
            elif row==y:
                chess[col][row]-=1
            elif col+row==x+y:
                chess[col][row]-=1
            elif col-row==x-y:
                chess[col][row]-=1
            else:
                pass

def judgedanger(chess,x,y):
    if chess[x][y] == 0:
        return True
    else:
        return False

def judgecol(chess,col):
    for row in range(len(chess[col])):
        if judgedanger(chess,col,row):
            break
        else:
            return False
    return True

def tryqueen(chess,col,flag,result):
    flag=True
    if col== 8:
        print(result)
        result=[]
        flag=False
    else:
        if judgecol(chess,col):
            for row in range(len(chess[col])):
                if judgedanger(chess,col,row):
                    print('安全'+str(col)+':'+str(row))
                    setdanger(chess,col,row)
                    result.append((col,row))
                    tryqueen(chess,col+1,flag,result)
                    if flag==False:
                        erasedanger(chess,col,row)
                        result.pop()
        else:
            flag = False

if __name__ == '__main__':
    chess = [[0 for x in range(8)] for x in range(8)]
    result = []
    flag = True
    tryqueen(chess,0,flag,result)
