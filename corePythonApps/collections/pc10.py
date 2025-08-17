colours = list(("red", "blue", "green"))

print(colours)

for colour in colours:
    print(colour)

for index in range(len(colours)):
    print(colours[index])

index = 0
while index < len(colours):
    print(colours[index])
    index += 1
else:
    print("Iteration is done")
