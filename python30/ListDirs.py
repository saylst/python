# 输出某个路径下的所有文件和文件夹的路径
import os


def print_dir():
    filepath = input("请输入一个路径:")
    if filepath == "":
        print('请输入正确的路径。')
    else:
        for i in os.listdir(filepath):
            print(os.path.join(filepath, i))


if __name__ == '__main__':
    print_dir()
