# -*- coding:utf-8 -*-
# @Time : 2022/7/17 6:30 下午
# @Author : Bin Bin Xue
# @File : 09_threeVector
# @Project : python_basic

'''
    9.1 迭代器和生成器
        9.1.1 迭代器
            支持迭代的结构（必须有__iter__()和next()，前者返回迭代器自身，后者返回下一个元素）

            遍历方式：（自定义的next和__iter__）
            （1）a=lis(num)
                     a.next()
            （2）list_a=lis.__iter__()
                    for i in list_a

        9.1.2 生成器
            1_使用yield定义一个生成器函数，而不是普通函数（数据提供者）
            2_yield n的功能分为两个部分：
            （1）将n返回给用户
            （2）进入wait_and_get方法状态，程序暂时暂停，在用户调用next()时才激活

            3_遍历方法（非自定义的next方法）
                a=infinite()
                next(a)

            4_yield和next()方法
                yield是表达式。
                当用户调用next()方法时，执行到yield时，先返回值再进入wait状态，
            只有当再有next()方法时才会恢复，继续执行下面的代码，一直执行到
            下一个yield代码。如果没有yield，调用next()，就会报StopIteration异常

            5_生成器的send(msg)方法
                恢复生成器运行，并将发送的值成为当前的yield表示式的返回值。
            程序恢复后会继续执行下面的代码，直到遇到yield停下，如果没有遇到
            则报异常。（wait_and_get负责检测send信息）
                调用send方式，如：g.send(n)
                注意：第一个只能使用next()或send(None)

            6_生成器的throw()方法
                从生成器内部自主抛出一个异常
                a.throw(异常名)

            7_关闭生成器
                close()方法关闭，关闭后再使用next()会报错

            8_生成器的用途（yield类似于return返回一个值，但会暂停，直到调用next方法）
            （1）相对于列表、元组、生成器更节省内存
                    list要存储变量，生成器一次只存取一个
            （2）线性遍历访问数据
                    将非线性化的处理转为线性化的，典型的例子是二叉树的访问

    9.2 修饰器
        9.2.1 修饰器模式
            是JAVA里的概念，为了在不改变源代码的基础上进行增减
        9.2.2 Python修饰器
            python语法支持Decorator模式（注解）
            不带参数的形式：
                @A                      @A
                def f():  ...            @B
                -> f = A(f)          @C
                                            def f():...     ->f=A(B(C(f)))
            带参数的形式：
                @A(args)    ->  _deco = A(args)
                def f()     ->          f = _deco(f)

        9.2.3 修饰器函数的定义
            第一种调用对应的'修饰'函数，如：
            def A(func):
                def new_func(*args, **argkw):
                    result = func(*args, **argkw)   #调用原函数进行处理，得到结果
                    #对结果进行处理
                    if result:
                        #做一些额外的工作，使用新的结果替换原来结果
                        return new_result
                    else:
                        return result
                return new_func
            @A
            def f(args):pass

            第二种调用对应的函数，如：（该形式将返回一个新的修饰_A，根据指定参数）
            def A(arg):
                def __A(func):
                    def new_func(args):
                        #做一些额外的工作
                        return func(args)
                    return new_func
                return _A
            @A(arg)
            def f(args):pass

        9.2.4 修饰器的应用
            修饰器的作用就是在不改变源代码的情况下，对函数进行加工，且可以
        叠加多层（应用场景如对不同级别用户设置不同权限，如下面的测试样例）

'''

if __name__ == '__main__':
    print('创建支持迭代的类')


    class simple_range(object):
        def __init__(self, num):
            # num<=0表示迭代结束
            self.num = num

        def __iter__(self):
            return self

        def next(self):
            if self.num < 0:
                raise StopIteration
            tmp = self.num
            self.num -= 1
            return tmp


    a = simple_range(5)
    print(a.next())
    print(a.next())
    print(a.next())
    print(a.next())
    print(a.next())
    print(a.next())

    print('定义一个无限数据生成器')


    def infinite():
        n = 1
        while 1:
            yield n
            n += 1


    ge = infinite()
    print(next(ge))
    print(next(ge))
    print(next(ge))
    print(next(ge))

    print('生成器send方法测试')


    # 结论是send先返回值，再找下一个yield
    def test():
        print('step 1')
        x = yield 1
        print('step 2', 'x=', x)
        x = yield 2
        print('step 3', 'x=', x)


    g = test()
    next(g)
    g.send(5)
    # g.send(9)

    print('使用生成器计算闰年')


    def getyear(start, end):
        for i in range(start, end + 1):
            if i % 4 == 0 and i % 100 != 0:
                # yield == return
                yield i
            elif i % 400 == 0:
                yield i


    year_gen = getyear(1900, 2000)
    print(next(year_gen))
    print(next(year_gen))
    print(next(year_gen))
    print(next(year_gen))

    print('使用修饰器模式给不同用户设置不同访问权限')


    # 权限类（放不同权限的方法（加工函数））
    class Permission:
        def __init__(self):
            pass
        # 普通用户的修饰函数
        def needUserPermission(self, function):
            def new_func(*args, **kwargs):
                obj = args[0]
                if obj.user.hasUserPermission():
                    ret = function(*args, **kwargs)
                else:
                    ret = 'No User Permission'
                return ret
            return new_func()
        # 管理员的修饰函数
        def needAdminPermission(self, function):
            def new_func(*args, **kwargs):
                obj = args[0]
                if obj.user.hasAdminPermission():
                    ret = function(*args, **kwargs)
                else:
                    ret = 'No Admin Permission'
                return ret
            return new_func

    class UserService:
        def newUser(self, name):
            self.name = name
            return self

    # 实际业务类
    class Action:
        def __init__(self,name):
            self.user = UserService.newUser(name)
        @Permission.needUserPermission
        def listAllPoints(self):
            return 'TODO: do real list all points'
        @Permission.needAdminPermission
        def setup(self):
            return 'TODO: do real setup'



    action = Action('user')
    print(action.listAllPoints())
    print(action.setup)
