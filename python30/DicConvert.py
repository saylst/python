# 把原字典的键值对颠倒并生产新的字典


if __name__ == '__main__':

    dic = {'A': 'a', 'B': 'b', 'C': 'c'}
    dic1 = {y: x for x, y in dic.items()}

    print(dic1)
