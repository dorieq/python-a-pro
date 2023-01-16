# break - используется для того, чтобы прервать цикл
# continue - используется для того, чтобы пропустить шаг
for i in range(1, 10):
    if i == 4:
        continue
    if i == 8:
        break
    print(i)