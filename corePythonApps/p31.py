# This program is used to find the Sum of of given number's individual digits
n = int(input("Enter The Number :"))

sumV = 0

while n>0:
 r = n%10
 print("Individual Digit :",r)
 sumV = sumV+r
 n=n//10
 

print("Sum of Individual Digits of Given Number :",sumV)
 
 
 