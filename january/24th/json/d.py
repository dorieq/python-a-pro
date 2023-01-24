import json

x = {
    "name": "Dauren",
    "year": 2000,
    "city": "Atyrau"
}
y = json.dumps(x, sort_keys=True)
print(y)