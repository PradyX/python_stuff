list = ["a", "b", "c", "d"]
print(list)

list[2] = "e"
print(list)

if "e" == list:
    print("exist")
else:
    print("not exist")

list.pop(3)
print(list)

list.append("f")
print(list)
