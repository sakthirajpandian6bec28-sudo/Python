# PROGRAM TO FIND THE COMMON ELEMENTS IN TWO STRINGS 
a=[22,33,44,55]
b=[11,88,99,00,666,101]
c=0
com=[]
for i in a:
   if i in b:
      com.append(i)
      c=c+1
if (c!=0):
   print ("YES")
   print(com)
else:
   print("NO")
