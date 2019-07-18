# 最小公倍数


def lcm(x, y):
    # 获取较大的数
    if x > y:
        bigger = x
    else:
        bigger = y

    while (True):
        if (bigger % x == 0) and (bigger % y == 0):
            result = bigger
            break
        else:
            bigger += 1
    return result


if __name__ == '__main__':
    print(lcm(6, 8))
