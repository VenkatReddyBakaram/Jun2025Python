cars = dict(
    brand="Ford",
    model="Mustang",
    year=1958,
    colours=["red", "blue", "green"]
)

print("Brand of your car is :", cars.get("brand"))
print("Model of your car is :", cars.get("model"))
print("Year of your car is :", cars.get("year"))
print("Colours of your car is :", cars.get("colours"))

(red, blue, green) = cars.get("colours")

print("Tha car ", cars.get("brand"), " is manufactured in year of :", cars.get("year"),
      " and introduced new model called :",
      cars.get("model"), " with various favourite colours :", red, ",", blue, ",", green)
