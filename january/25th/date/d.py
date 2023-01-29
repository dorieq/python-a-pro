## strftime
## %A - название дня
## %w - день недели
## %d - день 
## %B - название месяца
## %m - число месяца
## %y - число года
import datetime

x = datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%m"))
print(x.strftime("%B"))
print(x.strftime("%y"))