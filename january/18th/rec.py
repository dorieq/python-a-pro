

def rec(curr, n):
    if curr > n:
        ans = False
        return
    if curr == n:
        print('YES')
        return
    rec(curr + 3, n)
    rec(curr + 5, n)
    
rec(1, 5)
ans = True
if (ans == False):
    print('NO')
