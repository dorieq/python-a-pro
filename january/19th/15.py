def attach(fun):
    fun.data = 10
    return fun

@attach
def add(x, y):
    return x + y

print(add(10, 20))
print(add.data)