friends = ["Wilson", "Mike", "Nelson", "Greg", "Jimmy"]
friends.append("Aaron") #附加
friends.append("Milly")
friends.append(15.0)
my_lost_friend = friends.pop()
print(friends)
print(my_lost_friend)

x = [1,2,3,4,5,6]
y = x.copy()
y[0] = 15
print(x)
print(y)

x = [1,2,3,4,5,6]
y = x #y指向x指向RAM
y[0] = 15
print(x)
print(y)
print(x[len(x)-1])

person = {"name": "Wilson", "age": 25} #dictionaries
print(person["name"])

person = {"x": {"age": [10, 20, 30]}}
print(person["x"]["age"][2]) #指引age里的第三个数字

x = {} #定义x为dictionary
x['name'] = "Grace"
x["age"] = 26
print(x)

x = {'name': 'Grace', 'age': 26}
print(x.keys()) #loop

x = {'name': 'Grace', 'age': 26}
print(x.values())
print(x.items()) #something like a list of tuples
print(x['name']) #objects

myTuple = (10, "100", "Hello")
print(myTuple)

x = 10, 15, 17, 100 # tuple packing
print(x)
print(type(x))

x = ("Wilson", 25)
name, age = x
print(name)
print(age) #variable names have meaning

x = 25
y = 35
temp = x #temp = 25
x=y # x = 35
y = temp # y = 25
print(x)
print(y)

x = 25
y = 35

x, y = y, x
# tuple.packing
# tuple. unpacking
print(x)
print(y)

a = ([1,2,3], "Wilson") # dictionary key? No
a[0][1] = 100
print(a) 
# if an element in a tuple is mutable, then we can just select the element, and then change it.
# if we want to use a tuple as a dictionary key, then all elements in the tuple has to be immutable.

# 15 ---integer, can be a key of dictionary
# 'Bob' ---string, can be a key
# ('Tom, [14, 23, 27]) --- [list] is mutable, can not be a key
# ['filename', (15, 16)] ---[list] is mutable, can not be a key
# "filename" ---string, can be a key
# ("filename", 25, "extension") ---(tuple), every element inside is string or integer, can be a key

myset = set({1,2,3})
print(myset)

mylist = [1, 4, 3, 2, 5, 1, 5]
myset = set(mylist)
print(myset)

s = set()
s.add(1)
print(s)
s.add(2)
print(s)
s.add(3)
s.discard(1)
print(s)
s.clear
print(s)

a = {1, 3, 4, 5}
b = {3, 4, 7, 8}
print(a.difference(b)) # A-B
print(b.difference(a)) # B-A
print(a.intersection(b)) #交集
print(b.intersection(a))
print(a.union(b)) #并集
print(b.union(a))

x = True
print (x)

x = 3 + 4j
y = 5 - 7j
print(x + y)

def hello(): #hello is stored in RAM
    print("hello")

print(hello) # print the location of "hello" in RAM
print(hello())

myList = ["a", "b", "c", "d"]
myString = "|".join(myList)
print(myString)
myString = " and ".join(myList)
print(myString)

# sort a list
x = [4, 2, 3, 1]
y = sorted(x) # without modifying the original one
print("the list x is", x, ".Also,the list y is", y)
y = sorted(x, reverse = True) # keyword arguments
print("the list x is", x, ".Also,the list y is", y)

# sort a tuple
x = (4, 2, 3, 1)
y = sorted(x)
print(x)
print(y)

# sort a dictionary
x = {"name": "Wilson", "age":25}
y = sorted(x)
print(x)
print(y) # output keys of the dictionary

# sort a set (unordered collection of unique objects)
x = {4, 5, 3, 2, 1}
y = sorted(x)
print(x)
print(y)

# "in or not in" operation
a = "ABCD"
if "A" in a:
    print("A is in", a)

a = ("A", "B", "C")
if "A" in a:
    print("A is in", a)