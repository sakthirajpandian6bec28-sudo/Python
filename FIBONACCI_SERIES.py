# PYTHON FUNCTION FOR FIBONACCI SERIES USING RECURSION
def fibo(n):
   if(n<=0):
      return 0
   elif(n==1):
      return 1
   else:
      return fibo(n-1) + fibo(n-2)
n=int(input("ENTER THE NO.OF TERMS WE WANT:"))
for i in range(n):
   c=fibo(i)
   print(c,end=',')
