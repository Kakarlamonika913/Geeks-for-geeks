n=int(input())
flag=0
for i in range(1,n):
    if i*i==n:
        flag=1
        break
if flag==1:
    print("perfect square")
else:
    print("not")
