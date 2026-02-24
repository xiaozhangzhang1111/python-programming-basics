# Naming Restriction
# variable name should begin with a letter or an underscore
# _player_1 or player_1 is OK, NO 1_player
# Variable names are case-sensitive, 大小写要一致
# Module name: all lowercase, use_if necessary(instead of camelCase)
formal_name = "Wilson"
formalName = "Wilson"  # camelcase
nickName = "Will"
# Function name: all lowercase, use_if necessary
# Variable name: all lowercase, use_if necessary
# Class name Capitalized, Camelcase
# Constants: ALL CAPITALIZED, use_if necessary
# Comparison: No need for ==, just do if my_var, if not my_var
haveBudget = True
if haveBudget == True:
    print("Buy house")
else:
    print("Don't buy houses.")

not_have_budget = False
if not not_have_budget:
    print("buy a house")
else:
    print("Don't buy a house.")

# Pythonic
# original way
a = 10
b = 5
temp = a
a = b
b = temp
print(a, b)

# Pythonic way
a = 10
b = 5
c = 20
a, b, c = b, c, a  # Pythonic
print(a, b, c)

# get_user_id(id) returns a tuple(name, age)
# info = get_user_id(id)
# print("The user name is " + info[0])
# print("The user age is" + info[1])

# name, age = get_user_id(id)
# print("The user name is " + name)
# print("The user age is" + age)

b = 50
if b > 10 and b < 100:
    print("b is in the range of 10 and 100.")

# original coding
cmd = input("Give a command: ")
if cmd == "cd" or cmd == "dir" or cmd == "echo":
    print("valid command")
else:
    print("invalid command")

# pythonic coding
cmd = input("Give a command: ")
# membership operator
if cmd in ('dir', 'cd', 'echo'):
    print("valid command")
else:
    print("invalid command")
