#User function Template for python3

class Solution:
    def fullPrime(self,N):
        #code here
        i=2
        while(i*i<=N):
            if(N%i==0):
                return 0
            i=i+1    
        while(N>0):
            if(N%10!=2 and N%10!=3 and N%10!=5 and N%10!=7):
                return 0
            N//=10    
        return 1  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.fullPrime(N))
# } Driver Code Ends
