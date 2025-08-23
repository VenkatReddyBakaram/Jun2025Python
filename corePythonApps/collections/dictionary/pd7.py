cars = dict(
    brand="Ford",
    model="Mustang",
    year=1958,
    colours=["red", "blue", "green"]
)

for key in cars:
    print(key)

for value in cars.values():
    print(value)

for key, value in cars.items():
    print(key, "::", value)

new_cars = cars.copy()
print(new_cars)

another_cars = dict(new_cars)
print(another_cars)
