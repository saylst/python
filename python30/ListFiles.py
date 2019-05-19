# 列出当前目录下的所有文件和目录名
import os

if __name__ == '__main__':

    result = [d for d in os.listdir('.')]
    print(result)
