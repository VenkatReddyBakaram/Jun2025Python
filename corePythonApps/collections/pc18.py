set_data = set((1, 2, 3, 5, 4, 6))

for item in set_data:
    print(item)

if 10 in set_data:
    print("10 is available")
else:
    print("10 is not available")

if 10 not in set_data:
    print("10 is not available")
else:
    print("10 is available")
