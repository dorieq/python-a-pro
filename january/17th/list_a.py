n = int(input()) # считываем размер массива
a = list(map(int, input().strip().split()))[:n] # считываем сам массив
for i in range(n):
    if (i % 2 == 0):
        print(a[i])