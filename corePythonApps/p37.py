# Find all armstrong numbers between the given range
min_range = int(input("Minimum Range: "))
max_range = int(input("Maximum Range: "))

while min_range <= max_range:

    n = min_range
    temp = n
    cub_sub = 0
    while n > 0:
        r = n % 10
        cub_sub = cub_sub + (r * r * r)
        n = n // 10

    if temp == cub_sub:
        print(temp, " is ArmStrong Number")

    min_range = min_range + 1
