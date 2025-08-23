colours = tuple(("red", "green", "yellow", "blue"))

new_colours = colours * 4
print(new_colours)

for colour in new_colours:
    print(colour)

print("=========================")

new_colours = colours * 5

index = len(new_colours) - 1
while index > 0:
    print(new_colours[index])
    index -= 1
else:
    print("Iteration is done..!")
