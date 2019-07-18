# 简单计算器


def add(x, y):
    """相加"""
    return x + y


def subtract(x, y):
    """相减"""
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


#用户输入计算
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")


if __name__ == '__main__':

    choice = input("输入你的选择(1/2/3/4):")

    num1 = int(input("输入第一个数字:"))
    num2 = int(input("输入第二个数字:"))

    if choice == '1':
        print(add(num1,num2))
    elif choice == '2':
        print(subtract(num1,num2))
    elif choice == '3':
        print(multiply(num1,num2))
    elif choice == '4':
        if num2 != 0:
            print(divide(num1,num2))
        else:
            print("分母不能为0")
    else:
        print("非法输入")