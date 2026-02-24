# Simple Exercise I
# Q1
import math


def printMany():
    for i in range(1, 101):
        print(i)


printMany()

# Q2


def printEvery3():
    for i in range(1, 89, 3):
        print(i)


printEvery3()

# Q3


def position(string):
    # enumerate function
    for num, s in enumerate(string):
        if s == s.upper():
            return (s, num)
    return -1  # 如果不加此句将returns None (default result)


print(position("abcd"))  # returns -1
print(position("AbcD"))  # returns ('A', 0)
print(position("abCD"))  # returns ('C', 2)
# 或者另一个写法


def position(string):
    # enumerate function
    for num, s in enumerate(string):
        if s == s.upper():
            print(s, num)
            return (s, num)
    print(-1)
    return -1


position("abcd")  # returns -1
position("AbcD")  # returns ('A', 0)
position("abCD")  # returns ('C', 2)

# Q4


def findSmallCount(lst, num):
    counter = 0
    for ele in lst:
        if ele < num:
            counter += 1
    return counter


print(findSmallCount([1, 2, 3], 2))  # returns 1
print(findSmallCount([1, 2, 3, 4, 5], 0))  # returns 0
print(findSmallCount([1, 2, 3, 4, 5], 100))  # returns 5

# Q5


def findSmallerTotal(lst, num):
    result = 0
    for ele in lst:
        if ele < num:
            result += ele
    return result


print(findSmallerTotal([1, 2, 3], 3))  # returns 3
print(findSmallerTotal([1, 2, 3], 1))  # returns 0
print(findSmallerTotal([3, 2, 5, 8, 7], 999))  # returns 25
print(findSmallerTotal([3, 2, 5, 8, 7], 0))  # returns 0

# Q6


def findAllSmall(lst, num):
    result = []
    for ele in lst:
        if ele < num:
            result.append(ele)  # 附加
    return result


print(findAllSmall([1, 2, 3], 10))  # returns [1, 2, 3]
print(findAllSmall([1, 2, 3], 2))  # returns [1]
print(findAllSmall([1, 3, 5, 4, 2], 4))  # returns [1, 3, 2]

# Q7


def summ(lst):
    result = 0
    for ele in lst:
        result += ele
    print(result)
    return result


summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # returns 55
summ([])  # return 0
summ([-10, -20, -30])  # return -60

# Simple Exercise II
# Q1


def stars(n):
    # for loop
    for i in range(1, n+1):  # i goes from 1, 2, ..., n。range的区间是左闭右开
        print("*" * i)


stars(1)  # returns *
stars(3)

# Q2


def stars2(n):
    # 1， 2， 3， 4，..., n
    for i in range(1, n+1):
        print("*" * i)
    # n -1, n-2, ..., 1
    for i in range(n-1, 0, -1):  # 这里 range(n-1, 0, -1) 表示从 n-1 递减到 1，步长-1
        print("*" * i)


stars2(3)
# returns
# *
# **
# ***
# **
# *

# Q3


def table(n):
    # n x i (1 - 9)
    for i in range(1, 10):
        print(f"{n} x {i} = {n * i}")


table(10)

# Q4


def table9to9():
    # nested loop
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")


table9to9()

# Q5


def swap(string):
    result = ""
    for letter in string:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    print(result)
    return result


swap("Aloha")  # returns "aLOHA"
swap("Love you.")  # returns "lOVE YOU."

# Q6


def findMin(lst):
    if len(lst) == 0:
        print("undefined")
        return "undefined"

    min_element = lst[0]
    for ele in lst:
        if ele < min_element:
            min_element = ele
    print(min_element)
    return min_element

    # set the index 0 element to be the min element
    # for loop, in each iteration
    # if the element is less than my current min element
    # if yes, then change my min element
findMin([1, 2, 5, 6, 99, 4, 5])  # returns 1
findMin([])  # returns "undefined"
findMin([1, 6, 0, 33, 44, 88, -10])  # returns -10

# Intermediate Exercise I
# Q1


def findMin(lst):
    if len(lst) == 0:
        return "undefined"
    result = lst[0]
    for ele in lst:
        if ele < result:
            result = ele
        return result


def mySort(myList):
    result_list = []
    while len(myList) > 0:
        min_element = findMin(myList)
        result_list.append(min_element)
        myList.remove(min_element)
    print(result_list)
    return result_list


mySort([17, 0, -3, 2, 1, 0.5])  # returns [-3, 0, 0.5, 1, 2, 17]

# Q2
# prime（质数）只能整除自己和1，1不是prime
# test if 2,3,4,5,...,n-1 can divide n


def is_prime(n):
    if n == 1:
        print("False")
        return False

    starter = 2
    while starter < n:
        if n % starter == 0:
            print("False")
            return False
        starter += 1
    print("True")
    return True


is_prime(1)  # returns false
is_prime(5)  # returns true
is_prime(91)  # returns false
is_prime(1000000)  # returns false

# Q3 palindrome意思是一个词正着读和反着读都一样（回文）
# solution 1
# bearaeb
# 0123456


def palindrome(string):
    # 通过math.floor向下取整，例如对于5个字符的字符串，检查前2个字符
    for i in range(0, math.floor(len(string)/2)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


print(palindrome("bearaeb"))  # true
print(palindrome("Whatever revetahW"))  # true
print(palindrome("Aloha, how are you today?"))  # false

# solution 2
# left += 1   right -= 1
# stop while loop when left is bigger than right


def palindrome2(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


print(palindrome("bearaeb"))  # true
print(palindrome("Whatever revetahW"))  # true
print(palindrome("Aloha, how are you today?"))  # false

# Q4


def pyramid(n):
    space = n - 1  # 初始化空格数量
    star = 1  # 初始化型号数量
    for i in range(n):
        print(space * ' ' + star * '*')
        star += 2
        space -= 1


pyramid(4)

# Q5
# solution 1


def inversePyramid(n):
    space = 0
    stars = 2*n - 1
    for i in range(n):
        print(space * ' ' + stars * '*')
        space += 1
        stars -= 2


inversePyramid(4)

# solution 2


def inverse_pyramid(m):
    result = []

    def pyramid(n):
        space = n - 1
        star = 1
        for i in range(n):
            result.append(space * ' ' + star * '*')
            star += 2
            space -= 1
    pyramid(m)
    result.reverse()  # 反转列表得到倒金字塔
    for line in result:  # 逐行打印
        print(line)


inverse_pyramid(3)

# Q6


def has_33(lst):
    result = False
    for i in range(len(lst) - 1):
        if lst[i] == 3 and lst[i + 1] == 3:
            result = True
    return result


print(has_33([1, 5, 7, 3, 3]))  # True
print(has_33([]))  # False
print(has_33([4, 3, 2, 1, 0]))  # False

# Q7


def spyGame(lst):
    string = '007'  # 要查找的模式
    pointer_for_lst = 0  # 列表指针
    pointer_for_string = 0  # 字符串指针
    while pointer_for_lst < len(lst):
        if lst[pointer_for_lst] == int(string[pointer_for_string]):
            pointer_for_string += 1  # 每找对一个，字符串指针+1
            print(pointer_for_string)  # 显示匹配过程
            if pointer_for_string == len(string):  # 指针达到字符串长度
                return True
        pointer_for_lst += 1  # 列表指针+1
    return False
# 列表指针始终递增，而字符串指针只在匹配成功的时候才递增，所以列表中的数字是单向遍历的，不会回头重复使用


print(spyGame([1, 2, 4, 0, 3, 0, 7]))  # True
print(spyGame([1, 2, 5, 0, 3, 1, 7]))  # False

# Intermediate Exercises II
# Q1


def factorPrime(n):
    answer = str(n) + " = "  # 初始化结果字符串，如”120 = “
    # if n cannot be divided by 2,
    # then n cannot be divided by any multiples of 2
    p = 2  # 从最小的质数2开始尝试
    while (p <= n):  # 当尝试的质数不超过n时循环
        if n % p == 0:  # 如果n能被p整除
            answer += str(p) + " x "  # 将p加入结果字符串
            n /= p  # 将n除以p，继续分解
        else:
            p += 1  # 如果不能被p整除，尝试p+1
    return answer[:len(answer) - 3]  # 通过slicing切掉多余的“ x ”


print(factorPrime(120))  # returns "2 x 2 x 2 x 3 x 5"

# Q2
# solution 1


def my_intersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))


print(my_intersection([1, 3, 4, 6, 10], [
      5, 11, 4, 3, 100, 144, 0]))  # returns [3, 4]

# solution 2


def my_intersection(lst1, lst2):
    result = []
    for ele1 in lst1:
        for ele2 in lst2:
            if ele1 == ele2:
                result.append(ele1)
    return result


print(my_intersection([1, 3, 4, 6, 10], [
      5, 11, 4, 3, 100, 144, 0]))  # returns [3, 4]

# Q3
result = []


def flatten(lst):  # 压平，把所有的element都变单调
    for i in lst:
        if type(i) == type([]):
            flatten(i)
        else:
            result.append(i)
    return result


print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
# returns [1, 2, 0, 1, 3, 1, 3, 3, 4, 1, 2]
