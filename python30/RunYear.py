# 判断闰年
import calendar

if __name__ == '__main__':
    year = int(input('请输入年份：'))
    check_year = calendar.isleap(year)
    if check_year:
        print("%d 是闰年" % year)
    else:
        print("%d 不是闰年" % year)
