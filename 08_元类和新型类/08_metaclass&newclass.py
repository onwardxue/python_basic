# -*- coding:utf-8 -*-
# @Time : 2022/7/16 9:30 下午
# @Author : Bin Bin Xue
# @File : 08_metaclass&newclass
# @Project : python_basic

'''
    8.1 元类（非必选，需要的时候再看）
        元类是Python语言中的高级主题，可以认为类是元类的实例。

        8.1.1 类工厂（老版本中使用）
        8.1.2 初识元类
        8.1.3 设置类的元类属性
        8.1.4 元类的魔力
        8.1.5 面向方面(AOP)和元类
        8.1.6 元类的小结

    8.2 新型类
        8.2.1 新型类VS传统类
            继承object或其子类的都叫新型类，否则为传统类（现版本内置类基本都是新型类）

            建议：都使用新型类（现在版本新建的类都默认继承object）
                        使用issubclass(子类,父类)可查看某个类是否是另一个类的子类

        8.2.2 类方法和静态方法
            静态方法（方法上加@staticmethod）可以不用实例化，直接通过类名.方法调用（可不用加self）

        8.2.3 新型类的特定方法
            1.__new__和__init__方法
                __new__用来判断实例是否属于该类，然后分配内存生成实例对象（初始化实例前）
                    （接受一个类参数cls，返回一个类实例给__init__作初始化）
                __init__用来对类实例对象做初始化操作（初始化实例时）

                使用：__new__可以实现一个功能：让一个类只能实例化一次

            2.__getattribute__方法
                该方法由基类对象提供，负责实现对象属性引用的全部细节（在调用方法前调用）
                （可用该方法隐藏父类方法）

        8.2.4 新型类的特定属性
            property内建方法主要是将类方法的返回值转为属性
            语法：attribute = property(fget=None,fset=None,fdel=None,doc=None)
            - x是实例的话，当引用x.attrib时，x.attribute会调用fget方法取值；
                                      为x.attrib赋值时，调用fset()方法，且value值作为fset()方法的参数；
                                      当执行del x.attrib时，调用fdel；
                                      doc参数为该属性的文档字符串
                                      （若只定义fget属性，表示只读）

        8.2.5 类的super()方法
            使用super(子类,self).方法，调用父类方法可保证父类方法只被调用一次，不会重复

'''

print(issubclass(int, object))
print(issubclass(float, object))
print(issubclass(dict, object))
print(issubclass(list, object))


class C:
    pass


print(issubclass(C, object))

print('----------测试类方法和静态方法----------')
# class ClassA(object):
#     @staticmethod
#     def teststatic(aa):
#         print(aa)
#     def testnormal(aa):
#         print(aa)
#     def testnormal2(self,aa):
#         print(aa)

# 不实例化，直接用类名调用方法
# ClassA.teststatic(33)
# ClassA.testnormal(33)
# ClassA.testnormal2(33)  #出错，缺少参数

# 实例化，再调用方法
# in_A = ClassA()
# in_A.teststatic(33)
# in_A.testnormal(33) #出错，参数多了
# in_A.testnormal2(33)

print('----------__new__和__init__测试----------')
class C(object):
    def __new__(cls):
        print('this is C new method')
        return object.__new__(cls)

    def __init__(self):
        print('this is C init method')

cc = C()

print('----------__new__实现一个类只能生成一个实例----------')
class C(object):
    __objectpool={}
    def __new__(cls):
        if not cls in cls.__objectpool:
            cls.__objectpool[cls]=object.__new__(cls)
        return cls.__objectpool[cls]
x=C()
y=C()
print(id(x))
print(id(y))

print('----------__getattribute__----------')
class C(object):
    def test(self):
        print('this is test!')
    def __getattribute__(self,name):
        print('calling to '+name)
        return object.__getattribute__(self,name)

x=C()
x.test()

print('----------property方法----------')
# 使用property将方法的值转为属性area，自动计算面积值
class Rectangle(object):
    def __init__(self,width,height):
        self.width=width
        self.height = height
    def getArea(self):
        return self.width * self.height
    area = property(getArea,doc='area of thr rectangle')

