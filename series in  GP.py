 res=1
        n=n-1
        while(n>0):
            if(n%2!=0):
                res=(res*r)%(pow(10,9)+7)
            r=r*r%(pow(10,9)+7)
            n=n//2
        return (a*res)%(pow(10,9)+7)

