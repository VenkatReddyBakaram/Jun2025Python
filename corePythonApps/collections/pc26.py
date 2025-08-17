set1 = {"red", "blue", "green", "orange"}
set2 = {"yellow", "blue", "green", "white", "black"}

print(set1)
print(set2)

set3 = set1.intersection(set2)  # will return common elements from the both sets
print(set3)

set4 = set1 & set2  # works like intersection() method
print(set4)

print(set1)
print(set2)

set1.intersection_update(set2) # works like intersection but the result will be stored into same set unlike intersection() stored result into new set
print(set1)
