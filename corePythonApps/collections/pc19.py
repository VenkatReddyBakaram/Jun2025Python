set_data = set((10, 20, 40, 50, 60, 30, 30, 30, 30))

for item in set_data:
    print(item)

set_data.add(90)
[print(item) for item in set_data]

set_one = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
set_two = set([10, 20, 30, 40, 50, 60, 70, 80, 90])


print(set_one)
print(set_two)

set_one.update(set_two)
print(set_one)


