# and, or, xor
# True = 1 Or False = 0
# 1 and 0 = 0, 0 and 1 = 0 => True and False = False, True and True = True
# True or False = True, True or True = True
# True xor False = True, True xor True = False
# xor - excluding or(1 xor 0 = 1, 0 xor 1 = 1, 0 xor 0 = 0, 1 xor 1 = 0)
# and - &, or - |, xor - ^
a = 40 #22 apples, 12 orange, 6 tangerine
b = 30
c = 15
d = 10
if (b >= 22 & c >= 12 & d >= 6):
    print('Праздник удался')