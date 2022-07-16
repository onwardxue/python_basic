# -*- coding:utf-8 -*-
# @Time : 2022/7/16 8:16 下午
# @Author : Bin Bin Xue
# @File : 07_module&package
# @Project : python_basic

'''
    7.1 模块
        注意：导入模块时要注意当前目录的位置（os.getcwd() 能获取当前目录的位置）

        7.1.1 Python模块
            一个.py文件就是一个模块，要使用模块中的方法或属性要用import导入该模块

        7.1.2 导入模块
            导入模块的四种写法：
            （1）'import' mymodule 'as' my（按模块名称导入，并起别名），导入多个：import sys,mymodule as my
            （2）'from' mymodule 'import' module_value,printvalue（用这种方式不能使用模块的名字，可以直接使用import后面所导入的名字）
            （3）'from' mymodule 'import' '(module_value,printvalue)'（这种方式与第二种一致，只是多加了括号）
            （4）'from' mymodule 'import' * （这种方式一次性导入模块下的所有成员，调用时可直接用成员名使用）

        7.1.3 查找模块
            查找模块的顺序：（1）当前目录（2）环境变量PYTHONPATH中查找（若没有则到安装目录查找）
            python查找目录：sys.path可以查看

        7.1.4 模块编译
            .py文件在运行时，会生成.pyc文件，进一步优化会生成.pyo文件

    7.2 包
        7.2.1 Python包
            包是一组模块的集合，所以包就是一个存放若干.py文件的目录，并且在该目录下有一个__init__.py文件（包的初始化文件），
        可以在该文件里导入包里的所有模块（__all__属性是包的重要属性，用来存放包下面模块名称，在初始化文件中设置就可以
        不用import导入了）

        7.2.2 包的导入
            包的导入和模块的导入是一样的语法规则，不同点在于from mypackage importlib * 这种形式：
            （1）若导入的包中的__init__.py有定义__all__，则将__all__指定的包导入模块
            （2）若导入的包中的__init__.py没有定义__all__，则将按其命名空间导入，若其为空文件，则不导入任何模块

        7.2.3 内嵌包
            一个大的包里面套着若干个子包，每个子包里面套着若干个子包。子包即为内嵌包，每个包功能不一样。

            注意：同一个大包下的内嵌包要调用另一个内嵌包的模块时，要使用如下方法导入：
                import etree. ElementTree（包.模块）
                from etree import ElementTree（from 包 import 模块）

'''
# 设置当前路径为Python的系统路径，并将路径加入到环境变量中
import sys, os, importlib

sys.path.append(os.getcwd())
importlib.reload(sys)

# 导入自定义模块
import mymodule

if __name__ == '__main__':
    print('----------调用模块----------')
    print(mymodule.module_value)
    mymodule.printvalue()
    print('----------查看要查找的目录信息----------')
    print(sys.path)

