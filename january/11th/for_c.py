from math import sqrt

a = int(input())
b = int(input())
for i in range(a, b + 1):
    t = int(sqrt(i))
    if (t * t == i):
        print(i)