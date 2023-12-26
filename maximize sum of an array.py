 k=[]
        a.sort()
        # Complete the function
        for i in range(len(a)):
            k.append(a[i]*i) 
        l=sum(k)
        l=l%(10**9 +7)
        return l
