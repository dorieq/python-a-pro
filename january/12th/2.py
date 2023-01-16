# if (condition1):
#   action1
# elif (condition2):
#   action2
# else:
#   action3
# == - ?, = - присвоение, == - вопрос, является ли первое выражение равным второму?

a = int(input())
if (a > 10):
    print('Хлеб')
elif (a == 10):
    print('Молоко')
else:
    print('10 хлебов')
a = 6
t1 = (6 == 7) #False
t2 = (6 == 6) #True