set1 = {"apple", "orange", "cherry"}
print(set1)

set2 = {"orange", "cherry", "banana"}
print(set2)

set3 = set1.symmetric_difference(set2)
print(set3)

print(set1)
print(set2)
set1.symmetric_difference_update(set2)
print(set1)

set1 = {"apple", "orange", "cherry"}
set5 = set1 ^ set2
print(set5)
