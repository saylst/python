# 计算 a*a + b*b + c*c + ……
def calc(*number):
    s = 0
    for n in number:
        s = s + n * n
    return s


if __name__ == '__main__':
    result = calc(1, 3, 5)
    print(result)
