import random
# randint = random integer
secret = random.randint(1, 100)  # generate a random integer from 1 to 100
min_value = 1
max_value = 100
print(secret)
while True:
    guess = input(f"Make your guess(between {min_value} and {max_value}): ")
    # 这里的{}是f-string的语法，是字符串格式化的占位符，不代表集合
    if int(guess) < min_value or int(guess) > max_value:
        print("Your guess is not within the range!")
        continue
    if int(guess) == secret:  # guess前加“int”是因为input返回的是字符串
        print(f"The secret is {secret}")
        break
    elif int(guess) < secret:
        min_value = int(guess)  # 当guess小于secret，就把范围最小值更新为guess
    elif int(guess) > secret:
        max_value = int(guess)  # 同理，缩小猜测范围
