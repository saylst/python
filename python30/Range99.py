# 打印九九乘法表

if __name__ == '__main__':

    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d x %d = %d \t' % (i, j, i * j), end='')
        print()
