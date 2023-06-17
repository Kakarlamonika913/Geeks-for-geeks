
#User function Template for python3

class Solution:

    def nthTermOfAP(self,A1,A2,N):

        #calculating common difference

        difference=A2-A1

        #calculating nth ternm

        nthTerm=A1+(N-1)*difference

        return nthTerm

#{ 

 # Driver Code Starts

#Initial Template for Python 3

if __name__=='__main__':

    t=int(input())

    for _ in range(t):

        A1,A2,N=map(int,input().strip().split(' '))

        ob=Solution()

        print(ob.nthTermOfAP(A1,A2,N))  

# } Driver Code Ends
