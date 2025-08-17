fruits = list(("mango", "apple", "banana", "cherry"))

print(fruits[1])

fruits[1] = "orange"

print(fruits[1])

fruits[1:3] = ["apple", "cherry"]
print(fruits)

fruits[1:3] = ["watermelon"]

print(fruits)
