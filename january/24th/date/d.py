import datetime

x = datetime.datetime(2018, 8, 21)
print(x.strftime("%B")) # название месяца
print(x.strftime("%A")) # название дня недели
print(x.strftime("%d")) # название день месяца
print(x.strftime("%y")) # год
print(x.strftime("%H")) # час
print(x.strftime("%p")) # утреннее вечернее
