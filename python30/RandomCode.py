# 随机生成验证码的两种方式
import random,string

if __name__ == '__main__':
    list1 = []
    for i in range(65, 91):
        list1.append(chr(i))
    for j in range(97, 123):
        list1.append(chr(j))
    for k in range(48, 58):
        list1.append(chr(k))

    ma = random.sample(list1, 6)
    ma = ''.join(ma)
    print(ma)

    str1 = '0123456789'
    str2 = string.ascii_letters
    str3 = str1 + str2
    ma1 = random.sample(str3, 6)
    ma1 = ''.join(ma1)
    print(ma1)
