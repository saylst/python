# 斐波那契数列


if __name__ == '__main__':
    n1, n2 = 0, 1
    count = 0
    number = int(input('请输入一个数字:'))

    if number < 0:
        print('负数无效，请输入正数.')
    elif number == 0:
        print('斐波那契数列为:')
        print(n1)
    else:
        print('斐波那契数列为:')
        print(n1, ',', n2, end=' , ')
        while count < number:
            print(n1 + n2, end=' , ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count = count + 1
