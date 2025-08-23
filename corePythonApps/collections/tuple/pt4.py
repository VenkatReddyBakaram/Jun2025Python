colours = ('red', 'green', 'blue', 'yellow', 'magenta', 'cyan')
print(colours)

colours = list(colours)

colours[1] = "white"
print(colours)
print(type(colours))

colours = tuple(colours)
print(colours)
print(type(colours))

