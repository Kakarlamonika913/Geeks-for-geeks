n=int(input())
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem*rem*rem
    n=n//10
if(sum==temp):
    print("arm")
else:
    print("not")
    
