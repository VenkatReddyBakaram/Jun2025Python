n = int(input("Enter The Number :"))

temp = n
fact_sum = 0

while n > 0:
    i = 1
    fact = 1
    r = n % 10
    while i <= r:
        fact = fact * i
        i = i + 1

    fact_sum = fact_sum + fact
    n = n // 10

print("Result is :", fact_sum)

if temp == fact_sum:
    print(temp, " is Strong Number")
else:
    print(temp, " is not Strong Number")
