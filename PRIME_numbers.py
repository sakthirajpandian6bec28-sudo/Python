#PYTHON FUNCTION TO FIND PRIME NUMBERS
def prime(x):
   i = 2
   while(i<x):
      if(x%i==0):
         return 1
      else:
         return 0
   i+=1
a = int(input("Enter a number: "))
if(prime(a)==0):
   print("PRIME")
else:
   print("NOT A PRIME")
