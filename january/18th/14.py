def attach(func):
    func.data = 10
    return func

@attach
def add(x, y):
    return x + y

print(add(5, 15))
print(add.data)