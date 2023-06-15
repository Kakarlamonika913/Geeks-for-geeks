#User function Template for python3



class Solution:

    def isPerfect(self,N):

        fact=[0]*10

        fact[0]=1

        #storing the factorial of all digits

        #makes sure we don't calculate factorial

        #for digits multiple time

        for i in range(1,10):

            fact[i]=fact[i-1]*i

        store=N  #storing original number

        Sum=0

        while(N):

            Sum+=fact[N%10] #adding factorials of digits

            N//=10

        return 1 if store==Sum else 0 





#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__=='__main__':

    t=int(input())

    for _ in range(t):

        N=int(input())

        ob=Solution()

        print(ob.isPerfect(N))   

# } Driver Code Ends
