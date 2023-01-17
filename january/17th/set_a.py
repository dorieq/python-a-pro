n = int(input()) # считываем размер массива
a = list(map(int, input().strip().split()))[:n] # считываем сам массив
s = set() # считываем множество
for x in a: # for i in range(n): x = a[i]
    s.add(x) # добавляем в set числа
print(len(s)) # печатаем размер множества
#1 2 3 4 5 -> ['1', '2', '3', '4', '5'] -> [1, 2, 3, 4, 5]