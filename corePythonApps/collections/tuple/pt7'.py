fruits = ("apple", "banana", "cherry", "dragon")

for fruit in fruits:
    print(fruit)

print("===================")

for index in range(len(fruits)):
    print(fruits[index])

print("==============================")

'''
index = 0
while index < len(fruit):
    print(fruits[index])
    index += 1
else:
    print("Iteration is done..!")

print("==================") '''

[print(fruit) for fruit in fruits]

index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
else:
    print("Iteration is done..!")

print("==================")
