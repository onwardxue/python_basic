# -*- coding:utf-8 -*-
# @Time : 2022/7/15 9:13 下午
# @Author : Bin Bin Xue
# @File : 06_exceptCap&throw
# @Project : python_basic

'''
    6.1 异常处理
        6.1.1 Traceback异常信息
            当代码发生异常而没有指定异常处理的方法时，会暂停程序，返回异常信息
            如：（除数为0的异常 - ZeroDivisionError）
            Traceback包含3个部分：信息头、出错位置、异常信息
        6.1.2 捕获异常
            try:
                statements 1
            except A:
                statements 2
            如果statements 1 发生了异常，将把异常类型和A作比较，一样则执行statement2
            注：捕获异常可以放在发生异常的地方，也可以放在方法调用的里面

        6.1.3 多重异常处理
            try:
                statements 1
            except (ExceptionType1,ExceptionType2):
                statements 2
            except (ExceptionType3,ExceptionType4):
                statements 3
            except:
                statements 4
            注：except后面什么也不带表示发生任何异常都按此处理

            在except后面接else和finally：
                else：只有当try中的语句没有发生异常时才会执行else的语句
                finally：无论是否产生异常都要执行的语句
            注：finally语句会显示在异常信息前面

        6.1.4 异常的参数
            直接使用异常中的参数信息进行返回
            try:
                statements 1
            except (ExceptionType) as e:
                print(e)

        6.1.5 内置异常类型
            BaseException类查看（包含30多种）
            6个主要类如下：
            （1）LookupError下的IndexError和KeyError
                    IndexError - 访问列表中不存在的元素
                    KeyError - 访问字典不存在的Key时
            （2）IOError - 文件不存在或其他IO问题
            （3）NameError - 访问一个不存在的变量名称时
            （4）TypeError - 类型不匹配问题
            （5）Attribution - 当访问一个对象不存在的属性时
            （6）ZeroDivisionError - 当被除数是0的时候抛出的异常

        6.1.6 抛出异常（主动）
            raise自定义选择当程序在某种情况下，抛出设置的异常
            3种常用方法：
            （1）raise后接实例化对象
                    raise NameError('aa')
            （2）raise后接异常类名
                    raise NameError
            （3）raise后接异常类和类的初始化参数
                    raise NameError('aa')

        6.1.7 自定义异常类型
            class MyError(Exception):
                def __init__(self,value):
                    self.value = value
                def __str__(self):
                    return repr(self.value)
            注：要继承Exception类
            总异常类：当一个较大的程序时，需要使用多级异常类
            如：class BusiError(Exception):
                        '程序异常错误信息总类'
                    class UserInputError(BusiError):
                        '用户输入信息错误,id是窗口或输入框的编号，
                        value是用户输入信息，reason是原因'
                        def __init__(self,id,value,reason):
                            self.id=id
                            self.value=value
                            self.reason=reason
                    class InnerdealError(BusiError):
                        '内部逻辑错误，参数为发生模块类型，模块名字，模块行数'
                    调用：
                    try:
                        statement1
                    except (BusiError) as obj_e:
                        if type(obj_e).__name__=='UserInputError':
                            statement2
                        elif type(obj_e).__name__=='InnerdealError':
                            statement3
                    注：当不知道具体异常时，可以使用基类捕获，再根据对象类型名定位


'''

if __name__ == '__main__':
    print('----------单异常处理----------')
    def calcnum(li, divnum):
        try:
            new_list = [divnum / one for one in li]
        except ZeroDivisionError:
            print('列表中有0')


    calcnum([4, 5, 6, 8, 0, 2], 3)

    print('----------多异常处理----------')
    try:
        a = []
        print(a[1])
        b = 1 / 0
        c = {}
    except IndexError:
        print('访问了不存在的列表元素')
    except ZeroDivisionError:
        print('被除数为0')
    except KeyError:
        print('访问了不存在的列表key值')

    print('----------except后面无类型----------')
    try:
        a = []
        print(a[1])
        b = 1 / 0
        c = {}
    except:
        print('出现了错误')

    print('----------except后面接else和finally----------')
    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print('division by zero!')
        else:
            print('result is %f', result)
        finally:
            print('executing finally clause')
    divide(2, 1)
    divide(2,0)
    # divide('1','2')

    print('----------异常参数----------')
    try:
        a=[]
        print(a[1])
    except(IndexError) as e:
        print(e)

    print('----------抛出异常----------')
    # raise NameError('aa')

    print('----------自定义异常类----------')
    class MyError(Exception):
        def __init__(self,value):
            self.value = value
        def __str__(self):
            return repr(self.value)
    try:
        raise MyError(2*2)
    except (MyError) as e:
        print('My exception occurred,value:', e.value)
