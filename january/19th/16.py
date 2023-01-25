def fact(x):
    if (x == 1):
        return 1
    else:
        return x * fact(x - 1)

print(fact(6))

#fact(6) -> fact(5) * 6 -> fact(4) * 5 * 6 -> ... -> 1 * 2 * 3 * 4 * 5 * 6