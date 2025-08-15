# This program is used to find the given number is polyndrome or not
n = int(input("Enter The Number :"))

rev = 0
temp = n

while n>0:
 r = n%10
 rev = rev*10+r
 n=n//10


print("Reverse Order of Given Number :",rev)

if temp==rev:
 print("Polyndrome")
else:
 print("Not Polyndrome") 
 
 