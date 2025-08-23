cars = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1958,
    "colours": ["red", "blue", "green"]
}

print(cars)

print(cars['colours'])

for colour in cars['colours']:
    print(colour)

[print(colour) for colour in cars['colours']]
