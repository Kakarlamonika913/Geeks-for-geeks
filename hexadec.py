def hexa dec(hexa):
    length=len(hexa)
    sum=0
    j=0
    for i in range(length-1,-1,-1):
        print(sum)
        if (hexa[i]>='o' and hexa[i]<='o'):
            sum=sum+(ord(hexa[i]-48)*pow(16,j))
            j=j+1
        elif (hexa[i]>='a' and hexa[i]<='f'):
            sum=sum+(ord(hexa[i]-55))*pow(16,j)
            j=j+1
    return sum
hexa=input("enter")
print("decimal value of hexa",hexa,"=",hexa_dec(hexa))
            
            
