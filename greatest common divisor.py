n1=int(input())
n2=int(input())
if n1>n2:
    min=n2
else:
    min=n1
for i in range(1,min+1):
    if(n1%1==0) and (n2%i==0):
        hcf=i
print(hcf)
