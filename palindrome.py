num=int(input("ENTER THE NUMBER"))
n=num
dig=0
rev=0
while(n!=0):
   dig=n%10
   rev=(rev*10)+dig
   n=n//10
print(rev)
if(num==rev):
   print(num,"is palindrome")
else:
   print(num,"is not palindrome")