n = int(input("Enter The Number :"))

cub_sub = 0
temp = n

while n>0:
    r= n%10
    cub_sub = cub_sub+(r*r*r)
    n=n//10

print("Result is :",cub_sub)

if temp==cub_sub:
    print(temp," is ArmStrong Number")
else:
    print(temp," is not ArmStrong Number")

