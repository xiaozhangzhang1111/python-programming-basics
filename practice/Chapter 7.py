import myPackage
import sys
from try4 import hello1
from try3 import hello1  # 覆盖了try4的hello1()
from try4 import hello1 as hello2  # 解决被覆盖的问题
from random import randint  # 直接从random里引用randint方法也可以
from random import *  # 可以引用random里所有的function
import random as rd  # random作为一个name比较长module，每次使用都要写太杂乱
import random
from myPackage.sub_package import hello
from myPackage import some_code, some_more_code
from try2 import one_func, two_func


# def hello():
#     print("this is a hello")


# one_func()
# hello()
# two_func()

# from myPackage import some_code, some_more_code
# from myPackage.sub_package import hello
some_code.some_code()
some_more_code.here_is_some_more()
hello.small_hello()

print(random.randint(0, 5))
print(rd.randint(0, 5))  # 只需引入rd即可
print(randint(0, 5))
hello1()  # 结果产生try3的hello1()
hello2()  # 结果产生try4的hello1()
# print(sys.path)
# import __builtins__ #__builtins__ module is also an object
# 内置模块，包含所有的内置函数，异常，类型等
x = "This is a string."
print(__builtins__.len(x))

# print(dir(__builtins__))#列出所有内置名称

# print(globals())  # return global namespace as a dictionary
# 查看当前全局作用域中所有变量，函数和类的命令


def hello3():
    x = 5
    print(locals())  # 内置函数，返回当前局部作用域的所有变量及其值的字典
    print("hello3")


hello3()  # 返回'x':5。因为当前只有变量5

# if _name_=="_main_"详见one.py & two.py
# 模块直接运行时，name的值为main
# 模块被倒入时，name的值为模块的名称
