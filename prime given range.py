n=int(input())
count=0
for i in range(2,n):
    if(n%i==0):
        count=count+1
        break
if(count==0):
    print("prime")
else:
    print("not prime")
