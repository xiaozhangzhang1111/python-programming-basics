# Object-Oriented Programming
# 物件导向程序设计
# A class is a code template for creating objects
class Robot:  # 创造一个Robot的模版
    pass


my_robot = Robot()
print(type(my_robot))
# The naming convention of class name is always capitalize the first letter

# __init__() & Method


class Robot:
    # in classes, we can also define doctring
    """ Robot class is for creating robots"""
    # contructor
    ingredient = "metal"

    def __init__(self, name, age):  # self表示class（类）的当前实例（实例就是根据class设计出来的实物）
        self.name = name  # self.name是variable,跟name没有关系
        self.age = age

    def walk(self):  # 定义method
        print(f"{self.name} is walking...")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours. ")

    # def greet(self):
    #     print(
    #         f"Hi, my name is {self.name}, and I am made of {self.__class__.ingredient}")
    @staticmethod  # 静态方法，不用"self"
    def greet():
        print("A robot says hi...")


my_robot_1 = Robot("Wilson", 25)
my_robot_2 = Robot("Grace", 26)
my_robot_2.walk()
my_robot_1.sleep(15)
print(my_robot_1.__doc__)
print(my_robot_1.name)
print(my_robot_1.age < my_robot_2.age)

print(my_robot_1.ingredient)
print(Robot.ingredient)  # 不推荐，以防以后需要修改class name时需要修改很多东西
print(my_robot_1.__class__.ingredient)
# my_robot_1.greet()
# my_robot_2.greet()
my_robot_1.__class__.greet()


class Circle:  # 定义一个Circle类，创建圆形对象
    """This class creates circle"""
    pi = 3.14159  # 类属性，所有圆共享的pi值
    all_circles = []  # 类属性，一个列表，存储所有创建的Circle实例

    def __init__(self, radius):
        self.radius = radius  # 实例属性，每个圆的半径
        self.__class__.all_circles.append(self)  # 将新实例添加到类属性列表里

    def area(self):  # 计算单个圆的面积
        return self.__class__.pi * (self.radius ** 2)

    @staticmethod
    def total_area():
        total = 0
        for circle in Circle.all_circles:  # 直接引用Circle类，circle是Circle类的某个实例
            total += circle.area()
        return total

    @classmethod  # 第一个参数是类本身（cls）
    def total_area2(cls):
        total = 0
        for circle in cls.all_circles:  # 通过cls参数访问类属性
            total += circle.area()
        return total


c1 = Circle(10)
print(c1.area())  # 普通方法，通过实例调用
print(c1.__class__.total_area())  # 通过static方法
print(c1.__class__.total_area2())  # 通过cls方法

print("-----------")

# inheritance继承


class People:  # 定义People基类
    def __init__(self, name, age):  # 初始化方法，创建实例时自动调用
        self.name = name  # 将传入的name赋给实例
        self.age = age

    def sleep(self):  # 定义实例方法sleep
        print(f"{self.name} is sleeping...")

    def eat(self):
        print(f"{self.name} is eating food")


class Student(People):  # 定义子类Student，继承People里所有的method
    def __init__(self, name, age, student_id):  # 子类的初始化，重写了_init_，添加了student_id参数
        # People.__init__(self, name, age)
        # 调用父类的初始化方法，设置name和age属性
        super().__init__(name, age)  # 用super（）替换People，不需要再写self
        self.student_id = student_id  # 创建Student类的实例student_one

    def eat(self, food):  # 重新定义覆写从父类继承的method
        print(f"{self.name} is now eating {food}")  # 增加了一个food


student_one = Student("Wilson", 25, 100)
print(student_one.age, student_one.student_id)  # （继承自People类，Student特有）
student_one.sleep()  # 调用从People类继承来的sleep方法
student_one.eat("beef")

# Multiple Inheritance从不止一个父类调用method

# simple example


class C:
    def do_stuff(self):
        print("hello from class C")


class D:
    def do_another_stuff(self):
        print("hello from class D")


class A(C, D):
    pass


a = A()
a.do_stuff()
a.do_another_stuff()

print("-----------")
# complicated example


class E:
    pass


class F:
    def do_stuff(self):
        print("doing stuff fom F")


class G:
    def do_stuff(self):
        print("doing stuff fom G")


class B(E, F):
    pass


class C:
    def do_stuff(self):
        print("doing stuff fom C")


class D(G):
    pass


class A(B, C, D):
    pass


a = A()
a.do_stuff()
# print(A.mro()) 寻找order的method
# print(A.__mro__) 另一种方法

print("--------")
# Private Attributes and Methods


class Robot:
    def __init__(self, name):
        self.name = name  # 公开属性
        self.__age = 25  # 私有性，private property

    def greet(self):
        print(f"Hi, I am {self.__age} years old.")
    # # getter, setter

    def get_age(self):
        return self.__age

    def set_age(self):
        self.__age += 1
    # private method
    # __name_(前面两个_,后面一个_就自动识别private)

    def __this_is_private(self):
        print("Hello from private method.")

    def greeting(self):
        print("Hi, I am a robot")
        self.__this_is_private()


my_robot = Robot("Wilson")
print(my_robot.get_age())
my_robot.greet()
my_robot.greeting()

# my_robot.__this_is_private()输出error，不能直接调用private method

print("--------")
# OOP Style in Python
# info hiding--encapsulation


class Robot:
    def __init__(self, name):
        self.name = name
        self.__age = 25  # __age初始化为25

    def age_setter(self, new_age):  # 设置器方法
        if new_age > 0 and new_age < 100:
            self.__age = new_age
        else:
            print("New age setting is invalid")

    def age_getter(self):  # 对私有属性__age的获取方法
        print(self.__age)


my_robot = Robot("Wilson")  # 创建实例“Wilson”
my_robot.age_setter(-30)  # 尝试设置年龄-30
my_robot.age_getter()

# property decorator (虚拟的property)

# 传统封装方式


class Employee:
    def __init__(self):
        self.income = 0
        self.__tax = 0  # 私有属性存储计算结果

    def earn_money(self, money):  # 调用earn money来更新收入
        self.income += money
        self.__tax = self.income * 0.05

    def get_tax(self):
        return self.__tax  # 必须通过调用get_tax方法来获取tax值


wilson = Employee()
wilson.earn_money(300)
print(wilson.get_tax())

wilson.earn_money(500)
print(wilson.get_tax())

print("-------")
# 节省RAM，使用虚拟property方法
# 不存储，每次访问时动态计算


class Employee:
    def __init__(self):
        self.income = 0

    def earn_money(self, money):
        self.income += money  # 只更新收入

    @property  # 动态计算税收，不存储，将方法伪装成属性
    def tax_amount(self):
        return self.income * 0.05

    @tax_amount.setter
    def tax_amount(self, tax_number):
        self.income = tax_number * 20  # 通过税收反向设置收入


wilson = Employee()
wilson.earn_money(300)
print(wilson.tax_amount)
wilson.tax_amount = 200
print(wilson.income)
# tax_amount is not a real property(virtual), read only

# The Mighty Hash Function
# A hash is a function converts one value to another

a = 100
b = "This is just a string"  # 有意义
c = 1.0
d = True
e = None
print(hash(a), hash(b), hash(c), hash(d), hash(e))

print(hash((1, 4, 7, 11)))  # 能做hash的：integer,set,string,tuple
print("--------")
# returns fixed—size integer
# hash()里的值必须是immutable
# good hash function:
# 1.Consistent
print(hash("Hello"))
print("Doing other stuff")
for i in range(10):
    pass
print(hash("Hello"))
# 不论执行几次hash，结果都一样
print("--------")
# 2.Distributed Evenly
# 3.Not invertible，不可逆
print(hash("Look at me!"))
print(hash("Look at me!!"))
print(hash("Look at me!!!"))
# input只有微小的不同，但output差别很大，避免hash colision
# 不可用output反推input，用于网络加密安全
print("--------")

# __hash__() function
# any object that implements the hash function can be used as a key for dictionary


class Robot:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    # define a private method__key()

    def __key(self):  # 私有方法（前缀双下划线）
        return (self.name, self.age, self.address)  # 返回包含对象关键属性的元祖
    # implement __hash__() function

    def __hash__(self):
        return hash(self.__key())  # 使用内置hash函数计算__key（）返回值

    def __eq__(self, other):  # 定义两个robot实例的相等性比较
        if isinstance(other, Robot):  # 检查other是否是Robot实例
            return self.__key() == other.__key()  # 如果是，比较两者的__key()返回值
        return NotImplemented  # 如果不是，返回NotImplemented

    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.age == other.age  # 定义年龄相等为True
        return NotImplemented

    def __len__(self):
        return self.age

    def __str__(self):
        return f"{self.name} is now {self.age} years old, living in {self.address}"

    def __repr__(self):  # 常用于debug
        return f"name: {self.name}, age: {self.age}, address: {self.address}"

    def __add__(self, other):
        if isinstance(other, Robot):
            return self.age + other.age
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Robot):
            return self.age > other.age
        return NotImplemented


robot1 = Robot("Wilson", 25, "Windsor")  # 创建实例robot
dictionary = {robot1: "Wilson"}  # 使用实例作为字典的key
print(dictionary[robot1])  # 通过robot成功检索到Wilson

robot2 = Robot("Wilson", 25, "Windsor")
print(robot1 == robot2)  # 输出True。虽然是不同的对象，但是哈希值相同，字典认为他们是一个key
# 如果不实现__eq__，则会比较对象ID（内存地址），结果则为False
robot3 = Robot("Grace", 25, "Toronto")
robot4 = Robot("Jason", 27, "Windsor")
print(robot1 == robot3)
print(len(robot1))
print(robot1)  # 输出和str()的一样
print(str(robot1))
print(repr(robot1))
print(robot1 + robot2)
print(robot4 > robot1)
print(gt(robot4, robot1))

# Dunder or Magic Methods
# 前后都有两个底线的叫Dunder
# obj1==obj2会去寻找是否有__eq__
