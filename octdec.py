def octdec(num):
    sum=0
    i=0
    while num!=0:
        rem=num%10
        sum+=rem*pow(8,i)
        i=i+1
        num=int(num//10)
    return sum
num=int(input("enter a number"))
dec=octdec(num)
print("decimal value of",num," = ",dec)
