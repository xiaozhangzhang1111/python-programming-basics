# Comparison Operators
a = 10
b = 20
print(a == b)
print(a != b)

a = "Wilson"
b = "Wilson"
print(a == b)

# Assignment Operators
a = 10
b = 20
a += b
print(a)

# Logical Operators
a = True
b = False
print(not a)
print(a or b)

# Bitwise Operators
a = 60  # binary 00111100
b = 13  # binary 00001101
print(a & b)  # binary "and"
print(a | b)  # binary "or"
print(a ^ b)  # binary XOR (同时为1则为0，只有其中一个是1则为1，同时是0则为0)
print(~a)  # ones complement, means 11000011 in 2'scomplement form
print(a << 2)  # left shift all bits, get 11110000
print(a >> 2)  # right shift

# Truthy and Falsy values
if []:
    print("empty list is true in boolean context")
else:
    print("empty list is false in boolean context")

# Short-Circuit Evaluation
if 2 or (10 / 0):
    print("we got no error")

  # if (10 / 0) or 2:
    # print("we got no error")
    # it will shows error, because of the short-circuit will give the outcome when check the first one
