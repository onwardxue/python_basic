# -*- coding:utf-8 -*-
# @Time : 2022/7/15 2:48 下午
# @Author : Bin Bin Xue
# @File : 05_class&object
# @Project : python_basic

'''
5.1 面向对象
    类、对象（类的实例化）、继承、多态（同样的方法名/接口，根据不同的输入类型按不同的方式处理）

5.2 python类和对象
    1_类的定义：class ClassName(father class name):  <statement-1>..（类的成员=类的属性和方法）
                举例：class customer(object):
                                buy_dict={}
                                def buy(self,pro_name,price):
                                    self.buy_dict[pro_name]=price

                类的属性可以显式定义属性，也可以隐式定义属性：
                class test(object):
                # 显示定义
                    value=0
                    def  test2(self):
                        # 隐式定义（要加self）
                        self.value=0

                类方法的形参中第一个必须为self

    2_类的实例化：创建一个类的对象（调用类的方法必须先进行实例化）
                class Test(object):
                    value=0
                    def printf(self):
                        print(self.value)
                #实例化：
                a = Test()
                a.printf()

    3_类的方法：类的内部定义的函数，但第一个参数必须是self
        类方法的三条原则：
            （1）第一个参数必须是self
            （2）类方法里面调用类本身的属性和方法必须在前面加self
            （3）类的方法名开头必须为下划线或者字母
            （如果开头为两个下划线且结尾无两个下划线，为私有方法，只能类内其他方法使用）

        举例：
        class vipcust(object):
            def buy_some(self,prod_name,price):
                dist_price=self.__disct(prod_name,price)
                self.prod_dict[prod_name]=disct_price
            def __disct(self,prod_name,price):
                if prod_name=='苹果':
                    return prod_name*0.9
                elif prod_name=='桃子':
                    return prod_name*0.8
                else:
                    return price

    4_类的特殊方法：
        （1）类的初始化和析构函数：__init__和__del__（初始化和删除实例时会自动调用）
        class Test(object):
            def __init__(self):
                print(..)
            def __del__(self):
                print(..)
        aa = testA()
        del aa

        （2）类的操作符方法（用处不大）

    5_类的继承（泛化 ）
        语法：class <name>(superclass1,superclass2,):
        (1)单一继承（继承一个父类，自动获得父类的所有属性和方法）
            注：super()引用父类的方法（当子类中存在与父类相同的名字时使用）
        (2)多重继承（多个组合混到一起）

        重载（同名时，后类覆盖前类）：
            注：当存在多个父类时，加载顺序是从右往左（所以重载时，左边的会覆盖右边的）

    6_类的关联和依赖
        （1）依赖（依赖的类的某个方法以被依赖的类作为其参数）
            如：人过河需要船（过河这个函数就需要船这个类作为参数）
                class Person(object):
                        def gobyboat(self,boat):
                            boat.overriver()
                    class Boat(object):
                        def overriver(self):
                            pass
        （2）关联（关联关系一般是用一个类作为另一个类的成员属性）
            如：一个企业有n个员工（company类有属性employee）
                class employee(object):
                    id=0
                    name=' '
                class company(object):
                    def __init__(self):
                        self.employeer=employee()

        （3）聚合和组合（都是关联的特例，区别在于聚合的两个对象之间可分离）
            如：
            class A(object):
                pass
            class B(object):
                pass
            class C(object):
                a=A()
                b=B()
            class D(object):
                b=B()

            C中调用了A和B，所以C和A、B为组合关系，有A才有C。B又为D，所以B、C为聚合

'''

