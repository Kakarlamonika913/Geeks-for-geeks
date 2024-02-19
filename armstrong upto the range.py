lower=int(input("enter lower range"))
upper=int(input("enter upper range"))
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while(temp>0):
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10

    if(num==sum):
        print(num)
