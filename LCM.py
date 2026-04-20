#PYTHON PROGRAM TO FIND LCM OF THE GIVEN NUMBER
a=int(input("ENTER THE vALUE OF A:"))
b=int(input("ENTER THE VALUE OF B:"))
if(a>b):
  g=a
  l=b
else:
  g=b
  l=a
if(g%l==0):
   print("THE LCM IS:",g)
else:
   print("THE LCM IS:",g*l)
