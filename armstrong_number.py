#PYTHON PROGRAM TO CHECK WHETHER ARMSTRONG OR NOT
d=0
a=int(input("ENTER THE NUMBER"))
a1=a
while(a>0):
    a=a//10
    d=d+1
a=a1
c=0
while(a>0):
    b=a%10
    a=a//10
    c+=b**d
if (a1==c):
    print("ARMSTRONG NUMBER ")
else:
    print(" NOT AN ARMSTRONG NUMBER")
