min_range = int(input("Enter Min Range: "))
max_range = int(input("Enter Max Range: "))

for index in range(min_range, max_range, 1):

    n = index

    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count = count + 1
        i = i + 1

    if count <= 2:
        print(n, " is Prime Number")
