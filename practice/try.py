# Chapter 3
# Breakfast Program
name = input("Enter your name: ")  # string
print("your name is " + name)

money = input("Enter your cash amount: ")  # string
hungry = input("Are you hungry? (Y/N) ")  # string
if hungry == "Y":
    if int(money) >= 30:
        # f-string can analyze the content of {}
        print(f"{name} should go eat breakfast.")
    else:
        print(f"{name} is hungry but might not have enough money to buy breakfast.")
elif hungry == "N":
    if int(money) >= 30:
        print(f"{name} has budget but doesn't want to eat breakfast.")
    else:
        print(f"{name} has no money but is not hungry.")
else:
    print("Please make sure that you enter either Y or N.")

# if-elif => switch ==, >, <, >=, <=
# 不一定要使用switch
name = input("Enter your name: ")
money = input("Enter your cash amount: ")
hungry = input("Are you hungry? (Y/N) ")

match hungry:
    case "Y":
        if int(money) >= 30:
            print(f"{name} should go to eat breakfast.")
        else:
            print(f"{name} is hungry but not have enough money.")
    case "N":
        if int(money) >= 30:
            print(f"{name} has budget but doesn't want to eat breakfast.")
        else:
            print(f"{name} has no money but is not hungry.")
    case _:
        print("Please make sure that you enter either Y or N.")


# Structural Pattern Matching
# Switch statement ==
# or
lang = input("你希望学什么程式语言？")
if lang == "JavaScript":
    print("你会成为网页前端开发人员！")
elif lang == "PHP":
    print("你会成为网页后端开发人员！")
elif lang == "Python":
    print("你会成为资料科学家！")
elif lang == "Kotlin":
    print("你会成为Android应用程式开发人员！")
elif lang == "Swift":
    print("你会成为ios应用程式开发人员！")
else:
    print("你会成为其他开发人员！")

# match subject:
#      case <pattern_1>:
#           <action_1>
#      case <pattern_1>:
#           <action_2>
#      case _:
#           <action_wildcard>
lang = input("你希望学什么程式语言？")
match lang:
    case "JavaScript":
        print("你会成为网页前端开发人员！")
    case "PHP":
        print("你会成为网页后端开发人员！")
    case "Python":
        print("你会成为资料科学家！")
    case "Kotlin":
        print("你会成为Android应用程式开发人员！")
    case "Swift":
        print("你会成为ios应用程式开发人员！")
    case _:  # _ means none of the previous option is applicable
        print("你会成为其他开发人员！")

# example
command = input("Where do you wanna go?")
match (command.split(" ")):
    case ["Go", "home"]:
        print("You wanna go home.")
    case _:
        print("The system cannot determine where you wanna go.")

command = input("Where do you wanna go?")
match command.split(" "):
    case ["Go", "north"]:
        print("You are heading to the north.")
    case ["Go", "east"]:
        print("You are heading to the east.")
    case ["Go", "west"]:
        print("You are heading to the west.")
    case ["Go", "South"]:
        print("You are heading to the south.")
    case ["Turn", "left"]:
        print("You want to turn left.")
    case ["Turn", "right"]:
        print("You want to turn right.")
