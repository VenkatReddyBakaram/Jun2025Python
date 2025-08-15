min_range = int(input("Enter Min Range: "))
max_range = int(input("Enter Max Range: "))

while min_range <= max_range:

    n = min_range

    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count = count + 1
        i = i + 1

    if count <= 2:
        print(n, " is Prime Number")

    min_range = min_range + 1
