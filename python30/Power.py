# 计算 x 的 n 次方的方法
def power(x, n):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s


if __name__ == '__main__':
    result = power(5, 2)
    print(result)
