# find all the strong numbers between the given range
min_range = int(input("Enter Minimum Range: "))
max_range = int(input("Enter Maximum Range: "))

while min_range <= max_range:

    n = min_range
    temp = n
    fact_sum = 0

    while n > 0:
        r = n % 10
        i = 1
        fact = 1
        while i <= r:
            fact = fact * i
            i = i + 1

        fact_sum = fact_sum + fact
        n = n // 10

    min_range = min_range + 1

    if temp == fact_sum:
        print(temp, " is Strong Number")
