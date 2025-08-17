colours = list(("red", "Blue", "green", "Pink", "white"))

nums = [1, 2, 3, 4, 5]

number_colours = colours + nums

print(number_colours)

for num in nums:
    colours.append(num)

print(colours)
