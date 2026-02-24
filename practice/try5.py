# def ask_for_int():
#     while True:
#         try:
#             result = int(input("Enter a number here:"))
#         except:
#             print("Invallid number. Please try again.")
#         else:
#             print("Good job!")
#             return result


# ask_for_int()

def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number here:"))
        except ValueError as ve:
            print(ve)
            print("Please try again.")
        else:
            print("Good job!")
            return result


ask_for_int()
