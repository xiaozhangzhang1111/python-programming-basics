# Control Flow
# If statement
from sys import argv
if True:
    print("This is so true!!")
else:
    print("This is false.")

# age<8 for free; >= 8 & 65 for $300; >= 65 for half
age = 5
if age < 8:
    print("Movie is free for you!!")
elif 8 <= age < 65:
    print("You need to pay $300!")
else:
    print("You only need to pay $150!")

if (5 > 3) and []:  # [] is falsy value
    print("the condition is true")
else:
    print("the condition is false")

k = True
if k == True:
    print("Variable k is True")
else:
    print("Variable k is false")

# program asks user's name
# cash
# Y/N
# program checks if the user has more than or equal
# name = input("Enter your name: ")
# Detailed Breakfast Program is included in try.py

# For & While Loop
# For Loop: we know how many times the loop should run
# for variable in iterable:
#    do something here
for letter in "Hello World":
    if (letter == letter.upper()):  # capital letter of the string
        print(letter)

# list
myList = [1, 3, 5, 7, 9]
for num in myList:
    print(num ** 2)

# a list of tuples
for tuple in [(1, 2), (3, 5), (5, 7)]:
    print(tuple[0] + tuple[1])
# the other way
for a, b, c in [(1, 2, 5), (3, 5, 9), (5, 7, 7)]:
    print(a + b + c)

# dictionary (keys)
myDictionary = {"name": "Wilson", "age": 25}
for item in myDictionary.values():
    print(item)
for item in myDictionary.items():
    print(item)
for key, value in myDictionary.items():
    print(f"The key is {key}")
    print(f"The value is {value}")

# set
for i in {1, 3, 5, 7, 9}:
    print(i)

# While Loop: we want loop to break based on a condition
x = 0
while x < 5:
    print(x)
    x += 1  # we must write this line of code, or it will unlimited loop

# Nested Loop
counter = 0
for i in "1234":
    for j in "abcd":
        print(i, j)  # 4 * 4 = 16
        counter += 1
print(f"counter is now {counter}")

# Pass, Break, Continue
for i in "How are you?":
    # some codes go here
    pass  # when a statement is required syntactically, but we do not want any command or code
print("hello")

if True:
    pass
else:
    print("hello")

# function


# def hello()
# ....pass

# Break
print("Before the for loop")
for i in "123456789":
    if i == "5":  # True
        break
    else:
        print(i)
print("After the for loop")

# break in the nested loop
for i in "1234":
    for j in "abcdefg":
        if j == "c":
            break
        else:
            print(i, j)

# Continue
for i in "ABCD":
    if i == "B":  # force to execute the next loop, the loop included "continue" will be skipped
        continue
    print(i)

for i in "ABCDE":
    print("Now the current i is " + i)
    continue
    # the code under the "continue" will not be executed
    print("Here is the line after continue")

# Range function
for i in range(5):  # range() function returns an iterable object
    print(i)

for i in range(20, 15, -1):
    print(i)

# typecasting to List
myList = list(range(0, 15, 2))  # 不建议的用法，过多占用RAM
print(myList)

# Enumerate & Zip Function
counter = 0
for letter in "How are you today?":
    if counter < 10:
        print(letter)
    counter += 1

for counter, char in enumerate("How are you today?"):
    if counter < 10:
        print(char)

# Zip
x = [1, 2, 3]
y = ['A', 'B', 'C']
z = ['a', 'b', 'c', 'c']
for tuple in zip(x, y, z):
    print(tuple)

# comprehensive
# general expression
x = [1, 2, 3, 4]
squared_x = []  # list, dict, set
for item in x:
    squared_x.append(item ** 2)
print(squared_x)

# List Comprehensions
# new_list = [operation for variable in original_list optional_(if condition)]
# For example
x = [1, 2, 3, 4]
squared_x = [item ** 2 for item in x]
print(squared_x)
# new_dict = {key: value(operation) for variable in original_dict if contidion}
x = [1, 2, 3, 4]
x_squared_dict = {item: item ** 2 for item in x if item > 2}
print(x_squared_dict)

# Set Comprehensions
# new_set = {operation for variable in original_set if condition}
x = [1, 2, 3, 4]
x_squared_set = {item ** 2 for item in x if item > 2}
print(x_squared_set)

# Generator Comprehensions
x = [1, 2, 3, 4]
x_squared_generator = (item ** 2 for item in x)
print(x_squared_generator)
for i in x_squared_generator:
    print(i)

# this is how we get command line arguments
print(argv)
