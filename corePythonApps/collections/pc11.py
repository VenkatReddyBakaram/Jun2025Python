# comprehension i.e. shortest syntax of loop
colours = list(("red", "blue", "green", "pink", "white"))

for colour in colours:
    print(colour)

print("=====================")

[print(colour) for colour in colours]
