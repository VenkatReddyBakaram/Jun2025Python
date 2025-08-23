ford = {
    "model": "Mustang",
    "year": 1958,
    "colours": ["red", "blue", "green"]
}

bmw = {
    "model": "superb",
    "year": 1978,
    "colours": ["black", "magma", "green"]
}

audi = {
    "model": "verizon",
    "year": 1998,
    "colours": ["red", "blue", "green"]
}

all_brands = {
    "Ford": ford,
    "BMW": bmw,
    "Audi": audi
}

print(all_brands)
print(all_brands["Ford"])
print(all_brands["BMW"])

print(all_brands["Audi"]["model"])
print(all_brands["BMW"]["year"])

for brand in all_brands:
    print(brand)

for brand, car_info in all_brands.items():
    print(brand, car_info)

print("=================================")

for brand, car_info in all_brands.items():
    print(brand, car_info)

    for car in car_info:
        print(car, "::", car_info.get(car))
