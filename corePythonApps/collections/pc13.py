colours = list(("red", "blue", "green", "pink", "white"))

new_colours = [
    colour for colour in colours if "r" in colour
]

print(colours)
print(new_colours)

colours = list(("red", "blue", "green", "pink", "white"))

new_colours = [
    colour.upper() for colour in colours
]

print(colours)
print(new_colours)

colours = list(("red", "blue", "green", "pink", "white"))

new_colours = [
    colour if colour != "green" else "black" for colour in colours
]

print(colours)
print(new_colours)
