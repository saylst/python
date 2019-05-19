# 判断奇偶数

if __name__ == '__main__':
    while True:
        try:
            num = int(input('请输入一个数:'))
        except ValueError:
            print('输入的不是整数.')
            continue
        if num % 2 == 0:
            print("%d 是偶数." % num)
        else:
            print("%d 是奇数." % num)
        break
