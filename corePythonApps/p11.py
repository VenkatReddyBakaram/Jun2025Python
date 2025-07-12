a = int(input("Enter the Number :"))

print("Original Number is :",a)

b=a//100
c=a%100
d=c//10
e=c%10

res = e*100+d*10+b

print("Reverse Order of Given Number :",res)


