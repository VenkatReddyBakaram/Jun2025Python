set1 = set((1, 2, 3, 4, 5))
set2 = set((11, 22, 33, 44, 55))
set3 = set((13, 25, 37, 42, 53))
set4 = set((14, 28, 93, 84, 75))
set5 = set((21, 42, 73, 49, 51))
list1 = list((15, 23, 30, 42, 56))

set6 = set1.union(set2, set3, set4, set5)

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
print(set6)

set7 = set1 | set2 | set3 | set4 | set5 | set6
print(set7)

set8 = set1.union(list1)
print(set8)
