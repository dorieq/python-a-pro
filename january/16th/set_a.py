n = int(input()) # вводим размер массива
a = list(map(int,input().strip().split()))[:n] # считываем сам массив
s = set() # создаем сет
for x in a: # проходимся по массиву
    s.add(x) # добавляем числа массива в set 
print(len(s)) # печатаем длину set