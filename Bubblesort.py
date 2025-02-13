a=[90,50,80,755,45,1,200,25,32,47,69]
n=len(a)
for i in range (n):
    for j in range (n-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print("Sorted Array",a) 
