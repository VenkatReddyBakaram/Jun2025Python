set1 = {"apple", "orange", "cherry"}
print(set1)

set2 = {"orange", "cherry", "banana"}
print(set2)

set3 = set1.difference(
    set2)  # this method will return a new set that will contain only the items from the first set but not present into second set
print(set3)

set4 = set1 - set2  # - operator will work like a difference() method
print(set4)

print(set1)
print(set2)

set1.difference_update(set2)
print(set1)
