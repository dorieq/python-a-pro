n = int(input()) # считываем размер массива
a = list(map(int, input().strip().split()))[:n] # считываем сам массив
cnt = 0
for i in range(n):
    if (a[i] > 0):
        cnt = cnt + 1
print(cnt)