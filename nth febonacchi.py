 prev1=1
        prev2=0
        for i in range(2,n+1):
            cur=prev1+prev2
            prev2=prev1
            prev1=(cur%1000000007)
        return prev1 
        
