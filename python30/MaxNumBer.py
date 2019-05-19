# 获取最大值


if __name__ == '__main__':
    N = int(input('输入需要比对的数字个数:'))
    print('请输入需要比对的数字:')
    num = []
    for i in range(N):
        tempNum = int(input('输入第 %d 个数字:' % (i+1)))
        num.append(tempNum)

    print('您输入的数字为：', num)
    print('最大的数字为：', max(num))
