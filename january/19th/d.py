def vote(a, b, c):
    res = 0
    if (a == True):
        res = res + 1
    if (b == True):
        res = res + 1
    if (c == True):
        res = res + 1
    if (res >= 2):
        return 1
    else:
        return 0

print(vote(1, 1, 0))