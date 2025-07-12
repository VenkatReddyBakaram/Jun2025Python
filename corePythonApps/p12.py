a = int(input("Enter the Number :"))

print("Original Number is :",a)

b=a//100
c=a%100
d=c//10
e=c%10

res = e+d+b

print("Sum of Given Number Individual Digits :",res)

