import json

x = {
    "name": "Dauren",
    "year": 2000,
    "work": "dev"
}

y = json.dumps(x, indent=4)

print(y)