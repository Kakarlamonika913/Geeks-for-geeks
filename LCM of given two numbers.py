def computeLCM(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0) and (greater%y==0):
            LCM=greater
            break
        greater=greater+1
    return LCM
number1=12
number2=14
print("lcm of 2 numbers{}and{}is{}".format(number1,number2,computeLCM(number1,number2)))
