t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    m=x*y
    n=z*24*60
    if(m<=n):
        print("YES")
    else:
        print("NO")
