import json

# JSON
x = '{"name": "Dauren", "year": 2000}'
print(type(x))
y = json.loads(x)
print(type(y))
print(y)