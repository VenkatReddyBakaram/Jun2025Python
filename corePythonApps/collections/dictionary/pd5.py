cars = dict(
    brand="Ford",
    model="Mustang",
    year=1958,
    colours=["red", "blue", "green"]
)

car_information = cars.keys()
print(car_information)

for key in car_information:
    print(cars.get(key))

car_values = cars.values()

for value in car_values:
    print(value)

all_cars = cars.items()
print(all_cars)

if "model" in car_information:
    print("yes model is available")

if "Ford" in car_values:
    print("Ford's model is available")
