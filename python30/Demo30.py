# 获取昨天的日期
import datetime


def getyesterday():
    today = datetime.date.today()
    oneDay = datetime.timedelta(days=1)
    yesterday = today - oneDay
    return yesterday


if __name__ == '__main__':
    print(getyesterday())
