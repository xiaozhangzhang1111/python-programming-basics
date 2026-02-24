import one  # 模块导入时会立即执行模块的顶层代码
print("We are running codes in two.py now")


def get_name():  # 定义函数，但尚未调用
    print(__name__)


if __name__ == '__main__':  # 允许模块既可以被导入使用，也可以直接运行
    print("We are running two.py directly.")
    get_name()
else:
    print("one.py is being imported.")
    get_name()
    one.get_name()
