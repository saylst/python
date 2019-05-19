# 合并去重

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [2, 4, 6, 8, 10]

    print(list1 + list2)
    print(set(list1 + list2))
    print(list(set(list1 + list2)))
