r = open("a.txt", "w")
# a - append w - write

r.write("ABCDE")
r.close()

r = open("a.txt", "r")
print(r.read())