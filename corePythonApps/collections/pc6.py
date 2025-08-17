colours1 = list(("red", "blue", "green"))
colours2 = list(("yellow", "pink", "white"))
print(colours1)
print(colours2)

colours1.extend(colours2)
print(colours1)
print(colours2)

colours3 = list(("red", "blue", "green"))
colours4 = set(("yellow", "pink", "white"))

print(colours3)
print(colours4)

colours3.extend(colours4)
print(colours3)
print(colours4)
