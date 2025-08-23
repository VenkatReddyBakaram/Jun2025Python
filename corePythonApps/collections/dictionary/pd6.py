cars = dict(
    brand="Ford",
    model="Mustang",
    year=1958,
    colours=["red", "blue", "green"]
)

print(cars)

cars["model"] = "EcoSport"

print(cars)

cars.update({'year': 2008})
print(cars)

cars["available_countries"] = ["india", "us", "uk"]
print(cars)

cars.pop("model")  # removes the keys from the given dictionary
print(cars)

cars.popitem()  # removes the last item automatically

print(cars)

cars.clear()
print(cars)

del cars
print(cars)  # will get an error called NameError: name 'cars' is not defined. because del removed from the memory
