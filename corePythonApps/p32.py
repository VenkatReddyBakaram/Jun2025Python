#This program is used to print all polyndroms with in the given range

minV = int(input("Enter the Minimum Range from where you want to determine Polyndromes: "))
maxV = int(input("Enter the Maximum Range till which number you want to determine Polyndromes : "))

i=minV

while i<=maxV:   # Main/Outer loop
 
 n=i
 temp=n
 rev=0
 
 while n!=0:   # Inner/Nested Loop
  r=n%10
  rev= rev*10+r
  n=n//10
  
 
 if(temp==rev):
  print(temp," Reverse Order is :",rev," Hence it is polyndrome")  
 else:
  print(temp," Reverse Order is :",rev," Hence it is not a polyndrome")  
 
 i=i+1
