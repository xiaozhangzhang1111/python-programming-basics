# I/O with Files in Python
import shelve
import pickle
import os
file = open("myFile.txt")
print(file.read(5))  # 只读前5个元素，得到“roses”
print("----------")
print(file.read(5))  # seek右移5格，得到“ are ”
print(file.read())  # 读接下来的整份文件
print(type(file.read()))  # file.read returns a string
print("----------")
print(file.read())  # 之前已经读完了，所以不再有显示
print("----------")
file.seek(0)  # 又重新从0开始
print(file.read())
print("----------")
file.seek(0)
print(file.readlines())  # "\n"指的是空格
print("----------")
file.seek(0)
for line in file.readlines():  # 一行一行的打印，中间有空格分开
    print(line)
print("----------")
file.seek(0)
print(file.readline())  # 读第一行
print(file.readline())  # 读第二行
print("----------")
file.seek(0)
while True:
    line = file.readline()
    if not line:  # line == ""
        break
    else:
        print(line)
file.close
print("----------")

# with Statement and Open() Function
with open("myFile2.txt", mode="r") as my_file:
    all_content = my_file.read()
    print(all_content)

with open("myFile2.txt", mode="w") as my_file:
    my_file.write(
        "Learning python is so fun.\nLearning JavaScript is so fun as well\n")
# 另一种做法，encoding默认为utf-8可以不写
with open("myFile2.txt", "w", -1, "utf-8") as my_file:
    my_file.write(
        "Learning python is so fun.\nLearning JavaScript is so fun as well\n")

# Deleting Files & Folders
# os.remove("index.html")  # os unlink functionality
# os.rmdir("newfolder")  # folder里有文件时不能直接删除，输出error
# 解决办法1.os.walk() to travel through the folder
# 2. shutil-shell utility(与电脑核心交谈的通道)

# User Input-另有try1.py
# user_input = input("How old are you?")
# user_address = input("Where do you live?")
# print("-------------------")
# print(user_input)
# print(type(user_input))

# Secret Game(Guess Number)-另有secret.py
# import random
# secret = random.randint(1, 100) # generate a random integer from 1 to 100
# min_value = 1
# max_value = 100
# while True:
#     input("Make your guess(between (min_value) and (max_value)): ")

# Tic Tac Toe Game (圈叉棋盘游戏)
# 1. Display the grid
# 2. Accept user input
# 3. Update the game grid
# 4. Game win-checking algorithm
# 5. Improving game mechanism

# Serialize & Deserialize
# 两台电脑之间会有一个medium连接来传输数据
# 除了已有的dataset，也可以自己创造一个dataset，如book
# book——(serialization)——>binary——(deserialization)——>book

# Pickle & Shelve
# pickle是内建module，可以直接做serialize和deserialize
# in pickle, we use open() with rb(read binary) and wb(write binary)

# import pickle （用于对象序列化和反序列化）
x = 10
y = [1, 2, 3, 4]
with open("pickle_file", "wb") as p_file:  # 二进制写模式打开pickle_file
    pickle.dump(x, p_file)  # 写入第一个对象：整数 10
    pickle.dump(y, p_file)  # 写入第二个对象：列表[1，2，3，4]

with open("pickle_file", "rb") as p_file:  # 二进制读模式打开pickle_file
    print(pickle.load(p_file))
    print(pickle.load(p_file))

# import pickle
x = 10
y = 100
my_list = [1, 2, 3, 4, 5, 9]


def save_data():
    global x, y, my_list
    data = {'x': x, 'y': y, "my_list": my_list}
    with open("my_pickle_file", 'wb')as pfile:
        pickle.dump(data, pfile)


save_data()

# import pickle
x = None
y = None
my_list = None


def restore_data():
    global x, y, my_list
    with open("my_pickle_file", "rb") as pfile:
        data = pickle.load(pfile)
        x = data['x']
        y = data['y']
        my_list = data['my_list']


restore_data()
print(x, y, "my_list")

# Pickle has a security problem, make sure only load the pickle files from trustworthy sources!

# import shelve
integers1 = [1, 2, 3, 4, 5, 6]
integers2 = [6, 7, 8, 9, 10]
integers3 = [100, 101, 102, 103]

with shelve.open("shelf-example", 'c') as shelf:
    shelf['ints1'] = integers1
    shelf['ints2'] = integers2
    shelf['ints3'] = integers3
with shelve.open("shelf-example", 'r') as shelf:
    for key in shelf.keys():
        print(key)
    print(shelf['ints2'])
