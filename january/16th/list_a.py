n = int(input()) # вводим размер массива
a = list(map(int,input().strip().split()))[:n] # считываем сам массив
for i in range(n): #проходимся по массиву
    if i % 2 == 0:
        print(a[i])