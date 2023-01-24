import json

x = {
    "name": "Dauren",
    "year": 2000,
    "city": "Atyrau"
}
y = json.dumps(x, indent=4)
print(y)