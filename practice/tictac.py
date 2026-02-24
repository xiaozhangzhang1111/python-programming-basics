counter = 0
# 第一步，搭建棋盘
row1 = [' ', ' ', ' ']  # 1,2,3
row2 = [' ', ' ', ' ']  # 4,5,6 => row2 index 0,1,2
row3 = [' ', ' ', ' ']  # 7,8,9


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

# 第二步，使2个用户分别能交替输入不一样的棋子


def user_choice():
    choice = input("Please enter a number(1-9):")
    # no digits, not within 1-9
    while not choice.isdigit() or int(choice) not in range(1, 10):
        if not choice.isdigit():
            print("Sorry, your choice is not valid.")

        else:
            print("Your choice is not within the range of 1-9.")
        choice = input("Please enter a number(1-9):")
    return int(choice)


# display(row1, row2, row3)
# 1 user input o
# 2 user input x
# 3 user input o
# ... o和x 交替进行


def getCurrentSymbol():  # 轮流返回符号函数
    global counter  # 声明使用全局变量counter
    symbol_list = ['x', 'o']  # 符号列表，x和o交替
    counter += 1  # 第一次调用时counter为1，因此首次返回o
    return symbol_list[counter % 2]  # 对计数器值取模（除以2的余数），结果只能是0和1

# 第三步，使棋子对应在棋盘上的位置,确保位置是空格才可以赋值


def update_table(index):
    global row1, row2, row3
    if index in range(1, 4):
        if row1[index - 1] == ' ':  # 防止已经有棋子占用的格子被重复覆盖
            row1[index-1] = getCurrentSymbol()
            return True
        else:
            return False
    elif index in range(4, 7):
        # 4%3-1=0对应第一个元素，5%3-1=1对应第二个元素，6%3-1=-1对应最后一位元素
        if row2[index % 3 - 1] == ' ':
            row2[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False
    else:
        if row3[index % 3 - 1] == ' ':
            row3[index % 3 - 1] = getCurrentSymbol()
            return True
        else:
            return False
# update_table(1)
# update_table(4)
# update_table(7)
# update_table(8)
# update_table(2)

# display(row1, row2, row3)

# 确认赢家,通过8种连线情况来编写code，横3+竖3+斜2


def check_winning():
    player_1_wins = False
    player_2_wins = False
    if (row1[0] == row1[1] and row1[1] == row1[2] and (" " not in row1)):
        if (row1[0] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row2[0] == row2[1] and row2[1] == row2[2] and (" " not in row2)):
        if (row2[0] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row3[0] == row3[1] and row3[1] == row3[2] and (" " not in row3)):
        if (row3[0] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " " and row2[0] != " " and row3[0] != " ")):
        if (row1[0] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " " and row2[1] != " " and row3[1] != " ")):
        if (row1[1] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " " and row2[2] != " " and row3[2] != " ")):
        if (row1[2] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " " and row2[1] != " " and row3[2] != " ")):
        if (row1[0] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " " and row2[1] != " " and row3[0] != " ")):
        if (row1[2] == "x"):
            player_2_wins = True
        else:
            player_1_wins = True
    if player_1_wins:
        return "player 1 wins"
    elif player_2_wins:
        return "player 2 wins"
    else:
        return "no one wins"  # Tie game(平手)或者on-going game


def start_game():
    while True:
        display(row1, row2, row3)
        while True:
            choice = user_choice()
            if update_table(choice):
                break
            else:
                print("Wrong position to put your choice")
        result = check_winning()
        if result == "player 1 wins":
            display(row1, row2, row3)
            print("player 1 wins!! Congrats")
            return
        elif result == "playr 2 wins":
            display(row1, row2, row3)
            print("player 2 wins!! Congrats")
            return
        elif result == "no one wins" and counter == 9:
            display(row1, row2, row3)
            print("Tie game!!")
            return


start_game()
