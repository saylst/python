# 冒泡排序
def bubble_sort(test):
    for i in range(len(test) - 1):
        for j in range(len(test) - i - 1):
            if test[j] > test[j + 1]:
                test[j], test[j + 1] = test[j + 1], test[j]
    return test


if __name__ == '__main__':
    lis = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]
    bubble_sort(lis)
    print(lis)
