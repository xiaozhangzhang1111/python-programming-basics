# LBYL approach(Look before you leap)
def safe_divide_1(x, y):
    if y == 0:
        print("Divide by 0 attempt detected.")
        return None
    else:
        return x/y
    # 首先确认用是否可以拿来作除数

# EAFP(Easier to ask forgiveness than permission)


def safe_divide_2(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Divide by 0 attempt detected.")
        return None
# This is not real codes


def save_a_file():
    result = save_prefs()
    if result == 'error':
        print("Preference not saved.")
        return
    result = save_text()
    if result == 'error':
        print("Not enough memory")
        return
    result = save_format()
    if result == 'error':
        print("Format not saved.")
        return
# EAFP


def save_a_file():
    try:
        save_prefs()
        save_text()
        save_format()
    except:
        print("Something went wrong...")


try:
    f = open("testfile.txt", "w")
    f.write("write a test line.")
except TypeError:
    print("There is a type error")
except OSError:
    print("There is an OS Error")
finally:
    print("This will run no matter what")

# FileNotFoundError
try:
    with open("hello.txt") as f:
except FileNotFoundError:
    print("File not found...")
