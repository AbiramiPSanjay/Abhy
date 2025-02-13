n=int(input("Enter the Number:"))
def col(n):
    while(n>1):
        print(n,end=' ')
        if(n%2==1):
           n=3*n+1
        else:
            n=n/2
col(n)            
print(1,end=' ')
