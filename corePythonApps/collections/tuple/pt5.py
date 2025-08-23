fruits = ("apple", "banana", "cherry")  # packing

(green, yellow, red) = fruits  # unpacking
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "dragon")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
