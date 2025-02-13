a=int(input("Enter the Number:"))
s=0
while(a!=0):
    s*=10
    s+=(a%8)
    a//=8
while(s!=0):
    a*=10
    a+=(s%10)
    s//=10
print(a)    
