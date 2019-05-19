# 输出某个路径及其子目录下所有以.html 为后缀的文件
import os


def print_html(filePath):
    for i in os.listdir(filePath):
        path = os.path.join(filePath, i)
        if os.path.isdir(path):
            print_html(path)
        if path.endswith('.html'):
            print(path)


if __name__ == '__main__':
    print_html('D:\\Codes\\SaylstBlog')
