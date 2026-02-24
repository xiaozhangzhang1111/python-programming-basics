myList = [1, 2, 3, 4]
myList.insert(2, 10)
# help(myList.insert)  可以查看function作用

# Def keyword


def sayHi():
    print("Hello, how are you?")


sayHi()  # function execution, invokation


def addtion(x, y):  # x, y are the parameter
    print(x + y)


addtion(15, 35)  # 15, 35 are the arguments(给定的值)

a = 30
b = 25


def addtion(x, y):
    print(x + y)


addtion(a, b)  # arguments can be variables as well.

# difference between global variables, local variables
a = 5  # global variable


def f1():
    x = 2  # f1 function's local variable
    y = 3  # f1 function's local variable
    print(x, y, a)


def f2():
    x = 10  # f2 function's local variable
    y = 17  # f2 function's local variable
    print(x, y, a)


f1()
f2()
# print(x, y) 会出现x, y are not defined

a = 10

# parameters (inputs)are local variables in the function


def change(num):  # num = a (copy by value) => num = 10
    num = 25


change(a)
print(a)  # 无法改变global variable，最后结果还是10因为copy by value

# function with list
a = [1, 2, 3, 4]


def change(lst):  # lst = a (copy by reference)=> lst = [1, 2, 3, 4]
    lst[0] = 100  # a = [100, 2, 3, 4]


change(a)
print(a)

# can we change any copy by value global variables?


def change(num):
    global a
    a = 25


change(a)
print(a)


# def myAddition(a, b):
#     """This function does addtion for inputs a and b"""
#     print(a + b)
# help(myAddition)

# Return Keyword
# def myAddition(a, b):
#     print(a + b)
# print(myAddition(10, 18)+myAddition(26, 19)+myAddition(15, 17))
# NoneType不可以和NoneType相加
def myAddition(a, b):
    return a + b  # 返回两个数的和


result1 = myAddition(10, 18)
result2 = myAddition(26, 19)
result3 = myAddition(15, 17)
print(result1 + result2 + result3)

# evaluate
# python playground(sandbox)


def myAddition(a, b):
    result = a + b  # 计算得到25
    print(result)  # print25输出到终端
    return result  # 返回25给函数调用处
    # 让函数对外输出一个值，而print只是在终端显示内容


myAddition(10, 15)  # 没有print返回值


def myAddition(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 4:
                return  # 无返回值，None
            print(i, j)


print(myAddition(10, 15))

# positional arguments


def exponent(a, b):
    return a ** b


print(exponent(2, 3))  # 8
print(exponent(3, 2))  # 9 a和b位置不能对调

# keyword arguments
print(exponent(b=2, a=10))

myList = [4, 6, 3, 2, 1]
print(sorted(myList, reverse=False))  # 默认升序排序，True为降序

# default argument


def sum(n1=10, n2=0):
    return n1 + n2


print(sum(18))  # n1被18覆盖

# Arbitrary number of arguments


def sum(*args):  # 允许函数接受不限数量的位置参数（非关键字参数），并把他们打包成一个元祖tuple
    result = 0
    for number in range(0, len(args)):  # 遍历args元祖的索引
        print(f"We are now at number {number}.")
        print(f"Also, args[number] is {args[number]}.")
        result += args[number]  # 累加每个参数
        print(f"Now, the result is {result}")  # 每次打印结果
    return result  # 返回总和


print(sum(43, 22, 18, 3, -5, 44, -1000))


def myfunc(**kwargs):
    print("{} is now {} years old.".format(kwargs["name"], kwargs["age"]))


myfunc(name="Wilson", age=25, address="Hawaii")


def myfunc(*args, **kwargs):  # 同时使用args和kwargs时注意顺序
    print("I would like to eat {}{}".format(args[2], kwargs["food"]))


myfunc(14, 17, 23, "Hello", name="Wilson", food="eggs")

# 1 normal argument (p1, p3)
# 2 default argument
# 3 *args
# 4 **kwargs


def func(p1, p2, p3="three", *args, **kwargs):
    print("...")
    print(p1, p2, p3, args, kwargs)


func(1, 2, 3, 4, 5, x=1, y=3)
func(1, 2, 3, 4, x=4)
func(1, 2, 3, 4)
func(1, 2, 3)
func(1, 2)
# func(1) 会显示missing 1 required positional argument

# Higher-Order Function


def square(num):
    return num ** 2


myList = [-10, 3, 9, 8, 10]
for item in map(square, myList):
    print(item)


def even(num):
    return num % 2 == 0


    # if num % 2 == 0:
    #     return True
    # else:
    #     return False
myList = [444532, 3211543, -998432, 66154]
for item in filter(even, myList):
    print(item)

# Lambda variable: operation
result = (lambda x: x ** 2)(5)
print(result)

myTuple = (lambda x, y: (x + y, x-y))(15, 30)
print(myTuple[0])
print(myTuple[1])


for item in map(lambda x: x**2, [15, 10, 5, 0]):
    print(item)

for item in filter(lambda x: x % 2 == 0, [15, 10, 5, 0]):
    print(item)

# Scope
name = "Wilson"


def greet():
    name = "Grace"

    def hello():
        print("Hello, my name is " + name)

    def hello2():
        print("greeting from hello2.")
        hello2()
    hello()


# name的指向更改
greet()

name = "Wilson"


def greet():
    name = "Grace"
    hello()


def hello():
    print("Hello, my name is " + name)


greet()

# Bonus Assignment
# a = "hello"


# def change():
#     print(a)  # Python created "a" local variable
#     a = 2  # a variable assignment


# change()

# a = "hello"


# def change(x):
#     if x:
#         a = "We just changed a"  # variable assignment
#     print(a)


# change(False)

def addtion(a, b):
    return a + b


def subtraction(a, b):
    return a - b


addtion = subtraction
print(addtion(10, 5))

str = "This is my string"
x = 25
print("hello" + str(x))

