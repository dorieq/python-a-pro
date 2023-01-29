import json

x = {
    "name": "Dauren",
    "year": 2000,
    "work": "dev"
}

print(type(x))
y = json.dumps(x)
print(type(y))
print(y)