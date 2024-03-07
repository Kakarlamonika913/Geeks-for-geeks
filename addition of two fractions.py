1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=(x1*y2)+(x2*y1)
y3=y1*y2
div=0
if x3>y3:
    div=y3
else:
    div=x3
for i in range(div,0,-1):
    if(x3%i==0 and y3%i=x=0):
        x3=x3//i
        y3=y3//i
print("sum of fractions",x3,"/",y3)
