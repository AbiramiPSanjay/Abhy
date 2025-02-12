n=int(input("Enter a number")
if n==0 & n==1:
   print(n,"is not a prime number")
elif n==2:
   print(n,"is a prime number")
elif n>1:
   for i in range (2,n):
      if (num%i)==0:
          print(n,"is not a prime number")
          print(i,"times",n//i,"is",n)
          break
      else:
          print(n,"is a prime number")
          break
else:
    print(n,"is not a prime number")
