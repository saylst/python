# 最大公约数


def hcf(x, y):
    # 获取较小的数
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            result = i

    return result


if __name__ == '__main__':
    print(hcf(6, 8))
