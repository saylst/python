# 把一个 list 中所有的字符串变成小写

if __name__ == '__main__':
    L = ['Hello', 'World', 'IBM', 'Apple']
    result = [s.lower() for s in L]
    print(result)
