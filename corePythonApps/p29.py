# This program is used to find the reverser order of given number
n = int(input("Enter The Number :"))

rev = 0

while n>0:
 r = n%10
 rev = rev*10+r
 n=n//10
 

print("Reverse Order of Given Number :",rev)
 
 
 