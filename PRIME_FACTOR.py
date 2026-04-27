#PYTHON PROGRAM TO FIND THE PRIME FACTOR OF THE GIVEN NUMBER
def prime(x):
   for i in range(2,x):
      if(x%i==0):
         return 1
   return 0

a = int(input("Enter a number to find pfactor: "))
for i in range(2,a):
   if(prime(i)==0):
      if(a%i==0):
         print(f"\n{i}")
